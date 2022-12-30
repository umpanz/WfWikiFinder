import webbrowser


def main():
    # Declaring needed variables
    flag = True
    categories = {
        'w': 'warframes',
        'p': 'primaries',
        's': 'secondaries',
        'm': 'melees'
    }

    # Asking for item category
    print('Looking for a (w)arframe, a (p)rimary weapon, a (s)econdary weapon or a (m)elee weapon?')
    list_items = categories.get(f'{input().lower()}', 0)

    # Check if item is in available categories
    if list_items == 0:
        input('Not defined (yet)!\nPress Enter to continue...')
        quit()

    # Open relevant item list file
    with open(f'resources/{list_items}.txt') as file:
        items = [line.rstrip() for line in file]

    # Ask for item starting letter
    print('Which starting letter?')
    starting_letter = f'{input().lower()}'

    # Get all items with starting letter from file and put them into list
    res = [idx for idx in items if idx[0].lower() == starting_letter]
    for i, item in enumerate(res):
        print(f'{i + 1}: {item}')

    # Check if items were found
    if not res:
        input('No item with matching starting letter found!\nPress Enter to continue...')
        quit()

    # Ask for item index from generated item list with starting letter
    print('Which item do you want to display?')
    index = input()

    # Check if number was entered
    try:
        int(index)
    except ValueError:
        flag = False
        input('Wrong format.\nPress Enter to continue...')
        quit()

    # Check if entered number is part of generated list
    if flag and 0 < int(index) <= len(res):
        webbrowser.open(f'https://warframe.fandom.com/wiki/{res[int(index) - 1]}')
    else:
        input('Item not defined!\nPress Enter to continue...')
        quit()

if __name__ == '__main__':
    main()
