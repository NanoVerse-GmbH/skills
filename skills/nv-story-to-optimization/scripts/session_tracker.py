#!/usr/bin/env python3
"""
session_tracker.py – Verfolgt Änderungen und Entscheidungen während einer Dev-Session

Verwendung:
  python scripts/session_tracker.py init <story-id>
  python scripts/session_tracker.py add-decision "<entscheidung>"
  python scripts/session_tracker.py add-file "<dateipfad>"
  python scripts/session_tracker.py summary
  python scripts/session_tracker.py reset
"""

import sys
import json
import os
from datetime import datetime

SESSION_FILE = "/tmp/.story_dev_session.json"


def load() -> dict:
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE) as f:
            return json.load(f)
    return {}


def save(data: dict):
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def init(story_id: str):
    data = {
        "story_id": story_id,
        "start": datetime.now().isoformat(),
        "decisions": [],
        "changed_files": [],
        "changes": []
    }
    save(data)
    print(json.dumps({"ok": True, "story_id": story_id}))


def add_decision(text: str):
    data = load()
    if not data:
        print(json.dumps({"error": "Session nicht initialisiert"}))
        return
    data["decisions"].append({"text": text, "ts": datetime.now().isoformat()})
    save(data)
    print(json.dumps({"ok": True, "decisions_count": len(data["decisions"])}))


def add_file(path: str):
    data = load()
    if not data:
        print(json.dumps({"error": "Session nicht initialisiert"}))
        return
    if path not in data["changed_files"]:
        data["changed_files"].append(path)
        save(data)
    print(json.dumps({"ok": True, "files_count": len(data["changed_files"])}))


def add_change(description: str, file_path: str = ""):
    data = load()
    if not data:
        print(json.dumps({"error": "Session nicht initialisiert"}))
        return
    entry = {"description": description, "ts": datetime.now().isoformat()}
    if file_path:
        entry["file"] = file_path
        if file_path not in data["changed_files"]:
            data["changed_files"].append(file_path)
    data["changes"].append(entry)
    save(data)
    print(json.dumps({"ok": True}))


def summary():
    data = load()
    if not data:
        print(json.dumps({"error": "Keine aktive Session"}))
        return
    print(json.dumps(data, ensure_ascii=False, indent=2))


def reset():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    print(json.dumps({"ok": True, "message": "Session zurückgesetzt"}))


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Kein Befehl angegeben"}))
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        init(sys.argv[2] if len(sys.argv) > 2 else "UNKNOWN")
    elif cmd == "add-decision":
        add_decision(sys.argv[2] if len(sys.argv) > 2 else "")
    elif cmd == "add-file":
        add_file(sys.argv[2] if len(sys.argv) > 2 else "")
    elif cmd == "add-change":
        file_arg = sys.argv[3] if len(sys.argv) > 3 else ""
        add_change(sys.argv[2] if len(sys.argv) > 2 else "", file_arg)
    elif cmd == "summary":
        summary()
    elif cmd == "reset":
        reset()
    else:
        print(json.dumps({"error": f"Unbekannter Befehl: {cmd}"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
