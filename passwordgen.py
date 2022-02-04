from random import randint

lower = "abcdefghijklmnopqrstuvwxyz"
upper = str()
nums = []
specialChars = "-$&#"

def main():
    init()
    
    amountOfChars = int(input("Amount of letters chars: "))
    optionOfSpecialChars = input("Would you like special charcaters [y/n]: ")
    
    print(generatePassword(amountOfChars, optionOfSpecialChars))

    
def generatePassword(length = None, specialChars = None) -> str:
    # type checking
    given = False
    
    if specialChars.lower() == "y" or specialChars.lower() == "yes":
        given = True
    
    if length == None:
        return "ERR: Password can't be generated because length wasn't provided."
    
    if type(length) != int:
       return "ERR: Password can't be generated because non-integer value was given." 
    
    # START
    
    password = str() # defining a string
    
    for l in range(length):
        rng = randint(0,8)
        
        if rng == 1 or rng == 2: #num
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
    global upper
    for x in lower:
        upper += x.upper()
    for l in range(10):
        nums.append(l)

def chooseOutOfArray(arr: list): 
    randomnum = randint(0, len(arr)-1)
    return arr[randomnum]

if __name__ == '__main__':
    main()
