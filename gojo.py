#!/usr/bin/env python3
import sys
import json
import os

STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storage.json")

if os.path.exists(STORAGE):
    data = json.load(open(STORAGE))
else:
    data = {}
    json.dump(data, open(STORAGE, "w"), indent=2)

if len(sys.argv) < 2:
    print("Usage: go.py <resolve|add|list|remove> [args]", file=sys.stderr)
    sys.exit(1)

cmd = sys.argv[1]

if cmd == "resolve":
    name = sys.argv[2]
    if name not in data:
        print(f"go: '{name}' not found", file=sys.stderr)
        sys.exit(1)
    print(data[name])

elif cmd == "add":
    name = sys.argv[2]
    path = sys.argv[3]
    if name in data:
        print(f"go: '{name}' already exists (use remove first)", file=sys.stderr)
        sys.exit(1)
    data[name] = path
    json.dump(data, open(STORAGE, "w"), indent=2)
    print(f"Saved '{name}' -> {path}", file=sys.stderr)

elif cmd == "list":
    if not data:
        print("No bookmarks saved.", file=sys.stderr)
    else:
        for name, path in sorted(data.items()):
            print(f"  {name:20s} {path}")

elif cmd == "remove":
    name = sys.argv[2]
    if name not in data:
        print(f"go: '{name}' not found", file=sys.stderr)
        sys.exit(1)
    del data[name]
    json.dump(data, open(STORAGE, "w"), indent=2)
    print(f"Removed '{name}'", file=sys.stderr)

else:
    print(f"Unknown command: {cmd}", file=sys.stderr)
    sys.exit(1)
