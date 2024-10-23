import random
try:
    with open ('questions.txt', 'r', encoding='utf-8') as file:
        questions = file.readlines()
    with open('response.txt', 'r', encoding='utf-8') as file:
        response = file.readlines()
        uslovie_1 = random.choice(questions)
        print(uslovie_1)
        uslovie_2 = random.choice(response)
        print(uslovie_2)
except FileNotFoundError:
    print("Файл не найден.")