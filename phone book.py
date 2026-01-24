print("=== ТЕЛЕФОННАЯ КНИГА ===")

name = input("Введите имя: ")
phone = input("Введите телефон: ")

with open("контакты.txt", "a", encoding="utf-8") as f:
    f.write(f"{name}: {phone}\n")

print("\nВсе контакты:")
with open("контакты.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())