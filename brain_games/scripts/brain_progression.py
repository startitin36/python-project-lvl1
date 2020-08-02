#!/usr/bin/env python3


import brain_games.scripts.engine
from brain_games.games.progress import INTRO, progress


def main():
    brain_games.scripts.engine.main(INTRO, progress)


if __name__ == '__main__':
    main()
