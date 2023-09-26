def userSelection(list, n):

    for i in range(0, n):
        selection = input("Enter in a number: ")

        if(selection.isdigit()):
            list.append(int(selection))
            
        else:
            print("Try again")

            while(not selection.isdigit()):
                selection = input("Enter in a number: ")
            
            list.append(int(selection))

    return list
