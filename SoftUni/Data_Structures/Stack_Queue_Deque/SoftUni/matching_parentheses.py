# You are given an algebraic expression with parentheses.
# Scan through the string and extract each set of parentheses.
# Print the result back on the console.

# Input:                                     Output:
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5        (2 + 3)
#                                            (3 + 1)
#                                            (2 - (2 + 3) * 4 / (3 + 1))

input_=input()
parentheses=[]
for i in range(len(input_)):
    if input_[i]=="(":
        parentheses.append(i)
    elif input_[i]==")":
        start_index=parentheses.pop()
        print(input_[start_index:i+1])

