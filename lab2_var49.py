revenue = 0.0
count = 0
print("Команды: sell <товар> <цена> <кол-во>, report, exit")
while True:
    request = input("> ").split()
    if not request:
        continue
    if request[0] == "exit":
        break
    elif request[0] == "report":
        print("Выручка:", revenue)
        if count > 0:
            print("Средний чек:", revenue / count)
        else:
            print("Нет продаж")
    elif request[0] == "sell":
        if len(request) != 4:
            print("Ошибка: нужно sell <товар> <цена> <кол-во>")
            continue
        try:
            price = float(request[2])
            amount = int(request[3])
        except ValueError:
            print("Ошибка: цена и кол-во должны быть числами: целым/дробным и целым соответственно")
            continue
        revenue = revenue + price * amount
        count = count + 1
        print("Продано:", request[1], "на", price * amount)
    else:
        print("Неизвестная команда")