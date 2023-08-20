import csv 
import json
from typing import List, Dict, Tuple

def add_record():
    """
    функция для добавления записи в справочнике
    """
    # ввод данных пользователем
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    middle_name = input('Введите отчество: ')
    organization = input('Введите имя организации: ')
    work_phone = input('Введите рабочий телефон: ')
    personal_phone = input('Введите личный телефон: ')

     # кортеж для сохранения в csv файл
    new_record = (first_name, last_name, middle_name, organization, work_phone, personal_phone)

    if not is_duplicate_record(new_record):
        # сохранение в CSV
        try:
            with open('phone_directory.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(new_record)
        except Exception as e:
            print(f"Ошибка при сохранении в CSV: {e}")
        
        # список для сохранения в json файл
        record = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'organization': organization,
            'work_phone': work_phone,
            'personal_phone': personal_phone
        }
        # сохранение в JSON
        try:
            with open('phone_directory.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = []
        
        data.append(record)
        
        with open('phone_directory.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print('Запись добавлена')
        print('-' * 20)
    else:
        print('Такая запись уже существует')
        print('-' * 20)

def is_duplicate_record(new_record: Tuple[str]) -> bool:
    """
    функция проверяет, есть ли такая запись уже в справочнике
    """
    # считываем файл csv и перебор в цикле значений на совпадение 
    with open('phone_directory.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if tuple(row) == new_record:
                return True
    return False


def display_records():
    """
    функция для вывода записей из справочника
    """
    print("Вывод записей из справочника")
    
    # чтение из CSV
    with open('phone_directory.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))
    
    print('-' * 20)
    print('-' * 20)
    # чтение из JSON
    with open('phone_directory.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for record in data:
            print(', '.join(record.values()))

    print("Конец записей")
    print('-' * 20)



def edit_record():
    """
    функция для редактирования записей из справочника
    """
    last_name = input('Введите фамилию для редактирования: ')

    found = False
    updated_records = []
    # считываем файл csv и перебор в цикле для редактирования записи
    with open('phone_directory.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == last_name:  
                found = True
                print('Редактирование записи:')
                print(', '.join(row))
                new_record = []
                new_record.append(row[0])  
                new_record.append(input('Введите новую фамилию: '))
                new_record.append(input('Введите новое отчество: '))
                new_record.append(input('Введите новое имя организации: '))
                new_record.append(input('Введите новый рабочий телефон: '))
                new_record.append(input('Введите новый личный телефон: '))
                updated_records.append(new_record)
            else:
                updated_records.append(row)

    if not found:
        print('Запись не найдена')
    else:
        with open('phone_directory.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for record in updated_records:
                writer.writerow(record)

        print('Запись успешно обновлена')


def search_records():
    """
    функция для поиска записей из справочника
    """
    query = input('Введите часть фамилии или другие характеристики для поиска: ')

    found = False
    # считываем файл csv и перебор в цикле для поиска записи
    with open('phone_directory.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if any(query.lower() in field.lower() for field in row):
                found = True
                print(', '.join(row))

    if not found:
        print('Записи не найдены')

add_record()
display_records()
edit_record()
search_records()
