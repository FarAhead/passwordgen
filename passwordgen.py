from random import randint

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = []
nums = []
specialChars = ['-', '$', '&', '#']

def main():
    init()
    
    amountOfChars = int(input("Amount of letters chars: "))
    optionOfSpecialChars = input("Would you like special charcaters [y/n]: ")
    
    print(generatePassword(amountOfChars, optionOfSpecialChars))

    
def generatePassword(length = None, yes_or_no = None) -> str:  #yes or no
    # type checking
    given = False
    
    if yes_or_no.lower() == "y" or yes_or_no.lower() == "yes":
        given = True
    
    if length == None:
        return "ERR: Password can't be generated because length wasn't provided."
    
    if type(length) != int:
       return "ERR: Password can't be generated because non-integer value was given." 
    
    # START
    
    password = str() # defining a string
    
    for l in range(length):
        rng = randint(0,8)
        
        if rng == range(1,5): #num
            password += str(chooseOutOfArray(nums))
        
        elif rng == 1 and given == True:
            password += str(chooseOutOfArray(specialChars))
        
        else: #string
            if randint(0,1) == 0: #lower
                password += chooseOutOfArray(lower)
            else: # upper
                password += chooseOutOfArray(upper)
        
        chooseOutOfArray(upper)
        
    return password
        

def init(): # adds all of the values to the lists
    for x in range(len(lower)):
        upper.append(lower[x].upper())  
    for l in range(10):
        nums.append(l)

def chooseOutOfArray(arr: list): 
    randomnum = randint(0, len(arr)-1)
    return arr[randomnum]

if __name__ == '__main__':
    main()