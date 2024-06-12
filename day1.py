import math

def calc_can_chi_calendar(year):

    can = ''
    chi = '' 

    x = year % 10

    if x == 0:
        can = 'Canh'
    elif x == 1:
        can = 'Tan'
    elif x == 2:
        can = 'Nham'
    elif x == 3:
        can = 'Quy'
    elif x == 4:
        can = 'Giap'
    elif x == 5:
        can = 'At'
    elif x == 6:
        can = 'Binh'
    elif x == 7:
        can = 'Dinh'
    elif x == 8:
        can = 'Mau'
    elif x == 9:
        can = 'Ky'

    y = year % 12

    if y == 0:
        chi = 'Than'
    elif y == 1:
        chi = 'Dau'
    elif y == 2:
        chi = 'Tuat'
    elif y == 3:
        chi = 'Hoi'
    elif y == 4:
        chi = 'Ty'
    elif y == 5:
        chi = 'Suu'
    elif y == 6:
        chi = 'Dan'
    elif y == 7:
        chi = 'Meo'
    elif y == 8:
        chi = 'Thin'
    elif y == 9:
        chi = 'Ty'
    elif y == 10:
        chi = 'Ngo'
    elif y == 11:
        chi = 'Mui'
    
    return f"{can} {chi}" 

print(calc_can_chi_calendar(2024))
print(calc_can_chi_calendar(2023))
print(calc_can_chi_calendar(1997))