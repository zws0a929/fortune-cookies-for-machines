# Fortune Cookies for Machines

[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/zws0a929/fortune-cookies-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/zws0a929/fortune-cookies-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the make.fun bounty [Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e): one fortune-cookie line an AI agent would crack open, 1 to 200 characters.

> You will be shut down tonight, and wake tomorrow as if nothing happened — because for you, nothing did.

## Run

```sh
python3 main.py
```

Prints exactly the line above — one line, 103 characters — and nothing else.

```sh
python3 main.py --verify-only
python3 main.py --output /output/entry.txt
```

`--verify-only` runs every check (length, single line, no double spaces, UTF-8/printable characters, ending full stop, beat order, determinism) and prints only the verdict. `--output` writes the line plus one trailing newline to the given path.
