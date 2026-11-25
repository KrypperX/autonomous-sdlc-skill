#!/usr/bin/env python3
"""Read or list a licensed skill snapshot without extracting or executing it."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import tarfile

ROOT = Path(__file__).resolve().parent
CATALOG = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_id", help="ID from CATALOG.md")
    parser.add_argument("--file", default=None, help="Path inside the skill package; defaults to its SKILL.md")
    parser.add_argument("--list", action="store_true", help="List text and resource members in this skill package")
    args = parser.parse_args()
    skill = next((item for item in CATALOG["skills"] if item["id"] == args.skill_id), None)
    if skill is None:
        parser.error("unknown skill ID; see CATALOG.md")
    if skill["availability"] != "bundled":
        raise SystemExit("This skill is not bundled. Confirm it is actually available in the current Codex runtime and review its source/license before use.")
    source = CATALOG["sources"][skill["source_id"]]
    archive_path = (ROOT / source["archive"]).resolve()
    if ROOT.resolve() not in archive_path.parents or not archive_path.is_file():
        raise SystemExit("archive path is missing or outside the library")
    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    if digest != source["archive_sha256"]:
        raise SystemExit("archive digest does not match catalog; refuse to read")
    prefix = skill["archive_root"]
    if args.list:
        with tarfile.open(archive_path, "r:gz") as bundle:
            for member in bundle.getmembers():
                if member.name.startswith(prefix) and member.isfile():
                    print(member.name[len(prefix):])
        return 0
    rel = args.file or skill.get("entrypoint", "SKILL.md")
    relative = PurePosixPath(rel)
    if relative.is_absolute() or not relative.parts or any(part in ("", ".", "..") for part in relative.parts) or "\\" in rel:
        raise SystemExit("file path must stay inside the selected skill package")
    member_name = prefix + relative.as_posix()
    with tarfile.open(archive_path, "r:gz") as bundle:
        try:
            member = bundle.getmember(member_name)
        except KeyError:
            raise SystemExit("file is not present in this skill package; use --list to inspect available resources")
        if not member.isfile() or member.size > 16 * 1024 * 1024:
            raise SystemExit("only regular text files up to 16 MiB can be read")
        stream = bundle.extractfile(member)
        if stream is None:
            raise SystemExit("unable to read archived file")
        data = stream.read(16 * 1024 * 1024 + 1)
    try:
        sys.stdout.write(data.decode("utf-8"))
    except UnicodeDecodeError:
        raise SystemExit("selected member is not UTF-8 text; it was not extracted")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
