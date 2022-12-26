import webbrowser

flag = True
iterIndex: int = 1
categories = {
    'w' : 'warframes',
    'p' : 'primaries',
    's' : 'secondaries',
    'm' : 'melees'
}

print('Looking for a (w)arframe, a (p)rimary weapon, a (s)econdary weapon or a (m)elee weapon?')
listItems = categories.get(str(input().lower()),0)

if listItems == 0:
    print('Not defined (yet)!')
    input("Press Enter to continue...")
else:
    with open('resources/' + listItems + '.txt') as file:
        items = [line.rstrip() for line in file]

    print("Which starting letter?")
    startingLetter = str(input().lower())
    res = [idx for idx in items if idx[0].lower() == startingLetter]
    for x in res:
        print(iterIndex + ": " + x)
        iterIndex = iterIndex + 1

    print("Which item do you want to display?")
    index = input()
    try:
        int(index)
    except ValueError:
        flag = False
        print('Wrong format.')

    if flag = True and index > 0 and index <= iterIndex:
        webbrowser.open('https://warframe.fandom.com/wiki/' + res[index - 1])
    else:
        print('Item not defined!')
        input("Press Enter to continue...")
