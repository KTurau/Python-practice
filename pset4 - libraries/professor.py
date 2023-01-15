# In a file called professor.py, implement a program that:

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits.
# No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt
# the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should
# output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
# and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:


from random import randint


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for i in range(3):
            err = i
            try:
                print(f"{x} + {y} = ", end="")
                answer = int(input())
                if answer != (x + y):
                    print("EEE")
                    continue
                break
            except ValueError:
                print("EEE")

        if err == 0:
            score = score + 1
        elif err == 2:
            print(f"{x} + {y} = {x + y}")

    print("Score:", score)


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level not in [1, 2, 3]:
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    match level:
        case 1:
            return randint(0, 9)
        case 2:
            return randint(10, 99)
        case 3:
            return randint(100, 999)


if __name__ == "__main__":
    main()
