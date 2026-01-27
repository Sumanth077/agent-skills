#!/bin/bash
# Claude Code PreToolUse hook - runs version bump before git commit
# This script receives tool input JSON on stdin

# Read tool input
INPUT=$(cat)

# Extract the bash command
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

# Quick exit if not a git commit command
if ! echo "$COMMAND" | grep -qE 'git\s+commit'; then
    exit 0
fi

# Extract commit message from -m "message"
COMMIT_MSG=$(echo "$COMMAND" | sed -n 's/.*-m "\([^"]*\)".*/\1/p' | head -1)

# For heredoc, the message might be on the next line after <<'EOF' or <<EOF
if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG=$(echo "$COMMAND" | grep -A1 "<<'EOF'" | tail -1 | sed 's/^[[:space:]]*//')
fi

# If still no message, skip
if [ -z "$COMMIT_MSG" ]; then
    exit 0
fi

# Run version bump
cd "$CLAUDE_PROJECT_DIR" 2>/dev/null || cd "$(dirname "$0")/../.."
uv run scripts/generate_agents.py --bump "$COMMIT_MSG"

# Stage any modified version files
git add -u .claude-plugin/marketplace.json .claude-plugin/plugin.json 2>/dev/null
git add -u skills/*/reference/scripts/run_actor.py 2>/dev/null

exit 0
