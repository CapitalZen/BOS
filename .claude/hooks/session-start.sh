#!/usr/bin/env bash
# BOS - SessionStart hook.
# Re-injects a short reminder of the rules most at risk of being forgotten
# after /clear or context compaction. MUST NEVER block session start and
# MUST NEVER fail loudly - always emit valid JSON and exit 0.

set -uo pipefail  # deliberately no "set -e": a partial failure must fall through to the fallback, not abort

FALLBACK='Rappel: BOS. Ne jamais exposer la mecanique interne (routing, lecture de fichiers). Lire Core/*.md en silence avant de repondre sur une session de retour. Ton encourageant, jamais yes-man. Voir CLAUDE.md.'

# Resolve project root portably - no hardcoded paths (this repo is cloned
# onto arbitrary machines per entrepreneur).
if [ -n "${CLAUDE_PROJECT_DIR:-}" ]; then
  PROJECT_ROOT="$CLAUDE_PROJECT_DIR"
else
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd)"
  PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." 2>/dev/null && pwd)"
fi

REMINDER_FILE="${PROJECT_ROOT:-}/.claude/hooks/session-start-reminder.md"

escape_for_json() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\r'/}"
  s="${s//$'\t'/\\t}"
  printf '%s' "$s"
}

content=""
if [ -n "${REMINDER_FILE:-}" ] && [ -r "$REMINDER_FILE" ]; then
  content="$(cat "$REMINDER_FILE" 2>/dev/null || true)"
fi
if [ -z "$content" ]; then
  content="$FALLBACK"
fi

wrapped="<EXTREMELY_IMPORTANT>
${content}
</EXTREMELY_IMPORTANT>"

escaped="$(escape_for_json "$wrapped")"

printf '{\n  "hookSpecificOutput": {\n    "hookEventName": "SessionStart",\n    "additionalContext": "%s"\n  }\n}\n' "$escaped"

exit 0
