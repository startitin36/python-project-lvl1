import prompt
from brain_games.scripts.cli import welcome_user


WRONG_MSG = "'{}' is wrong answer :(. Correct answer was '{}'."
TRY_MSG = "Let's try again, {}!"
WIN_MSG = 'Congratulations, {}!'
TRIES = 3
CORRECT = 'Correct!'
ANS_REQ = 'Your answer: '
GREETING_MSG = 'Welcome to the Brain Games!'


def engine(game, name):
    cor_ans = 0
    while cor_ans < TRIES:
        (quest_str, result) = game()
        print(quest_str)
        ans = prompt.string(ANS_REQ)
        if ans == result:
            print(CORRECT)
            cor_ans += 1
            if cor_ans == TRIES:
                print(WIN_MSG.format(name))
        else:
            print(WRONG_MSG.format(ans, result))
            print(TRY_MSG.format(name))
            break


def main(INTRO, game):
    print(GREETING_MSG)
    print(INTRO, '\n')
    name = welcome_user()
    engine(game, name)


if __name__ == '__main__':
    main()
