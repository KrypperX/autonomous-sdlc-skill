# Central skill library use

The [central catalog](skill-library/CATALOG.md) is the routing source for the locally installed skill set captured with this product. It maps each unique skill to the six SDLC functions and names whether the content is bundled, system-managed, product-owned or only usable from an installed runtime.

## Task-time routing

1. Identify the current SDLC stage, owner role and concrete acceptance gap.
2. Consult the matching role section in the catalog. Read only one primary specialist method for each gap; add a second only for a distinct concern.
3. For a bundled entry, resolve `read_skill.py` relative to the loaded `autonomous-sdlc/SKILL.md` and stream its `SKILL.md` with `python3 <library-root>/read_skill.py <skill-id>`. Use `--list` to discover packaged references and `--file path/inside/package.md` to read only the relevant one.
4. For an installed-only entry, confirm that exact skill is available in the current Codex runtime before use. The catalog is not evidence that an unbundled skill can be invoked.
5. Apply the selected method through authorized tools and return actual action/artifact and verification evidence to the same task contract. Record selected, loaded, applied, verified, blocked or not applicable separately; reading alone is not application. A specialist remains subordinate to the coordinator and repository policy.

The library contains source snapshots as passive reference material. A skill's presence in the catalog does not authorize its scripts, package installation, network access, issue/PR writes, release actions or deployment. Review any code sample before running it, and verify version-sensitive claims against current primary documentation.

## Portability

Bundled source files are packed in archives so Codex does not discover dozens of nested skills as separate global skills. The standard-library reader checks the archive digest, confines lookup to the selected package, and streams UTF-8 files without extracting or executing them. Archives and reader code do not add dependencies to the target software project's runtime.

See [catalog](skill-library/CATALOG.md), [source and license provenance](skill-library/PROVENANCE.md), and [library handling notes](skill-library/README.md).
