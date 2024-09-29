# Чтение клиентов из файла ccclients.list
with open('ccclients.list', 'r') as cc_file:
    cc_clients = {line.strip() for line in cc_file}

# Ввод списка всех клиентов
all_clients_string = input("Введите список всех клиентов, разделённых запятыми: ")

# Преобразование строки в множество
all_clients = {client.strip() for client in all_clients_string.split(',')}

# Поиск совпадений
matched_clients = cc_clients.intersection(all_clients)

# Вывод совпавших клиентов в одну строку, разделённую запятыми
print("Совпавшие клиенты СС:", ", ".join(matched_clients))
