dic = {'yuk':'16/10/1997', 'kim':'10/09/1996', 'lee':'03/07/1995', 'park':'16/06/1998', 'son':'12/12/1994'}
select = 0

while select != 3:
    print('Select a number to do:')
    print('1. Enter a name to check birthday')
    print('2. Add new name and birthday')
    print('3. Terminate the program')
    select = int(input())

    if select == 1:
        print('Enter a name please: ')
        name = input()
        if name in dic:
            print(name + '\'s birthday is ' + dic[name])
            print('===================================\n')
        else:
             print('[Please enter the right name]')
             print('===================================\n')


    elif select == 2:
        name = input('Enter a name to add: ')
        birthday = input('Enter '+name+'\'s birthday: ')
        dic[name] = birthday
        print('[New data inserted into dictionary]')
        print('===================================\n')

    elif select == 3:
        print("[End of the program]")
        exit()

    else:
        print("[Please choose from the following number]")
        print('===================================\n')






