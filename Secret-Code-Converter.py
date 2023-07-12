# This program will convert your string in a code language which can be understand after decoding :
import random as R

randlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
choice = input("DO you wanna Incode or Decode : ")
String = input("Enter your chat : ")
String = String.split(" ")
newString = ""

if choice=="Incode" or choice=="incode" :
    for i in range(len(String)):
        codeString = ""
        if len(String[i])>=3:
            n1 = R.choice(randlist) + R.choice(randlist) + R.choice(randlist)
            n2 = R.choice(randlist) + R.choice(randlist) + R.choice(randlist)
            codeString = codeString+n1+String[i][1:]+String[i][0]+n2
        else :
            codeString = codeString + String[i][::-1]
        newString = newString+codeString+" "
    print("New Chat is :")
    print(newString)

elif choice=="Decode" or choice=="decode" :
    for i in range(len(String)):
        if len(String[i])>=3:
            codeString = String[i][3:-3]
            codeString = codeString[-1] + codeString[:-1]
        else :
            codeString = String[i][::-1]
        newString = newString+codeString+" "
    print("New Chat is :")
    print(newString)

else:
    print("Invalid Input ! please check your spellings !")