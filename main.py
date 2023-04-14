import json
import datetime


data = []

with open('notes.json', 'w') as f:
    json.dump(data, f)

#Функция чтения заметок
def read_notes():
    with open("notes.json","r") as f:
        notes = json.load(f) 
    return notes

#Функция сохранения заметок
def save_notes(notes):
    with open("notes.json","w") as f:
        json.dump(notes,f,indent=4) 

# Генерируем id
def generate_id(notes):
    if not notes:
        return 1
    else:
        return max(note["id"] for note in notes) + 1

#Функция добавления заметки
def add():
    notes = read_notes()
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": generate_id(notes),
        "title": title,
        "body":body,
        "created at": now,
        "updated_at": now

    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")


# Функция чтения заметки
def read_note():
    notes = read_notes()
    id = int(input("Введите идентификатор заметки"))
    note = next((note for note in notes if note["id"] == id),None)
    if note:
        print(f"Заголовок: {note['title']}")
        print(f"Тело заголовка: {note['body']}")
        print(f"Дата создания: {note['created_at']}")
        print(f"Дата последнего изменения: {note['updated_at']}")

    else:
        print("Такого id нет")

def edit_note():
    notes = read_notes()
    id = int(input("Введите идентификатор заметки"))
    note = next((note for note in notes if note["id"] == id),None)
    if note:
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        note['title'] = title
        note['body'] = body
        note['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)  
    else:
        print("Такого id нет")

# Функция удаления заметки

def delete_note():
    notes = read_notes()
    index = int(input("Введите номер заметки для удаления: "))-1
    del notes[index]
    save_notes(notes)

def main():
    while True:
        print("Выберите действие:")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Ваш выбор: ")

        if choice == "1":
            notes = read_notes()
            for my_dict in notes:
                for key,value in my_dict.items():
                    print(f"{key},{value}")
        elif choice == "2":
            add()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")




if __name__ == '__main__':
        main()
