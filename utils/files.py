
from pathlib import Path


def _data_dir() -> Path:
    return Path(__file__).resolve().parents[1] / 'input_files'


def test_file(day: int) -> list[str]:
    path = _data_dir() / f'tst{day}.txt'
    with open(path, 'r', encoding='utf-8') as fh:
        return list(map(list, (fh.read().splitlines())))


def day_file(day: int) -> list[str]:
    path = _data_dir() / f'{day}.txt'
    with open(path, 'r', encoding='utf-8') as fh:
        return list(map(list, (fh.read().splitlines())))

def str_test(day: int) -> list[str]:
    path = _data_dir() / f'tst{day}.txt'
    with open(path, 'r', encoding='utf-8') as fh:
        return fh.read()

def str_day(day: int) -> list[str]:
    path = _data_dir() / f'{day}.txt'
    with open(path, 'r', encoding='utf-8') as fh:
        return fh.read()

