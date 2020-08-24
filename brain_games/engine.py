import prompt


WRONG_ANSWER = "'{}' is wrong answer :(. Correct answer was '{}'."
SUGGESTION_TO_TRY = "Let's try again, {}!"
CONGRAT_ON_WINNING = 'Congratulations, {}!'
CORRECT_ANSWERS_TO_WIN = 3
CORRECT_ANSWER = 'Correct!'
ANSWER_REQUIRING = 'Your answer: '
WELCOME = 'Welcome to the Brain Games!'


def engine(game):
    print(WELCOME)
    print(game.INTRO, '\n')
    name = welcome_user()
    cor_ans = 0
    while cor_ans < CORRECT_ANSWERS_TO_WIN:
        (question, result) = game.get_game_data()
        print(question)
        ans = prompt.string(ANSWER_REQUIRING)
        if ans != result:
            print(WRONG_ANSWER.format(ans, result))
            print(SUGGESTION_TO_TRY.format(name))
            break
        print(CORRECT_ANSWER)
        cor_ans += 1
    if cor_ans == CORRECT_ANSWERS_TO_WIN:
        print(CONGRAT_ON_WINNING.format(name))


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name


def main(game):
    engine(game)


if __name__ == '__main__':
    main()
