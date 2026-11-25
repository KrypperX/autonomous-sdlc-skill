# Source and license provenance

Captured from the two direct user skill roots on 2026-11-25. The inventory found 100 `SKILL.md` files across `~/.codex/skills` and `~/.agents/skills`, resolving 19 duplicate definitions to 81 unique skill names. Four broken symlinks are excluded. The separate Codex plugin cache is excluded because plugin-managed packages are not part of the direct core skill roots.

## Packaged snapshots

| Package | Skills | Source revision / snapshot | License evidence |
|---|---:|---|---|
| Context Engineering Collection | 25 | Installed local snapshot, SHA-256 recorded in `catalog.json`; no commit recorded locally | MIT `LICENSE` from the installed collection, retained inside the archive; the nested `examples/llm-as-judge-skills/LICENSE` is retained too |
| Matt Pocock skills | 39 | `abeeaf95660ba9e8b7c753eb38f441ca707a8823` | MIT `LICENSE` at that exact commit, retained as `mattpocock-skills/LICENSE` |
| OpenTUI | 1 | Installed well-known archive digest `sha256:576bf5cdc06115f2e0e3b9d5bd21dbed294f1289d1d96c4cb209e77d1d037054`; docs include 0.9.5 | MIT `LICENSE` from upstream v0.9.5, retained as `opentui/LICENSE` |
| TUI Design | 1 | `716633c308ac847f96741fac37c5c11bb234df8e` | MIT `LICENSE` at that exact commit, retained as `tui-design/LICENSE` |

Each archive's final SHA-256 and source-tree digest are stored in `catalog.json`. Package file contents are preserved; archive file modes are normalized to non-executable `0644`. The library reader verifies the archive digest before displaying any file.

## Not redistributed

Nine installed entries are catalog-only because a redistribution grant or source provenance was not established: seven local Codex skills with no origin/license record, `create-agent-tui` from OpenRouterTeam (pinned locally but no redistribution license found in the reviewed source), and `reverse-engineer-anything` with no installation source recorded. The catalog points to the exact OpenRouterTeam commit for discovery and use only when that skill is independently present in the runtime.

Five Codex system skills remain system-managed, and `autonomous-sdlc` remains the product's own entrypoint. They are inventoried but not copied into vendor archives. Broken symlinks and plugin-cache skills are not counted as installed core skills.

## License references

- [Context Engineering Collection](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) — MIT license included in the local snapshot.
- [Matt Pocock skills at the pinned revision](https://github.com/mattpocock/skills/tree/abeeaf95660ba9e8b7c753eb38f441ca707a8823) — [LICENSE](https://raw.githubusercontent.com/mattpocock/skills/abeeaf95660ba9e8b7c753eb38f441ca707a8823/LICENSE).
- [OpenTUI v0.9.5](https://github.com/anomalyco/opentui/releases/tag/v0.9.5) — [LICENSE](https://raw.githubusercontent.com/anomalyco/opentui/v0.9.5/LICENSE).
- [TUI Design at the pinned revision](https://github.com/gfargo/tui-design-skill/tree/716633c308ac847f96741fac37c5c11bb234df8e) — [LICENSE](https://raw.githubusercontent.com/gfargo/tui-design-skill/716633c308ac847f96741fac37c5c11bb234df8e/LICENSE).
- [OpenRouterTeam create-agent-tui at the pinned revision](https://github.com/OpenRouterTeam/skills/tree/a110aad6072364da5e8017efc7a7873262164b11/skills/create-agent-tui) — catalog only; no redistribution grant identified.
