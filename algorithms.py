def LetterCapitalize(str): 

  # split the string into a list
  words = str.split(" ")

  # we split the word into two parts and then combine the parts 
  # the first part is the first letter which we capitalize and the 
  # second part is the rest of the string
  for i in range(0, len(words)): 
    words[i] = words[i][0].upper() + words[i][1:]

  # return the list of words joined into a string
  return " ".join(words)

def LetterChanges(str): 
    newString = ''
    for char in str:
        if char.isalpha(): 
            if char.lower() == 'z':
                char = 'a'
            else: 
                char = chr(ord(char) +1)
        if char in 'aeiou':
            char = char.upper()
        newString = newString + char
    return newString
print LetterChanges(raw_input())  


def FirstFactorial(num): 
    factorial = 1
    if num == 0:
        return 1
    else:
        for i in range(1,num + 1):
            factorial = factorial * i
    # code goes here 
    return factorial
    
# keep this function call here  
print FirstFactorial(raw_input())  



# PALINDROME:
def PalindromeCheck(word):
    reversedString = ""
    for i in range(1, len(word) + 1):
        reversedString += word[-i]
    
    if reversedString == word:
        print("Palindrome!")
    else: 
        print("Not a palindrome")


# FIZZBUZZZ
def FizzBuzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % == 0:
            print("FIZZBUZZ BABY")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(i)
        
# MINUTES INTO HOURS:MINUTES
def MinsToHrsMins(minutes):
    hours = int(math.floor(num/60))
    minutes = num % 60
    return (str(hours) + ':' + str(minutes))

# FACTORIALS
def Factorial(number):
    factorial = 1
    if number == 0:
        return 1
    else:
        for i in range(1, number + 1):
            factorial = factorial * i

    return factorial


#Reverse STRING
def ReverseEasy(string):
    return str[::-1]

def ReverseHard(string):
    reversedString = ''
    for i in range(1, len(string) + 1):
        reversedString += string[-i]
    
    return reversedString

# Add all numbers from 1 to num
def AddEmUp(number):
    for i in range(1, number)
        number = number + i
    return number

# Do letters have a + on either side? 
def CheckCrosses(string):
    for i in range(0, len(string)):
        if str[i].isalpha:
            if str[i-1] != '+' and str[i+1] != '+':
                return "False"

    return "True"
            
# Longest word
def LongestWord(string):
    wordlist = string.split()
    biggestWord = ''
    for i in wordlist:
        if len(i) > len(biggestWord):
            biggestWord = i
    
    return biggestWord

# Shift every letter in the alphabet, then capitalize the vowels:
def Shift(string):
    newString = ""
    for char in string:
        if char.isalpha:
            if char is "z":
                char = "a"
            else:
                char = chr(ord(char) +1)
        if char in 'aeiou':
            char = char.upper()
        newString = newString + char

    return newString

# CAPITALIZE WORDS
def CapitalizeWords(string):
    # newList = string.split()
    # for word in newList:
    #     word[0] = word[0].upper()

    # return " ".join(newList)

    words = string.split()
    for i in range(0, len(words)):
        words[i] = words[i][0].upper() + words[i][1:]
    return " ".join(words)


#Calculate TIp, assuming 15%
def CalculateTip(bill):
    tip = bill * 0.15
    return tip

#Prime numbers
def IsPrime(num):
    # If given number is greater than 1 
    if num > 1: 
        
    # Iterate from 2 to n / 2  
    for i in range(2, num//2): 
            
        # If num is divisible by any number between  
        # 2 and n / 2, it is not prime  
        if (num % i) == 0: 
            print(num, " is not a prime number") 
            break
    else: 
        print(num, " is a prime number") 
    
    else: 
    print(num, " is not a prime number.") 

correct_list = [1, 2, 3, 4, 5]
new_list = [1, 3, 4, 5]
def MissingElement():
  for element in correct_list:
    if element not in new_list:
      print("Missing " + str(element) + "!")

MissingElement()

word_list = ["Me","Bike","Minnesota","Apple"]

def determine_longest(list):
    longestword = max(list, key=len)
    return longestword

print(determine_longest(word_list))

#Find the biggest number
numbers = [15,10,100,1]

def biggest_number(list):
    bignumber = max(list)
    return bignumber

print(biggest_number(numbers))


my_array = [1, 2, 3, 4, 5]
def duplicate_array(first_array)
    duplicate = first_array
    new_array = first_array + duplicate
    return new_array


def largestHardWay(list):
    length = len(list)
    biggest = list[0]
    for i in range(1, length):
        if list[i] > biggest:
            biggest = list[i]
    return biggest


def primecheck():
    number = int(input("Please enter a number: "))
    text = ""
    if number == 2 or number == 1:
        text = "Prime number."

    for index in range(number-1,1,-1):
        if number % index == 0:
            text = "This is not a prime number."
            break
        else: 
            text = "This is a prime number."

    return text

print(primecheck())

def BubbleSort(numlist):
    for num in range(len(numlist)-1, 0, -1):
        for i in range(num):
            if list[i] > list[i+1]:
                tempnum = list[i]               
                list[i] = list[i+1]
                list[i+1] = tempnum

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1