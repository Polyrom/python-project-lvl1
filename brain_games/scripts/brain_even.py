from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, " + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def is_even(number):
        if number % 2 == 0:
            return 'yes'
        else:
            return 'no'

    def run_brain_even():
        i = 0
        while i < 3:
            number = randint(1, 99)
            print(f'Question: {number}')
            answer = input("Your answer: ")
            if answer.lower() == is_even(number):
                print("Correct!")
                i += 1
            else:
                return print(
                    f'"{answer}" is wrong answer ;(. '
                    f'The correct answer was "{is_even(number)}".'
                    f'\nLet\'s try again, {name}!')
        print("Congratulations, " + name + "!")

    run_brain_even()


if __name__ == "__main__":
    main()
