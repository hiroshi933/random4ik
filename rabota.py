import random
try:
    number = random.randint(1,100)
    print(number)
    numbers = set()
    current_number = 0
    while current_number != number:
        current_number = int(input("Введите число: "))
        if current_number in numbers:
            print('Вы уже вводили это число!')
        numbers.add(current_number)
        if current_number < number:
            print('Больше')
        elif current_number > number:
            print('Меньше')
    else:
        print('Вы угадали!')
        with open ('угадайка.txt', 'w', encoding='utf-8') as file:
            file.write(str(numbers))
except ValueError:
    print("Введите число")