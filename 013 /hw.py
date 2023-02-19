import requests
from bs4 import BeautifulSoup as BS

page = requests.get("https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/").text
soup = BS(page,"html.parser")

while True:
        user_input = input('Please choose:\n1. Heltermaa\n2. Jõgeva\n3. Jõhvi\n4. Kihnu\n5. Exit\n-->')
        list = ['city', 'temperature', 'average', 'max', 'min', 'humidity% average ', 'humidity% min',
                'wind speed average  ', 'wind speed max ',
                'precipitation', 'sunshine (hrs)']
        list2 = soup.find_all('tr')[2].text.split()
        list3 = soup.find_all('tr')[3].text.split()
        list4 = soup.find_all('tr')[4].text.split()
        list5 = soup.find_all('tr')[5].text.split()
        if user_input == '1':
            print(f'{list[0]}: {list2[0]}')
            print(f'{list[1]}: {list2[1]}')
            print(f'{list[2]}: {list2[2]}')
            print(f'{list[3]}: {list2[3]}')
            print(f'{list[4]}: {list2[4]}')
            print(f'{list[5]}: {list2[5]}')
            print(f'{list[6]}: {list2[6]}')
            print(f'{list[7]}: {list2[7]}')
            print(f'{list[8]}: {list2[8]}')
        elif user_input == '2':
            print(f'{list[0]}: {list3[0]}')
            print(f'{list[1]}: {list3[1]}')
            print(f'{list[2]}: {list3[2]}')
            print(f'{list[3]}: {list3[3]}')
            print(f'{list[4]}: {list3[4]}')
            print(f'{list[5]}: {list3[5]}')
            print(f'{list[6]}: {list3[6]}')
            print(f'{list[7]}: {list3[7]}')
            print(f'{list[8]}: {list3[8]}')
        elif user_input == '3':
            print(f'{list[0]}: {list4[0]}')
            print(f'{list[1]}: {list4[1]}')
            print(f'{list[2]}: {list4[2]}')
            print(f'{list[3]}: {list4[3]}')
            print(f'{list[4]}: {list4[4]}')
            print(f'{list[5]}: {list4[5]}')
            print(f'{list[6]}: {list4[6]}')
            print(f'{list[7]}: {list4[7]}')
            print(f'{list[8]}: {list4[8]}')
        elif user_input == '4':
            print(f'{list[0]}: {list5[0]}')
            print(f'{list[1]}: {list5[1]}')
            print(f'{list[2]}: {list5[2]}')
            print(f'{list[3]}: {list5[3]}')
            print(f'{list[4]}: {list5[4]}')
            print(f'{list[5]}: {list5[5]}')
            print(f'{list[6]}: {list5[6]}')
            print(f'{list[7]}: {list5[7]}')
            print(f'{list[8]}: {list5[8]}')
        elif user_input == '5':
            print('Good Bye')
            break
        else:
            print('Choice is out of range')
