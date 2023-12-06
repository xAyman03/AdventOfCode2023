document = []
digits = {"one": "1",
          "two": "2",
          "three": "3",
          "four": "4",
          "five": "5",
          "six": "6",
          "seven": "7",
          "eight": "8",
          "nine": "9"}

with open('t (Part2).txt') as f:
    document = f.readlines()

sum = 0

def find_first_digit(t):
    word = ""
    for char in t:
        if char.isdigit():
            return char
        else:
            word += char
            for digit in digits:
                if digit in word:
                    return digits[digit]

def find_last_digit(t):
    word = ""
    for char in reversed(t):
        if char.isdigit():
            return char
        else:
            word += char
            for digit in digits:
                if digit in word[::-1]:
                    return digits[digit]        

for t in document:
    firstNum = find_first_digit(t)
    lastNum = find_last_digit(t)    
                
    sum = sum + int(firstNum + lastNum)
    
print(sum)