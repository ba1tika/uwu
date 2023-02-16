Countoper=int(input("Кол-во операций\n")) #вводим переменную-счётчик
first = float(input("Первое число:\n")) #вводим переменную с названием first значения int и просим пользователя ввести число

while Countoper!=0: #цикл пока переменная-счётчик не равна 0
    masssive = [first] #вводим массив, с включенной в него переменной irst (каждый проход цикла обнуляем его)
    second = float(input("Второе число:\n")) #ребуем ввести второе число и преобразуем его ииз строки в int
    oper=input("Введите операцию:\n") #требуем ввести операцию
    if oper=="+": #проверка операции
        masssive.append(second) #добавляем в массив второе число
        result=sum(masssive) #испольуем sum чтобы сложить элементы
    elif oper =="-": #проверка операции
        result = first - second #вычитаем
    elif oper =="*": #проверка операции
        result = first * second #умножаем
    elif oper =="//": #проверка операции
        result = first // second #елим без остатка
    elif oper =="^":#проверка операции
        result = first ^ second #возводим в степень
    elif oper == "/": #проверка операции
        try: #выполняем операцию, в случае ошибки ловим её
            result = first / second #делим
        except ZeroDivisionError: #если мы пытаемся делить на 0
            print("Seriously? You're trying to divide by zero..")#надпись намёк на неправильное действие
            break #завершаем программу
    print(first,oper,second,"=",result) #выводим необходимые действия
    first=result #присваиваем в переменную first получившийся результат
    Countoper-=1 #уменьшаем нашу переменную-счётчик
