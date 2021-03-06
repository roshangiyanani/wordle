from pathlib import Path
from typing import Sequence

from termcolor import colored

from wordle.wordle import CharResult


def load_words(path: Path) -> Sequence[str]:
    words = path.read_text().splitlines()
    for i in range(len(words)):
        words[i] = words[i].casefold()

    words.sort()
    return words


def colored_text(word: str, results: Sequence[CharResult]) -> str:
    s = ""
    for char, result in zip(word, results, strict=True):
        if result == CharResult.Gray:
            s += char
        elif result == CharResult.Yellow:
            s += colored(char, "yellow")
        elif result == CharResult.Green:
            s += colored(char, "green")
        else:
            raise ValueError(f"unrecognized CharResult '{result}'")

    return s
