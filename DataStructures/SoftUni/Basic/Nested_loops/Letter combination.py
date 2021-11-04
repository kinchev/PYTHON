first = input()
second = input()
third = input()
combination = 0
result = ""
for i in range(ord(first),ord(second)+1):
    for k in range(ord(first),ord(second)+1):
        for l in range(ord(first), ord(second)+1):
            if chr(i) != third and chr(k) != third and chr(l) != third:
                combination += 1
                result = result + chr(i)+chr(k)+chr(l)+" "
print(f"{result}{combination}",end="")

