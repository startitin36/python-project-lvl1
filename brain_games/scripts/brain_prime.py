#!/usr/bin/env python3


import brain_games.engine
from brain_games.games import isprime


def main():
    brain_games.engine.main(isprime)


if __name__ == '__main__':
    main()
