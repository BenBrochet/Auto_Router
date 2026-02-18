GO
go is a lightweight directory bookmarking utility for Zsh powered by a Python backend and a persistent JSON data store. It allows short aliases to map to directory paths for instant navigation.
Description
GO is structured in two layers:
Zsh layer — parses commands and performs cd
Python backend — manages bookmarks, resolves paths, and handles JSON storage
Because a child process cannot modify its parent shell’s working directory, the Python backend prints the resolved absolute path to stdout. The Zsh layer captures that output and performs the directory change within the active shell.
This preserves a clean separation between environment control and application logic.
Architecture
Zsh Layer (go.zsh)
  • Command routing
  • Argument parsing
  • Directory transitions

Python Backend (go.py)
  • CRUD bookmark management
  • Alias resolution
  • JSON read/write operations

storage.json
  • Persistent key-value store
Usage
go add <name>     # Save current directory
go <name>         # Navigate to bookmark
go list           # List bookmarks
go rm <name>      # Remove bookmark
Technical Notes
Shell and backend logic are deliberately decoupled
stdout is reserved for resolved paths
stderr handles errors
Non-zero exit codes propagate correctly
Storage path resolves relative to __file__ for portability
