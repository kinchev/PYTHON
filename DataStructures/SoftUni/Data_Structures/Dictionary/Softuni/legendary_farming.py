def collect_material(key_material_dict: dict, junk_material_dict: dict, material: str, qty: int):
    if material == 'shards' or material == 'fragments' or material == 'motes':
        key_material_dict[material]+=qty
    else:
        if material not in junk_material.keys():
            junk_materials[material]=qty
        else:
            junk_materials[material]+=qty


key_material = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
obtain = ''

while obtain == '':
    input = input().split()
    for i in range(0, len(input), 2):
        m_qty = int(input[i])
        m_name = (input[i + 1]).lower()

# 3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards
# 123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver
