from collections import deque


def is_enough(fireworks):
    # return fireworks['palm'] >= 3 \
    #        and fireworks['willow'] >= 3 \
    #        and fireworks['crossette'] >= 3
    return all(x >= 3 for x in fireworks.values())


def solve(firework_effects, explosive_powers):
    firework_work_queue = deque([x for x in firework_effects if x > 0])
    explosive_power_stack = [x for x in explosive_powers if x > 0]

    fireworks = {
        'palm': 0,
        'willow': 0,
        'crossette': 0,

    }

    while firework_work_queue and explosive_power_stack and not is_enough(fireworks):
        firework_effect_queue = firework_work_queue.popleft()
        explosive_power = explosive_power_stack.pop()

        current_sum = firework_effect_queue + explosive_power
        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks['crossette'] += 1
        elif current_sum % 3 == 0:

            fireworks['palm'] += 1

        elif current_sum % 5 == 0:
            fireworks['willow'] += 1

        else:
            firework_work_queue.append(firework_effect_queue - 1)
            explosive_power_stack.append(explosive_power)

    return fireworks, firework_effect_queue, explosive_power_stack


fe = [5, 6, 4, 16, 11, 5, 30, 2, 3, 27]

ep = [1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22]

fireworks, firework_effects, explosive_powers = solve(fe, ep)


def print_fireworks(fireworks):
    print(
        f'''Palm Fireworks: {fireworks['palm']} \nWillow Fireworks: {fireworks['willow']}\nCrossette Fireworks: {fireworks['crossette']}
    ''')


def print_success(fireworks):
    print('Congrats! You made the perfect firework show!')
    print_fireworks(fireworks)


def print_fail(fireworks, firework_effects, explosive_powers):
    print('Sorry.You can\'t make the perfect firework show.')
    if firework_effects:
        print(f'Firework Effects left: {firework_effects}')
    if explosive_powers:
        print(f'Explosive Power left: {explosive_powers}')
    print_fireworks(fireworks)


fireworks, remaining_firework_effects, remaining_explosive_powers = solve(fe, ep)

if is_enough(fireworks):
    print_success(fireworks)
else:
    print_fail(fireworks, remaining_firework_effects, remaining_explosive_powers)
