input_text = input()

result_dict = {}

for char in input_text:
    if char != " ":
        result_dict[char] = input_text.count(char)

[print(f'{key} -> {value}') for (key, value) in result_dict.items()]



