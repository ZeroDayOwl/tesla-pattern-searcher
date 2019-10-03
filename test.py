def addDigits(num):
    s = 0
    digits = int(num)
    while digits:
        s += digits % 10
        digits //= 10
    return s


def checkYear():
    interestings = {}
    interestings["checks"] = []
    inputYear = int(input("What is the year?: "))
    
    def base10toN(num, base):
        """Change ``num'' to given base
        Upto base 36 is supported."""

        converted_string, modstring = "", ""
        currentnum = num
        if not 1 < base < 37:
            raise ValueError("base must be between 2 and 36")
        if not num:
            return '0'
        while currentnum:
            mod = currentnum % base
            currentnum = currentnum // base
            converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
        return converted_string
        
    def checkInteresting(base, s):
        if(addDigits(s) % 3 == 0):
            data = {'base' : base, 'additionOfDigits': s }
            interestings["checks"].append(data)


    bases = [2,3,6,9]
    number = inputYear
    
    print("Testing " + str(number) + " against several bases:")
    total = addDigits(int(number))
    checkInteresting(10, total)

    for n in bases:
        result = base10toN(number, n)
        print("Base " + str(n) + ": " + str(result))
        print("Added digits: " + str(addDigits(result)) + "\n")
        checkInteresting(n, addDigits(result))
    if(len(interestings) >= 1):
        print("\n \n Found interesting Output for " + str(number))
        print(interestings)
    else:
        print("\n \n No interesting Results found :(")


"""

CHECK NAME

"""


def checkName():
    interestings = {}
    interestings["checks"] = []
    def base10toN(num, base):
        """Change ``num'' to given base
        Upto base 36 is supported."""

        converted_string, modstring = "", ""
        currentnum = num
        if not 1 < base < 37:
            raise ValueError("base must be between 2 and 36")
        if not num:
            return '0'
        while currentnum:
            mod = currentnum % base
            currentnum = currentnum // base
            converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
        return converted_string

    def checkInteresting(number):
        if(length % 3 == 0):
            check = {'length' : length}
            interestings["checks"].append(check)
        bases = [2,3,6,9]
        for n in bases:
            result = base10toN(number, n)
            print("Base " + str(n) + ": " + str(result))
            print("Added digits: " + str(addDigits(result)) + "\n")
            if(addDigits(result) % 3 == 0):
                check = {'base' : n, 'addedDigits': addDigits(result)}
                interestings["checks"].append(check)

    givenName = input('What is the name/string?: ')
    name = givenName.replace(' ', '').lower()
    length = len(name)
    checkInteresting(length)

    

    if(len(interestings) >= 1):
        print("\n \n Found interesting Output for " + givenName)
        print(interestings)
    else:
        print("\n \n No interesting Results found :(")


ques1 = int(input
('''What is it you are searching for?
    (1) Name
    (2) Year
    (3) Any number
'''))

if(ques1 == 1):
    checkName()
if(ques1 == 2):
    checkYear()
if(ques1 == 3):
    print("Under consturction")
