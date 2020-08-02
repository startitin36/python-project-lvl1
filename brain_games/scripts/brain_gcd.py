#!/usr/bin/env python3


import brain_games.scripts.engine
from brain_games.games.gcd import gcd_game, INTRO


def main():
    brain_games.scripts.engine.main(INTRO, gcd_game)


if __name__ == '__main__':
    main()
