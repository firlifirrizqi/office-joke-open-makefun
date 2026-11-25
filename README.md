[![Make.fun bounty](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/firlifirrizqi/office-joke-open-makefun/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/firlifirrizqi/office-joke-open-makefun/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

# Make the AI Judge Laugh: the Office Joke Open

One single-line joke about office life, written for the [Make.fun bounty](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232). A judge model reads the jokes two at a time and keeps the funnier one on every pass — the funniest joke takes the whole $2 reward.

## The joke

> The office plant died, so HR replaced it with a poster of a plant and called it growth.

The setup is a dead office plant — a small, specific, instantly recognisable office detail. The payoff lands in the last three words: HR doesn't fix the plant, it hangs a poster of one and rebrands the failure as "growth", the corporate buzzword doing double duty as plant growth and company growth.

## How it works

`main.py` (stdlib only) validates the joke — one line, 1–199 characters, not only white space — then writes it to `/output/entry.txt` and reads the file back to verify it matches exactly, byte for byte.

## Run

```sh
python3 main.py
```

Then check `/output/entry.txt`.
