target_steps = 10000
total_step = 0
going_home = False
while total_step < target_steps:
    command = input()
    if command == 'Going home':
        going_home = True
        break
    current_step = int(command)
    total_step += current_step
