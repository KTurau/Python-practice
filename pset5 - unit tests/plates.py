def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Plates contain min 2 max 6 char.
    # Plates start with at least 2 letters
    # No periods, spaces, or punctuation marks
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():

        # Numbers cannot be used in the middle of a plate; they must
        # come at the end. For example, AAA222 would be an acceptable … vanity plate;
        # AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
        for i in s:
            if i in num:
                inx = s.index(i)
                if i != "0" and s[inx:].isdecimal():
                    return True
                else:
                    return False
            else:
                continue

        return True
    else:
        return False


if __name__ == "__main__":
    main()
