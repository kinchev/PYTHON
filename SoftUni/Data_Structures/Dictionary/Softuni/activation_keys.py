key = input()

command = input()

while not command == 'Generate':
    command = command.split(">>>")
    what_to_do = command[0]
    if what_to_do == 'Slice':
        startI = int(command[1])
        endI = int(command[2])
        key_start = key[:startI]
        key_end = key[endI:]
        key = key_start + key_end
        print(key)

    elif what_to_do == 'Flip':
        case = command[1]
        startI = int(command[2])
        endI = int(command[3])
        key = list(key)
        if case == "Upper":
            key[startI:endI] = [x.upper() for x in key[startI:endI]]
            key = "".join(key)
            print(key)
        else:
            key[startI:endI] = [x.lower() for x in key[startI:endI]]
            key = "".join(key)
            print(key)
    elif what_to_do == 'Contains':
        sub = command[1]
        if sub in key:
            print(f'{key} contains {sub}')
        else:
            print('Substring not found!')

    command = input()
print(f'Your activation key is: {key}')
# abcdefghijklmnopqrstuvwxz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate

# 134softsf5ftuni2020rockz42
# Slice>>>3>>>7
# Contains>>>-rock
# Contains>>>-uni-
# Contains>>>-rocks
# Flip>>>Upper>>>2>>>8
# Flip>>>Lower>>>5>>>11
# Generate