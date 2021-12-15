from collections import deque

elf_power = [int(x) for x in input().split()]
materials = [int(x) for x in input().split()]
elf_power = deque(elf_power)
materials = deque(materials)

times = 0
toys = 0
energy = 0
while materials:
    times += 1
    if len(elf_power) == 0:
        break

    elf = elf_power.popleft()
    material = materials.pop()
    if times % 3 == 0:
        if elf <= 5 and len(elf_power)>0:
            elf_power.popleft()
        else:
            increase_material = material * 2
            if increase_material <= elf:
                toys += 2
                elf -= increase_material
                energy += increase_material
                elf += 1
                elf_power.append(elf)
            else:
                elf *= 2

                elf_power.append(elf)
                materials.append(material)
    elif times % 5 == 0:
        if elf <= 5:
            elf_power.popleft()
        elif elf >= material:
            energy += material
            elf -= material
            elf_power.append(elf)

        else:

            energy += material
            elf_power.append(elf)
    else:
        if elf < 5 and len(elf_power)>0:
            elf_power.popleft()
        elif elf >= material:
            toys += elf//material
            energy += material
            elf -= material
            elf += 1
            elf_power.append(elf)
        else:
            elf *= 2
            elf_power.append(elf)
            materials.append(material)

print(f"Toys: {toys}")
print(f"Energy: {energy}")
# left_elf = list(elf_power)
if len(elf_power) == 0:

    print(f"Boxes left:", ', '.join(str(x) for x in materials))
else:
    print(f"Elves left:", ', '.join(str(x) for x in elf_power))