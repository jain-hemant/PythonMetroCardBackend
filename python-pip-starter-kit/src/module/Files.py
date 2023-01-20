def getInput(path):
    # creating an Array to store BALANCE
    balance = []
    # creating an Array to store CHECK_IN
    check_in = [] 
    if len(path) != 2:
        raise Exception("File path not entered")
    file_path = path[1]       
    # Open file stream via file path in read mode
    f = open(file_path, 'r')        
    # Read line from file
    for Line in f.readlines():
        Lines = Line.strip()
        print()
        # Slicing Line till Length of 6 to Extract BALANCE Keyword
        if Lines[:7] == 'BALANCE':
            # balance.append((Lines.replace("\n",'')).split(" ")) 
            temp = Lines[8:]
            balance.append(Lines)  # balance.append(temp.replace("\n",''))
        # Slicing Line till Length of CHECK_IN to Extract CHECK_IN Keyword
        elif Lines[:8] == 'CHECK_IN':
            temp = Lines[9:]
            check_in.append(temp.replace("\n",''))
        else:
            pass 
    # print(self.balance , self.check_in) 
    return balance 


