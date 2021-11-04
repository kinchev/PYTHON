import sys

max_goals = -sys.maxsize

name_player = input()
goals = int(input())
command = input()
current_goals = 0
while command != 'END':

    if current_goals > max_goals:
        max_goals = goals
        name_player = input()
        if goals >= 3:
