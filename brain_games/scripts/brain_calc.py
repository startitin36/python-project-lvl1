#!/usr/bin/env python3


from brain_games.games.calc import calc, INTRO
import brain_games.scripts.engine


def main():
    brain_games.scripts.engine.main(INTRO, calc)


if __name__ == '__main__':
    main()
