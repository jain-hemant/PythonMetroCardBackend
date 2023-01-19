from sys import argv
from src.module.file import getInput
# Creating Function to get input from file


def main():    
    input = getInput(argv)
    # print(input[0])
    print(input[1])

#  execution of main function  
if __name__ == "__main__":
    main()
    x = input()

