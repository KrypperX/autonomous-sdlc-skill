# Central skill library

The repository packages the machine-installed skill inventory as a task-scoped reference library for `autonomous-sdlc`. The catalog has one row per unique skill name; duplicate local copies are resolved to one canonical source. Plugin caches are excluded.

## Use by the workflow

1. Match the current task to its SDLC stage and owner role in [CATALOG.md](CATALOG.md).
2. Read one matching method only when it fills a concrete gap.
3. For a bundled source, use `python3 read_skill.py <skill-id>` to read the entrypoint, `--list` to see its package resources, and `--file path/inside/package.md` to read a supporting document. The reader verifies the archive SHA-256, rejects path traversal and non-regular files, streams text only, and never extracts or executes it.
4. For an installed-only entry, verify the skill is present in the current runtime before using it. Its source text is not redistributed by this repository.
5. Apply the selected method inside the coordinator's task contract, stage gates and evidence map. User instructions and repository policy keep precedence.

## Safety and scope

Bundled content is third-party reference material. Its inclusion does not make its scripts trusted or runnable. Review any individual code sample or script in the context of the task before execution. Do not install example dependencies into the target project, grant skills access to credentials, or let a specialist authorize external writes, releases or deployment. Verify version-sensitive claims against current primary documentation.

The archive snapshots add no dependency to the target project's runtime. The only reader uses Python's standard library; it is a development-time Codex helper. Source and license records are in [PROVENANCE.md](PROVENANCE.md), and machine-readable routing data is in [catalog.json](catalog.json).
