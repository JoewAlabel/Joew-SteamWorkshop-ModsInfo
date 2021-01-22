import requests
from bs4 import BeautifulSoup

# Set your mods here:
#modidslist = "1629667379,1629965981,1644646859"

# Ask for mods:
print('Enter mods separated by comma:')
modidslist = input()

modids = "".join(modidslist.split()).split(",")
modsfail = []
modsok = []

x = 1
print(f'Mods: {len(modids)}')

for modid in modids:
    page = requests.get(f'https://steamcommunity.com/sharedfiles/filedetails/?id={modid}')
    soup = BeautifulSoup(page.content, 'html.parser')
    mods = soup.find_all('div', class_='workshopItemTitle')

    if (soup.title.text != "Steam Community :: Error"):
        print(f'[{x}] {modid} - {mods[0].text} - https://steamcommunity.com/sharedfiles/filedetails/?id={modid}')
        modsok.append(modid)
        x += 1
    else:
        modsfail.append(modid)

if (len(modsfail) > 0):
    print('------------------------------------------------')
    print(f'Mods that don\'t exist anymore: {len(modsfail)}')
    x = 1
    for modid in modsfail:
        print(f'[{x}] {modid}')
        x += 1

print('------------------------------------------------')
print(f'Working Mods List:')
modsokstring = ','.join(modsok)
print(modsokstring)
