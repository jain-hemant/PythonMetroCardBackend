from sys import argv
from src.module.Files import getInput
from src.module.Metrocard import Metrocard
# Creating Function to get input from file


def main():
    input = getInput(argv)
    mc_card = Metrocard()
    mc_card.balance_info(input)
    # mc_card.balance_info(input[1])

    # input = objFile.getInput(argv)
    # print(input)
    
    # print(input[0])
    # print(input[0])
    # bal = Metrocard()
    # bal.balance_info(input)
    # print(bal)
   
#  execution of main function  
if __name__ == "__main__":
    main()
    x = input()

