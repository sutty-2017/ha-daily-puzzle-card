"""Local, frozen Word Links content and deterministic selection."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .puzzles import holiday_for_date

_CONTENT = json.loads(Path(__file__).with_name('word_links.json').read_text())
LINK_BOARDS = tuple(tuple(words) for words in _CONTENT['boards'])
HOLIDAY_LINKS = _CONTENT['holidays']
_BOARD_ORDER = tuple(sorted(range(len(LINK_BOARDS)), key=lambda i: hashlib.sha256(f'word-links-v1:{i}'.encode()).digest()))


def links_for_date(day):
    holiday = holiday_for_date(day)
    if holiday in HOLIDAY_LINKS:
        board = HOLIDAY_LINKS[holiday]
        return {'id': 'holiday-' + holiday, 'theme': board['theme'], 'words': list(board['words'])}
    # A stable shuffled calendar cycle visits every board before repeating.
    index = _BOARD_ORDER[day.toordinal() % len(_BOARD_ORDER)]
    return {'id': f'links-{index + 1:03}', 'theme': '', 'words': list(LINK_BOARDS[index])}
