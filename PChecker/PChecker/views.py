from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def checker(request):
    pd = str(request.POST["password"])


    # Check Uppercase

    def checkUpper(pd):
        upper = 0
        upperList = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
        for chr in pd:
            if chr in upperList:
                upper += 1
        if upper > 0:
            return True
        else:
            return False


    # Check Lowercase

    def checkLower(pd):
        lower = 0
        lowerList = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
        for chr in pd:
            if chr in lowerList:
                lower += 1
        if lower > 0:
            return True
        else:
            return False


    # Check Special Characters

    def checkSpecial(pd):
        special = 0
        specialList = " ! @ $ % ^ & # * ( ) _ - + = { } [ ] | \ , . > < / ? ~ ` \" ' : ; ".split()
        for chr in pd:
            if chr in specialList:
                special += 1
        if special > 0:
            return True
        else:
            return False


    # Check FIrst Digit

    def checkFirst(pd):
        if pd[0].isnumeric():
            return True
        else:
            return False


    # Check Length

    def checkLength(pd):
        if (len(pd)>8):
            return True
        else:
            return False

    if pd == '':
        result = 'Enter the password!'

    elif checkLength(pd) == False:
        result = "Youre password should have atleast 8 digits!"
    
    elif checkFirst(pd) == True:
        result = "Youre password's First digit can't be a number!"

    elif checkUpper(pd) == False:
        result = "Youre password should have contain atleast One Uppercase Character!"

    elif checkLower(pd) == False:
        result = "Youre password should have contain atleast One Lowercase Character!"

    elif checkSpecial(pd) == False:
        result = "Youre password should have contain atleast One Special Character!"

    else:
        result = "Valid Password!!!"

    return render(request, 'checker.html', {'Result':result})


