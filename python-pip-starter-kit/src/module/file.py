def getInput(path):
    if len(path) != 2:
        raise Exception("File path not entered")
    file_path = path[1]
    # Open file stream via file path in read mode
    f = open(file_path, 'r')
    # creating an Array to store BALANCE
    balance = []
    # creating an Array to store CHECK_IN
    check_in = []
    # Read line from file
    for Line in f.readlines():
        Lines = Line.strip()
        # Slicing Line till Length of 6 to Extract BALANCE Keyword
        if Lines[:7] == 'BALANCE':
            # balance.append((Lines.replace("\n",'')).split(" ")) 
            balance.append((Lines[8:].replace("\n",'')).split(" ")) 
        # Slicing Line till Length of CHECK_IN to Extract CHECK_IN Keyword
        elif Lines[:8] == 'CHECK_IN':
            check_in.append((Lines[9:].replace("\n",'')).split(' '))
        else:
            pass  
    return [balance, check_in]  
    