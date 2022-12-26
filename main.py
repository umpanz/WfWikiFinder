import webbrowser

#Declaring needed variables
flag = True
iterIndex: int = 1
categories = {
    'w' : 'warframes',
    'p' : 'primaries',
    's' : 'secondaries',
    'm' : 'melees'
}

#Asking for item category
print('Looking for a (w)arframe, a (p)rimary weapon, a (s)econdary weapon or a (m)elee weapon?')
listItems = categories.get(str(input().lower()),0)

#Check if item is in available categories
if listItems == 0:
    print('Not defined (yet)!')
    input("Press Enter to continue...")
else:
    #Open relevant item list file
    with open('resources/' + listItems + '.txt') as file:
        items = [line.rstrip() for line in file]

    #Ask for item starting letter
    print("Which starting letter?")
    startingLetter = str(input().lower())

    #Get all items with starting letter from file and put them into list
    res = [idx for idx in items if idx[0].lower() == startingLetter]
    for x in res:
        print(iterIndex + ": " + x)
        iterIndex = iterIndex + 1

    #Check if items were found
    if iterIndex == 1:
        print('No item with mathcing starting letter found!')
        input("Press Enter to continue...")
    else:
        #Ask for item index from generated item list with starting letter
        print("Which item do you want to display?")
        index = input()

        #Check if number was entered
        try:
            int(index)
        except ValueError:
            flag = False
            print('Wrong format.')
            input("Press Enter to continue...")

        #Check if entered number is part of generated list
        if flag = True and index > 0 and index <= iterIndex:
            webbrowser.open('https://warframe.fandom.com/wiki/' + res[index - 1])
        else:
            print('Item not defined!')
            input("Press Enter to continue...")
