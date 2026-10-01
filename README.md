# Daily Puzzle Card for Home Assistant

A shared daily puzzle card for Home Assistant, featuring Wordle- and Connections-inspired games designed to be played together from your dashboard.

> **Status:** Early development / v0.1.0. This project is experimental, intended for personal use, and developed with AI assistance.

## Goals

- One shared puzzle each day
- Word Grid and Connections-style puzzle modes
- Shared progress across Home Assistant dashboards
- Automatically hide the completed puzzle after a configurable delay
- No external puzzle service required
- Home Assistant-native appearance
- Easy installation through HACS when the project matures

## v0.1 architecture

The frontend card contains the puzzle bank and selects the daily puzzle deterministically from the local date. Shared progress is stored in a Home Assistant `input_text` helper as compact JSON, allowing multiple dashboards to participate in the same puzzle.

## Planned configuration

```yaml
type: custom:daily-puzzle-card
state_entity: input_text.daily_puzzle_state
hide_after: 600
title: Daily Puzzle
```

## Development

Initial development is happening on the `dev` branch. Installation instructions will be added once the first playable build is ready.

## Disclaimer

This is an independent Home Assistant community project. It is not affiliated with or endorsed by The New York Times, Wordle, Connections, or Nabu Casa. Game mechanics may be inspired by familiar word-puzzle formats, but puzzle content and presentation are original to this project.
