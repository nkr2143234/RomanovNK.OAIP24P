from datetime import datetime



clients = []


client_id_counter = 1


def add_client(name: str, **kwargs):

    global client_id_counter

    client = {
        "_id": client_id_counter,
        "name": name.strip(),
        "created_at": datetime.now().isoformat(),
        **kwargs
    }

    clients.append(client)
    client_id_counter += 1

    print(f"Добавлен клиент: {name} (id={client['_id']})")
    return client


def show_all_clients():

    if not clients:
        print("База пока пустая\n")
        return

    print("\nКлиенты в базе:\n" + "-" * 50)
    for client in clients:
        print(f"ID: {client['_id']}")
        print(f"Имя: {client['name']}")
        print(f"Создан: {client['created_at'][:19]}")


        for key, value in client.items():
            if key not in ["_id", "name", "created_at"]:
                if isinstance(value, list):
                    print(f"{key}: {', '.join(value)}")
                else:
                    print(f"{key}: {value}")
        print("-" * 50)


# ────────────────────────────────────────────────
# Примеры использования
# ────────────────────────────────────────────────

add_client("Алина",
           sketch_url="anna_tribal.jpg",
           sketch_description="трайбл, 12×18 см")

add_client("Дмитрий",
           appointment="2026-02-15 15:30",
           master="Иван",
           tattoo_size="15×10 см",
           placement="предплечье левое")

add_client("Мария",
           allergies=["latex", "red ink", "eucalyptus oil"],
           emergency_contact="+79991234567",
           note="очень боится боли — нужен хороший анестетик")

add_client("Сергей",
           appointment="2026-03-02",
           master="Катя",
           paid_deposit=3500)

add_client("Ольга")


show_all_clients()


