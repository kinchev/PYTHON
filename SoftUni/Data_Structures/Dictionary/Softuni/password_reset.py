text = input()

command = input()

while not command == 'Done':
    command = command.split()
    what = command[0]
    if what == 'TakeOdd':
        text = ''.join(text[1::2])
        print(text)
    elif what == 'Cut':
        index = int(command[1])
        length = int(command[2])
        cut_start = text[index:index + length]
        text = text.replace(cut_start, "")
        print(text)
    elif what == 'Substitute':
        sub = command[1]
        new_sub = command[2]
        if sub not in text:
            print("Nothing to replace!")
        elif sub in text:
            text = text.replace(sub, new_sub)
            print(text)

    command = input()

print(f'Your password is: {text}')

# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done
