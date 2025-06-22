x = 6
name = "Дима"
random_bool = True
print("Привет, " + name)
print("как прошел твой день, " + name)
print("Что ты сегодня ел, " + name)
print(random_bool)
weekDays = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
]
print(weekDays[2])
length = len(weekDays)  # вот здесь просто число (длина списка)
print(length)

monday = weekDays[0]
print(monday)

print(weekDays[6])

thursday = weekDays[3]
print(thursday)

sunday = weekDays[6]
print(sunday)


# whatIf = weekDays[7]  - вне диапазона списка
# print(whatIf)

def sumNumbers(a, b):  # на этой строке объявление функции, ниже - тело
    print(a + b)
    print("Меня вызвали 1")
    print("Меня вызвали 2")
    print("Меня вызвали 3")
    print("Меня вызвали 4")


print("Меня вызвали X")
sumNumbers(5, 6)


# эта строка уже не является телом функции, так как в ее начале нет отступа!

def greet(name):
    print("Привет, " + name)


greet("Дима")
greet("Наташа")


def sum_numbers(num_1, num_2):
    print("Слагаемое 1 = ", num_1)
    print("Слагаемое 2 = ", num_2)
    result = num_1 + num_2
    print("Сумма =", result)
    return result


x = sum_numbers(4, 5)
print(x)


def myltuplay(x, y):
    return x * y


m = myltuplay(3, 4)
print(m)


def delenie(x, y):
    return x / y


n = delenie(45, 5)
print(n)

globalVar = 1


def printGlobal():
    print(globalVar)


def printLocal():
    Local = 2
    print(Local)


printGlobal()
printLocal()