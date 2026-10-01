# Daily Puzzle for Home Assistant

A shared daily puzzle integration and companion dashboard card for Home Assistant. One household puzzle is selected each day, progress is shared across dashboards, and Home Assistant entities expose completion and stats for your own automations and dashboard visibility rules.

> **v0.1.0:** first installable community release.

This project is experimental, intended for personal/community use, and developed with AI assistance.

## Included in v0.1.0

- **Word Grid** — a five-letter daily word puzzle
- **Four of a Kind** — find four groups of four related words
- Compact dashboard card that opens a large play popup
- Minimize the popup and continue later
- Shared, persistent progress across Home Assistant clients
- Completed-board view after solving
- **Replay today's puzzle** without changing the day's completion, streak, or total
- Clear **Already completed today** indicator during replay
- Current streak, best streak, and lifetime puzzles solved
- Completed binary sensor for dashboard visibility and automations
- Time-remaining sensor plus a smooth HH:MM:SS countdown on the card
- Four customizable Four of a Kind group colors in the visual card editor
- Bundled card is automatically served and registered by the integration
- Local puzzle selection; no puzzle API, AI service, account, or API key required

## Installation

### HACS custom repository

1. In HACS, add this repository as a **custom repository** with category **Integration**.
2. Install **Daily Puzzle**.
3. Restart Home Assistant.
4. Go to **Settings → Devices & services → Add integration** and search for **Daily Puzzle**.
5. Add it once.
6. Add the **Daily Puzzle** card from the dashboard card picker.

The integration bundles and registers its Lovelace card automatically. A manual Dashboard Resource is not normally required.

### Manual card YAML

    type: custom:daily-puzzle-card

The visual editor also lets you change the card title and the four solved-group colors.

## Entities

Daily Puzzle creates:

- **Completed** — binary sensor; ON once today's puzzle has been completed
- **Status** — current play state and shared board data
- **Today's game**
- **Time remaining** — time until the next daily puzzle; includes the exact next-puzzle timestamp
- **Daily streak**
- **Best daily streak**
- **Puzzles solved**

The Completed sensor intentionally stays ON after Replay. Replay resets only the playable board; it does not erase the day's completion or award stats a second time.

## Dashboard visibility

Daily Puzzle does not hide itself after completion. Use Home Assistant's normal card **Visibility** conditions with the Completed binary sensor if you want the card hidden, shown, or conditionally displayed after solving.

This keeps presentation policy in Home Assistant: another household may prefer to leave the completed board available all day.

## How daily puzzles work

The integration chooses the game and bundled puzzle deterministically from Home Assistant's local date. The backend owns puzzle answers, validation, shared progress, daily rollover, completion, and statistics. The card is the presentation layer.

The card's countdown animates once per second in the browser, while the Home Assistant time-remaining entity updates at a much lower rate. This avoids unnecessary recorder/state traffic just to animate seconds.

## Replay behavior

After the first solve, the original completed board is retained. Pressing **Replay today's puzzle** starts the same daily puzzle again and displays an **Already completed today** indicator.

Replay never turns the Completed sensor back off, removes the original completion, increments Puzzles solved again, or changes the day's streak credit.

## Privacy and network use

Daily Puzzle does not require an external puzzle server, account, AI API, or API key. Gameplay data remains in Home Assistant's local integration storage.

## Disclaimer

This is an independent Home Assistant community project. It is not affiliated with or endorsed by The New York Times, Wordle, Connections, Home Assistant, or Nabu Casa. Game mechanics may be inspired by familiar word-puzzle formats, but puzzle content and presentation are original to this project.
