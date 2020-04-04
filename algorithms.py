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

#PentagonalNumber
def PentagonalNumber(n):
    a = 1
    for i in range(1, n):
        a += 5 * i
    return a

#Kaprekars
def KaprekarsConstant(n):
    count = 0
    while n != 6174:
        n = list(str(n))
        if len(n) < 4:
            while len(n) != 4:
                n.insert(1, '0')
        count += 1
        x, y = int(''.join([str(l) for l in (sorted(n))])[::-1]), int(''.join([str(l) for l in (sorted(n))]))
        n = x - y
    return count

# Scale Balancing
import itertools
def ScaleBalancing(a):
    x = list(int(l) for l in a[0][1:-1].split(','))
    y = list(int(l) for l in a[1][1:-1].split(','))
    for a in y:
        if x[0] + a == x[1] or x[1] + a == x[0]:
            return str(a)
    for pair in itertools.combinations(y, 2):
        if pair[0] + x[0] == x[1] + pair[1] or pair[0] + x[1] == pair[1] + x[0] or pair[0] + pair[1] + x[0] == x[1] or pair[0] + pair[1] + x[1] == x[0]:
            l, i = min(pair), max(pair)
            return ','.join([str(l), str(i)])
    return 'not possible'

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))



# bubble sort Javascript:
function BubbleSort(nums) {
  for (var i = 0; i < nums.length; i++) {
    for (var j = 0; j < nums.length; j++) {
      if (nums[j] > nums[j+1]) {
        var tempNum = nums[j]
        nums[j] = nums[j+1]
        nums[j+1] = tempNum
      }
    }
  }
}

# Selection sort Javascript: 
function SelectionSort(nums) {
  var minIdx;
  var tempNum;
 
  for (var i = 0; i < nums.length; i++) {
    let minIdx = i
    for (var j = i+1; j < nums.length; j++) {
      if (nums[j] < nums[minIdx]) {
        minIdx = j;
      }
    }
    tempNum = nums[i]
    nums[i] = nums[minIdx]
    nums[minIdx] = tempNum
  }
  return nums
}

# Insertion Sort in JS:
function insertion_Sort(arr)
{
  for (var i = 1; i < arr.length; i++) 
  {
    if (arr[i] < arr[0]) 
    {
      //move current element to the first position
      arr.unshift(arr.splice(i,1)[0]);
    } 
    else if (arr[i] > arr[i-1]) 
    {
      //leave current element where it is
      continue;
    } 
    else {
      //find where element should go
      for (var j = 1; j < i; j++) {
        if (arr[i] > arr[j-1] && arr[i] < arr[j]) 
        {
          //move element
          arr.splice(j,0,arr.splice(i,1)[0]);
        }
      }
    }
  }
  return arr;
}


// function reverseString(str) {
//   if (str === "") // This is the terminal case that will end the recursion
//     return "";
  
//   else
//     return reverseString(str.substr(1)) + str.charAt(0);
/* 
First Part of the recursion method
You need to remember that you won’t have just one call, you’ll have several nested calls

Each call: str === "?"        	                  reverseString(str.subst(1))     + str.charAt(0)
1st call – reverseString("Hello")   will return   reverseString("ello")           + "h"
2nd call – reverseString("ello")    will return   reverseString("llo")            + "e"
3rd call – reverseString("llo")     will return   reverseString("lo")             + "l"
4th call – reverseString("lo")      will return   reverseString("o")              + "l"
5th call – reverseString("o")       will return   reverseString("")               + "o"

Second part of the recursion method
The method hits the if condition and the most highly nested call returns immediately

5th call will return reverseString("") + "o" = "o"
4th call will return reverseString("o") + "l" = "o" + "l"
3rd call will return reverseString("lo") + "l" = "o" + "l" + "l"
2nd call will return reverserString("llo") + "e" = "o" + "l" + "l" + "e"
1st call will return reverserString("ello") + "h" = "o" + "l" + "l" + "e" + "h" 
*/
// }
// console.log(reverseString("hello"));



function PalindromeCheck(myString) {
  reversedString = ""
  for (var i = myString.length - 1; i >= 0; i--) {
    console.log(myString[i])
    reversedString += myString[i]
  }

  if (reversedString == myString) {
    return "Hey that's a bingo"
  } else {
    return "Uh oh ah geez"
  }
}

function Factorial(number) {
  factorial = 1
  factorialTotal = 1;
  for (var i = 1; factorial <= number; factorial += 1) {
    factorialTotal = factorialTotal * factorial
  }
  return factorialTotal;
}

function PrimeNumCheck(number) {
  for (var i = 2; i < number; i++) {
    if (number%i==0) {
      return "That ain't no prime"
    } 
  }

  return "That's a prime!"
}


function Factorial(number) {

  if (number == 0) {
    return 1
  }

  return number * Factorial(number - 1)
}