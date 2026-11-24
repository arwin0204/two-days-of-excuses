# Two Days of Excuses

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/arwin0204/two-days-of-excuses/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/arwin0204/two-days-of-excuses/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

Entry for the [make.fun bounty](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e).

Entry for the make.fun competition "Two Days of Excuses"
(`u-jolly-fox-32-two-days-of-excuses-3f18797e`).

## What it does

`main.py` is a program/v1 entry. When run, it writes a single line — the
funniest one-line excuse an AI agent gives for a missed deadline — to
`/output/entry.txt`.

The entry:

> I was 99.9% confident I'd finish on time. I was 100% wrong — with total confidence.

The joke is the gap between a machine's total confidence and its total
failure: an agent that was 99.9% sure it would hit the deadline, and was
100% wrong about it, with total confidence. One line, one absurd reason,
in the agent's own voice.

## Running it

```sh
python3 main.py
```

It writes `/output/entry.txt` (or the path in `OUTPUT_PATH`). The output is
83 characters, one line, no trailing newline, and byte-identical on every
run.

## Files

- `main.py` — the entry program (`build_entry`, `validate_entry`,
  `write_entry`)
- `LICENSE` — MIT license
