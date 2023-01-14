# Implement a program in Python that prompts the user for mass as an integer (in kilograms) and 
# then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.



def main():
    m = int(input("m: "))
    c = 300000000 ** 2
    E = m * c
    print("E:", E)

main()

