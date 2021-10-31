sublist_list = input().split("|")
result = []
for i in range(len(sublist_list) - 1, -1, -1):
    elements = sublist_list[i].split()
    result += elements
print(" ".join(result))
