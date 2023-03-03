import pandas as pd

df = pd.read_csv('survey_results_public.csv')

while True:
        user_input = input('Выбор опций:\n1.Сколько программистов является профессионалами и сколько хобби программистами \n2. средний, максимальный и минимальный возраст\n3. Таблица со странами\n4. Таблица с валютами\n5. Выход\n-->')
        if user_input == '1':
            print(df['Hobbyist'].value_counts())
        elif user_input == '2':
            print(df['Age'].describe())
        elif user_input == '3':
            print(df['Country'].value_counts())
        elif user_input == '4':
            print(df['CurrencyDesc'].value_counts())
        elif user_input == '5':
            print('До свидания ;)')
            break
        else:
            print('Выберите 1, 2, 3, 4 или 5')