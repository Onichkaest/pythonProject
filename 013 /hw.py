import requests
from bs4 import BeautifulSoup as BS

page = requests.get("https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/").text
soup = BS(page,"html.parser")

while True:
        user_input = input('Please choose:\n1. Heltermaa\n2. Jõgeva\n3. Jõhvi\n4. Kihnu\n-->')
        list = ['city', 'temperature', 'average', 'max', 'min', 'humidity% average ', 'humidity% min',
                'wind speed average  ', 'wind speed max ',
                'precipitation', 'sunshine (hrs)']
        list2 = soup.find_all('tr')[2].text.split()
        list3 = soup.find_all('tr')[3].text.split()
        list4 = soup.find_all('tr')[4].text.split()
        list5 = soup.find_all('tr')[5].text.split()
        if user_input == '1':
            print(f'{list}\n {list2}')
        elif user_input == '2':
            print(f'{list}\n {list3}')
        elif user_input == '3':
            print(f'{list}\n {list4}')
        elif user_input == '4':
            print(f'{list}\n {list5}')
        else:
            print('Try again')
