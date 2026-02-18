import json


projs = []



def load():
    global projs
    try:
        with open('data.json', 'r') as f:
            projs = json.load(f)
    except:
        projs = []



def save():
    with open('data.json', 'w') as f:
        json.dump(projs, f)



def show_projs():
    load()
    if not projs:
        print("\nНет проектов\n")
        return
    print("\n--- Проекты ---")
    for p in projs:
        print(f"{p['id']}. {p['name']} - {p['status']}")



def add_proj():
    load()
    name = input("Название проекта: ")
    new_id = len(projs) + 1
    projs.append({
        "id": new_id,
        "name": name,
        "status": "планирование",
        "tasks": []
    })
    save()
    print(f"Проект {name} создан!")



def add_task():
    load()
    show_projs()
    pid = int(input("ID проекта: "))

    for p in projs:
        if p['id'] == pid:
            text = input("Текст задачи: ")
            task_id = len(p['tasks']) + 1
            p['tasks'].append({
                "id": task_id,
                "text": text
            })
            save()
            print("Задача добавлена!")
            return
    print("Не найден проект")



def show_tasks():
    load()
    pid = int(input("ID проекта: "))

    for p in projs:
        if p['id'] == pid:
            print(f"\nЗадачи проекта {p['name']}:")
            if not p['tasks']:
                print("Задач нет")
            else:
                for t in p['tasks']:
                    print(f"  {t['id']}. {t['text']}")
            return



def change_status():
    load()
    show_projs()
    pid = int(input("ID проекта: "))

    for p in projs:
        if p['id'] == pid:
            print("1 - планирование")
            print("2 - в работе")
            print("3 - готов")
            s = input("Статус: ")

            if s == "1": p['status'] = "планирование"
            if s == "2": p['status'] = "в работе"
            if s == "3": p['status'] = "готов"

            save()
            print("Готово!")
            return



while True:
    print("\n1. Проекты")
    print("2. Создать проект")
    print("3. Добавить задачу")
    print("4. Задачи проекта")
    print("5. Статус проекта")
    print("0. Выход")

    c = input("Выбери: ")

    if c == "1": show_projs()
    if c == "2": add_proj()
    if c == "3": add_task()
    if c == "4": show_tasks()
    if c == "5": change_status()
    if c == "0": break