import webbrowser

iterIndex: int = 1

print('Looking for a (w)arframe, a (p)rimary weapon, a (s)econdary weapon or a (m)elee weapon?')
category = str(input().lower())

match category:
    case 'w':
        listItems = 'warframes'
    case 'p':
        listItems = 'primaries'
    case 's':
        listItems = 'secondaries'
    case 'm':
        listItems = 'melees'
    case _:
        print('Not defined (yet)!')
        input("Press Enter to continue...")

with open('resources/' + listItems + '.txt') as file:
    items = [line.rstrip() for line in file]

print("Which starting letter?")
inputStart = str(input().lower())
res = [idx for idx in items if idx[0].lower() == inputStart.lower()]
for x in res:
    print(str(iterIndex) + ": " + x)
    iterIndex = iterIndex + 1

print("Which item do you want to display?")
index = str(input())
webbrowser.open('https://warframe.fandom.com/wiki/' + res[int(index) - 1])
