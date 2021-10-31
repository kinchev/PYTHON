n = int(input())
word = input()
strings_list = []
word_list = []
for i in range(n):
    strings = input()
    strings_list.append(strings)
    if word in strings:
        word_list.append(strings)

print(strings_list)
print(word_list)
