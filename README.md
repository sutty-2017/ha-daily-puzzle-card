# Daily Puzzle for Home Assistant

A shared daily puzzle integration and dashboard card for Home Assistant. Play one household puzzle each day, keep a shared streak, and automatically clear the game from the dashboard after it is solved.

> **v0.1.0 preview:** installable for Home Assistant testing. The included puzzle bank is intentionally small while gameplay and state handling are validated.

This project is experimental, intended for personal/community use, and developed with AI assistance.

## Included in v0.1.0

- **Word Grid** — a five-letter daily word game
- **Four of a Kind** — find four groups of four related words
- One shared game state across all Home Assistant dashboards
- Persistent lifetime puzzles solved
- Current daily streak
- Best daily streak
- Today's game and status sensors
- Solved card remains visible for 10 minutes, then hides
- Local puzzle selection; no API key or cloud puzzle service

## Installation

### HACS custom repository

1. In HACS, add `https://github.com/sutty-2017/ha-daily-puzzle-card` as a **custom repository** with category **Integration**.
2. Install **Daily Puzzle**.
3. Restart Home Assistant.
4. Go to **Settings → Devices & services → Add integration** and search for **Daily Puzzle**.
5. Add it once.

### Dashboard resource

The integration serves its card JavaScript locally. In **Settings → Dashboards → Resources**, add:

```
/daily_puzzle/daily-puzzle-card.js
```

Set the resource type to **JavaScript Module**, then refresh the browser/app.

### Add the card

Add a Manual card with:

```yaml
type: custom:daily-puzzle-card
```

Optional:

```yaml
type: custom:daily-puzzle-card
title: Daily Puzzle
hide_after: 600
```

`hide_after` is in seconds.

## Entities

The integration creates sensors for:

- Daily Puzzle Status
- Daily Puzzle Daily streak
- Daily Puzzle Best daily streak
- Daily Puzzle Puzzles solved
- Daily Puzzle Today's game

The Status sensor also contains today's shared game state and completion timestamp as attributes.

## How daily puzzles work

The integration assigns the game type by day. Puzzle content is bundled locally with the card and selected deterministically from the date, so everyone using the same version receives the same daily puzzle. Progress is stored by the integration in Home Assistant storage, not in an individual browser.

The current v0.1.0 bank is for functional testing. Expanding and curating the puzzle library is a priority before calling the project stable.

## Privacy and network use

Daily Puzzle does not require an external puzzle server, account, AI API, or API key. Gameplay data remains in Home Assistant's local integration storage.

## Disclaimer

This is an independent Home Assistant community project. It is not affiliated with or endorsed by The New York Times, Wordle, Connections, Home Assistant, or Nabu Casa. Game mechanics may be inspired by familiar word-puzzle formats, but puzzle content and presentation are original to this project.
