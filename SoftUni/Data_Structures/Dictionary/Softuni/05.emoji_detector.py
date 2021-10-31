import re

text = input()
pattern = r"([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)"
emojis_found = re.findall(pattern, text)
threshold = 1

for digits in text:
    if digits.isdigit():
        threshold *= int(digits)

print(f"Cool threshold: {threshold}")
if len(emojis_found) > 0:
    print(f"{len(emojis_found)} emojis found in the text. The cool ones are:")
    for emoji in emojis_found:
        points_of_emoji = 0
        for char in emoji[1]:
            points_of_emoji += ord(char)
        if points_of_emoji >= threshold:
            print("".join(emoji))