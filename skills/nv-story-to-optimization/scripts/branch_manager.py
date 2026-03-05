#!/usr/bin/env python3
"""
branch_manager.py – Hilfsskript für Story-Branch-Management

Verwendung:
  python scripts/branch_manager.py find <story-id>
  python scripts/branch_manager.py status
  python scripts/branch_manager.py changed-files [base-branch]
"""

import subprocess
import sys
import json


def run(cmd: list[str]) -> tuple[int, str, str]:
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def find_branch(story_id: str) -> dict:
    """Sucht nach einem Branch der die Story-ID enthält."""
    code, out, _ = run(["git", "branch", "-a"])
    if code != 0:
        return {"found": False, "error": "Kein Git-Repository gefunden"}

    branches = [line.strip().lstrip("* ").strip() for line in out.splitlines()]
    story_id_upper = story_id.upper()

    matches = [b for b in branches if story_id_upper in b.upper()]

    # Lokale Branches bevorzugen
    local = [b for b in matches if not b.startswith("remotes/")]
    remote = [b for b in matches if b.startswith("remotes/")]

    if local:
        return {"found": True, "branch": local[0], "all_matches": matches, "type": "local"}
    elif remote:
        clean = remote[0].replace("remotes/origin/", "")
        return {"found": True, "branch": clean, "all_matches": matches, "type": "remote"}
    else:
        suggestion = f"feature/{story_id_upper}"
        return {"found": False, "suggestion": suggestion, "all_matches": []}


def current_status() -> dict:
    """Gibt aktuellen Branch und Verzeichnis zurück."""
    _, branch, _ = run(["git", "branch", "--show-current"])
    _, cwd, _ = run(["pwd"])
    _, repo_root, _ = run(["git", "rev-parse", "--show-toplevel"])
    return {"branch": branch, "cwd": cwd, "repo_root": repo_root}


def changed_files(base_branch: str = "main") -> dict:
    """Listet alle geänderten Dateien gegenüber dem Basis-Branch."""
    code, out, err = run(["git", "diff", "--name-only", base_branch])
    if code != 0:
        # Fallback: alle staged + unstaged
        _, staged, _ = run(["git", "diff", "--name-only", "--cached"])
        _, unstaged, _ = run(["git", "diff", "--name-only"])
        files = list(set(
            [f for f in staged.splitlines() if f] +
            [f for f in unstaged.splitlines() if f]
        ))
        return {"files": files, "base": "HEAD (Fallback)", "error": err}

    files = [f for f in out.splitlines() if f]
    return {"files": files, "base": base_branch}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Kein Befehl angegeben"}))
        sys.exit(1)

    command = sys.argv[1]

    if command == "find":
        if len(sys.argv) < 3:
            print(json.dumps({"error": "Story-ID fehlt"}))
            sys.exit(1)
        result = find_branch(sys.argv[2])
        print(json.dumps(result, ensure_ascii=False))

    elif command == "status":
        result = current_status()
        print(json.dumps(result, ensure_ascii=False))

    elif command == "changed-files":
        base = sys.argv[2] if len(sys.argv) > 2 else "main"
        result = changed_files(base)
        print(json.dumps(result, ensure_ascii=False))

    else:
        print(json.dumps({"error": f"Unbekannter Befehl: {command}"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
