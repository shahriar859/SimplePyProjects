command = ''
Started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if Started:
            print('Car is already started!')
        else:
            Started = True
            print('Car started...')
    elif command == 'stop':
        if not Started:
            print('Car is already stopped!')
        else:
            Started = False
            print('Car stopped.')
    elif command == 'help':
        print('''
        star - to start the car
        stop - to stop the car
        quit - to exit the game
        ''')
    elif command == 'quit':
        break
    else:
        print("Sorry I don't understand that!")