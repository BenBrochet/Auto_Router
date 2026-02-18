GO_DIR="${0:a:h}"


go() {
  if [[ $# -eq 0 ]]; then
    print "Usage:"
    print "  go <name>        # jump to bookmark"
    print "  go add <name>    # save current dir as <name>"
    print "  go rm <name>     # remove bookmark"
    print "  go list          # show all bookmarks"
    return 0
  fi

  case "$1" in
    add)
      if [[ -z "$2" ]]; then
        print "go add: missing name" >&2
        return 1
      fi
      python3 "$GO_DIR/gojo.py" add "$2" "$(pwd)"
      ;;
    rm)
      if [[ -z "$2" ]]; then
        print "go rm: missing name" >&2
        return 1
      fi
      python3 "$GO_DIR/gojo.py" remove "$2"
      ;;
    list)
      python3 "$GO_DIR/gojo.py" list
      ;;
    *)
      local target
      target=$(python3 "$GO_DIR/gojo.py" resolve "$1" 2>/dev/null)
      if [[ $? -ne 0 ]]; then
        print "go: '$1' not found" >&2
        return 1
      fi
      cd "$target" || return 1
      ;;
  esac
}
