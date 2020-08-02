#!/usr/bin/env python3


import brain_games.scripts.engine
from brain_games.games.even import even, INTRO


def main():
    brain_games.scripts.engine.main(INTRO, even)


if __name__ == '__main__':
    main()
