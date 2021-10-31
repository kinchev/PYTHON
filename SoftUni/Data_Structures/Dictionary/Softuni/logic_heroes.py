n = int(input())
heroes = {}
for _ in range(n):
    name, HP, MP = input().split()
    heroes[name] = [int(HP), int(MP)]

command = input()

while not command == 'End':
    command = command.split(" - ")
    what = command[0]
    if what == 'Heal':
        name = command[1]
        amount = int(command[2])
        if heroes[name][0] + amount > 100:
            current = 100 - heroes[name][0]
            heroes[name][0] = 100
            print(f"{name} healed for {current} HP!")
        else:
            heroes[name][0] += amount
            print(f"{name} healed for {amount} HP!")
    elif what == 'Recharge':
        name = command[1]
        amount = int(command[2])
        if heroes[name][1] + amount > 200:
            heroes[name][1] = 200
            print(f"{name} recharged for {amount} MP!")
        else:
            heroes[name][1] += amount
            print(f"{name} recharged for {amount} MP!")

    elif what == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker = command[3]

        if heroes[name][0] - damage > 0:
            heroes[name][0] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")

        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]

    elif what == 'CastSpell':
        name = command[1]
        need = int(command[2])
        spell = command[3]
        if need < heroes[name][1]:
            heroes[name][1] -= need
            print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")
    command = input()
sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0],-x[1][1],x[0])))

for k, v in sorted_heroes.items():
    print(f'{k}')
    print(f'  HP: {v[0]}')
    print(f'  MP: {v[1]}')
# [print(f'{k}\nHP: {v[0]}\nMP: {v[1]}') for (k, v) in heroes.items()]

# 2
# Solmyr 85 120
# Kyrre 99 50
# Heal - Solmyr - 10
# Recharge - Solmyr - 50
# TakeDamage - Kyrre - 66 - Orc
# CastSpell - Kyrre - 15 - ViewEarth
# End
