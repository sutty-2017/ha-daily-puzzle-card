# Daily Puzzle for Home Assistant

A shared daily puzzle integration and companion dashboard card for Home Assistant. One household puzzle is selected each day, progress is shared across dashboards, and Home Assistant entities expose completion and stats for automations and dashboard visibility rules.

> **Current release: v0.4.0**

This project is experimental, intended for personal/community use, and developed with AI assistance.

## Games

### Word Grid
A daily word-guessing game with configurable **3–7 letter** answers and six guesses. Optional hints can reveal letters, and the bundled library now contains hundreds of answers across the supported lengths.

### Four of a Kind
Find four groups of four related words. The game supports configurable mistake limits, two-stage hints, custom solved-group colors, and a **300-board** daily rotation backed by a much larger authored category bank.

### Word Weave
Trace themed words through neighboring letters in a 6×6 grid, including diagonal connections. Every cell belongs to an answer and each board includes a special **Theme Thread** spanning the grid. v0.4.0 includes **300 authored themes** with theme-first deterministic rotation and validated grid orientations.

## Highlights

- Three daily games: **Word Grid, Four of a Kind, and Word Weave**
- **Reveal Answer** after a failed attempt without awarding solve credit
- Special puzzles for major U.S. holidays and popular cultural dates across all three games
- Choose which games participate in the daily rotation
- Shared, persistent household progress across Home Assistant clients
- Compact dashboard card that fills its available card height and opens a large play popup
- Minimize the popup and continue later
- Smooth local HH:MM:SS countdown without second-by-second Home Assistant state traffic
- Completed-board view after solving
- **Replay today's puzzle** without changing official completion or stats
- Current streak, best streak, lifetime puzzles solved, and **No-Hint Solves**
- Optional hints with game-specific behavior
- Configurable Word Grid length and Four of a Kind mistake limit
- **Cozy Style** plus visual card controls for background, accent, title, keyboard, tile, and solved-group colors
- Admin/Test Mode for switching and resetting games without affecting official daily stats
- Reset Today's Puzzle and Reset All Stats controls in integration settings
- Completed binary sensor for dashboard visibility and automations
- Bundled card is automatically served and registered by the integration
- Local deterministic puzzle selection; no puzzle API, AI service, account, or API key required
- Rendering is designed to preserve in-progress input and selections during unrelated Home Assistant updates

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

The visual editor exposes the card's appearance settings. Game behavior such as enabled games, Word Grid length, hints, and Four of a Kind mistake limits is configured from the integration's **Configure** screen.

## Entities

Daily Puzzle creates entities for:

- **Completed** — binary sensor; ON once today's official puzzle has been completed
- **Status** — current play state and shared board data
- **Today's game**
- **Time remaining** — time until the next daily puzzle, including the exact next-puzzle timestamp
- **Daily streak**
- **Best daily streak**
- **Puzzles solved**
- **No-Hint Solves**

The Completed sensor intentionally stays ON during Replay. Replay resets only the active playable board; it does not erase the day's official completion or award stats a second time.

## Dashboard visibility

Daily Puzzle does not hide itself after completion. Use Home Assistant's normal card **Visibility** conditions with the Completed binary sensor if you want the card hidden, shown, or conditionally displayed after solving.

This keeps presentation policy in Home Assistant: another household may prefer to leave the completed board available all day.

## How daily puzzles work

The integration chooses the game and bundled puzzle deterministically from Home Assistant's local date. The backend owns puzzle answers, validation, shared progress, daily rollover, completion, and statistics. The card is the presentation layer.

All puzzle content is bundled locally. The card's countdown animates once per second in the browser while the Home Assistant time-remaining entity updates much less frequently, avoiding unnecessary recorder/state traffic just to animate seconds.

## Replay and Admin/Test Mode

After the first official solve, the original completed board is retained. Pressing **Replay today's puzzle** starts the same daily puzzle again and displays an **Already completed today** indicator.

Replay never turns the Completed sensor back off, removes the original completion, increments Puzzles solved again, or changes the day's streak credit.

**Admin/Test Mode** lets you switch among Word Grid, Four of a Kind, and Word Weave and reset the test board for development or casual play. Test-mode activity does not affect the official daily completion, streak, solved totals, or no-hint totals. Returning to Today restores the real daily state.

## Privacy and network use

Daily Puzzle does not require an external puzzle server, account, AI API, or API key. Gameplay data remains in Home Assistant's local integration storage.

## Disclaimer

This is an independent Home Assistant community project. It is not affiliated with or endorsed by The New York Times, Wordle, Connections, Strands, Home Assistant, or Nabu Casa. Game mechanics may be inspired by familiar word-puzzle formats, but puzzle content, game names, and presentation are original to this project.
