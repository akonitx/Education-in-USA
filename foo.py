from math import sqrt as s 

# TASK #1
a = float(input("Введіть катет a прямокутного трикутника: "))
b = float(input("Введіть катет b прямокутного трикутника: "))

c = s(a**2 + b**2)
P = a+b+c 

print(f"периметр:гіпотенуза: {P:.0f}:{c:.0f}")

#TASK 2
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def rectangle_perimeter(x1, y1, x2, y2):
    width = distance(x1, y1, x2, y1)
    height = distance(x2, y1, x2, y2)
    return 2 * (width + height)

def rectangle_area(x1, y1, x2, y2):
    width = distance(x1, y1, x2, y1)
    height = distance(x2, y1, x2, y2)
    return width * height

x1 = float(input("Введіть координату x першої вершини: "))
y1 = float(input("Введіть координату y першої вершини: "))
x2 = float(input("Введіть координату x другої вершини: "))
y2 = float(input("Введіть координату y другої вершини: "))

perimeter = rectangle_perimeter(x1, y1, x2, y2)
area = rectangle_area(x1, y1, x2, y2)

print("Периметр прямокутника:", perimeter)
print("Площа прямокутника:", area)

#TASK 3
def find_team_by_number(number):
    teams = {
        1: "Динамо",
        2: "Шахтар",
        3: "Зоря"
    }
    return teams.get(number, "Команда не знайдена")

number = int(input("Введіть номер призера: "))
team_name = find_team_by_number(number)
print("Назва команди:", team_name)

#TASK 4
def find_country_by_team_number(number):
    teams = {
        1: "Іспанія",
        2: "Іспанія",
        3: "Німеччина",
        4: "Англія",
        5: "Іспанія",
        6: "Португалія",
        7: "Німеччина",
        8: "Португалія",
        9: "Англія",
        10: "Англія"
    }
    return teams.get(number, "Команда не знайдена")

number = int(input("Введіть номер команди: "))
country = find_country_by_team_number(number)
print("Країна:", country)

