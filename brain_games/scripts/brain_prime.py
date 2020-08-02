#!/usr/bin/env python3


import brain_games.scripts.engine
from brain_games.games.isprime import isprime, INTRO


def main():
    brain_games.scripts.engine.main(INTRO, isprime)


if __name__ == '__main__':
    main()
