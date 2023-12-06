document = []
with open('t.txt') as f:
    document = f.readlines()

sum = 0

for t in document:
    num1 = 0
    num2 = 0
    for i in range(len(t)):
        if t[i].isdigit():
            num1 = t[i]
            break
    for i in range(len(t) - 1, 0, -1):
        if t[i].isdigit():
            num2 = t[i]
            break
        else:
            num2 = num1    
                
    sum = sum + int(num1 + num2)
    
print(sum)
