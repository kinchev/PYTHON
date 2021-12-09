# Write program that:
# Reads an input string
# Reverses it using a stack.
# Print the result back on the console

input_ = list(input())
stack = []

for i in range(len(input_)):
    stack.append(input_.pop())
print("".join(stack))
