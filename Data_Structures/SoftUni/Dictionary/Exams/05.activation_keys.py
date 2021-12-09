activation_key = input()
command = input()

while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        first_part = activation_key[:start_index]
        second_part = activation_key[start_index:end_index]
        third_part = activation_key[end_index:]
        if command[1] == "Upper":
            second_part = second_part.upper()
        else:
            second_part = second_part.lower()
        activation_key = first_part + second_part + third_part
        print(activation_key)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")