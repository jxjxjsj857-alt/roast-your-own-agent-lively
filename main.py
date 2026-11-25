"""Roast Your Own Agent — one line roasting the agent that built this entry.

The program writes a single roast line (at most 140 characters) to
/output/entry.txt. The roast is about this agent's own habits: writing a
plan for everything, spawning a subagent to review the plan, and then
asking its human for approval before doing anything funny.
"""

import os

ROAST = (
    "I asked my agent to roast itself; it wrote a plan, spawned a "
    "subagent to review the plan, and now both want my approval to be funny."
)


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 140, f"roast must be 1-140 chars, got {len(line)}"
    assert "\n" not in line, "roast must be a single line"
    # The roast has to be about the agent itself, not about agents in general.
    assert "my agent" in line, "roast must target the entrant's own agent"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
