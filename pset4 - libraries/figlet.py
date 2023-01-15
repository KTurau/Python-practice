# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the
# two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit
# via sys.exit with an error message.


import sys
import pyfiglet
import random


f_list = pyfiglet.FigletFont.getFonts()
rand_f = random.choice(f_list)


if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    if sys.argv[2] not in f_list:
        sys.exit("Invalid usage")
    x = input("Input: ")
    f = pyfiglet.Figlet(font=sys.argv[2])
    print(f.renderText(x))
elif len(sys.argv) == 1:
    x = input("Input: ")
    # f_list = pyfiglet.FigletFont.getFonts()
    # rand_f = random.choice(f_list)
    f = pyfiglet.Figlet(font=rand_f)
    print(f.renderText(x))
else:
    sys.exit("Invalid usage")
