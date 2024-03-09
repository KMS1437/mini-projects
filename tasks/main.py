tsks = []
while True:
    print("Система управления задачами")
    print("1 Добавить задачу")
    print("2 Удалить задачу")
    print("3 Просмотреть задачи")
    print("4 Выйти")
    num = input("Набери номер: ")
    if num == "1":
        tsk = input("\nВведите задачу: ")
        tsks.append(tsk)
    elif num == "2":
        tsk = input("\nВведите задачу: ")
        tsks.remove(tsk)
    elif num == "3":
        print("\nСписок задач:")
        for tsk in tsks:
            print(f"{tsk}\n")
    elif num == "4":
        break
    else:
        print("\nНабери номер (или 1 или 2 или 3 или 4)\n")
