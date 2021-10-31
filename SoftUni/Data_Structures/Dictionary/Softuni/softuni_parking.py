n = int(input())
plates = {}
for i in range(0, n):
    data = input().split()
    command = data[0]
    if command == 'register':
        name = data[1]
        number = data[2]
        if name not in plates:
            plates[name] = number

            print(f'{name} registered {number} successfully')
        else:
            print(f'ERROR: already registered with plate number {number}')
    elif command=='unregister':
        name=data[1]
        if name not in plates:
            print(f'ERROR: user {name} not found')
        else:
            del plates[name]
            print(f'{name} unregistered successfully')

[print(f'{k} => {v}')for k,v in plates.items()]

    # 5
    # register Jonn CS12434
    # register Georgy JAVA123
    # register Andy ABD1214D
    # register Jesica VR23123EE
    # unregister Andy
