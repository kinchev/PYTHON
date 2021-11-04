destination=input()

while destination!='End':
    target_money=float(input())
    current_money=0
    while current_money<target_money:
        input_money=float(input())
        current_money+=input_money
    print(f'Going to {destination}!')
    destination=input()