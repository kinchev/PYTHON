result1 = input()
result2 = input()
result3 = input()
count_w = 0
count_d = 0
count_l = 0

d_result1 = result1[0:1]
g_result1 = result1[-1]
if d_result1 > g_result1:
    count_w += 1
elif d_result1 < g_result1:
    count_l += 1
else:
    count_d += 1

d_result2 = result2[0:1]
g_result2 = result2[-1]
if d_result2 > g_result2:
    count_w += 1
elif d_result2 < g_result2:
    count_l += 1
else:
    count_d += 1

d_result3 = result3[0:1]
g_result3 = result3[-1]
if d_result3 > g_result3:
    count_w += 1
elif d_result3 < g_result3:
    count_l += 1
else:
    count_d += 1

print(f'Team won {count_w:.0f} games.\nTeam lost {count_l:.0f} games.\nDrawn games: {count_d:.0f}')