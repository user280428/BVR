import re
from periodictable import *

# Вопрос что это?
substance_mass_dict = {'H4N2O3': 354.8, 'N1Na1O2': 365.9, 'Cl1H4N1O4': 281.3, 'C12H26': 341.6, 'C1H4N2O1': 316.9,
         'C6H10O5': 946.2, 'C18H38': 558.9, 'C24H50': 46500.0, 'C2H4N2O6': 229.61, 'C4H8N8O8': -109.4,
         'C4H8N2O6О1': 415.7, 'C6H4N2O4': 23.9, 'C3H6N6O6': -93.4, 'C10H6N2O4': -49.8, 'C7H5N5O8': -55.7,
         'C1H6N2O4': 71.2, 'C4H8N4O8': 283.5, 'C1H6N4O3': 364.3, 'C6H3N5O8': -90.0, 'C6H8N6O18': 636.4,
         'C6H3N3O6': 9.63, 'C6H4N2O5': 223.2, 'C6H2N3O7': 211.9, 'C1H5N3O7': 230.7, 'H3N3O8': 415.3,
         'C10H5N3O6': 49.4, 'H6N4O7': 365.5, 'C6H3N3O7': 200.1, 'C2H6N4O10': 257.1, 'C24H29N11O42': 2391.0,
         'C6N12O6': 1138.8, 'C1H3N1O2': 113.2, 'C7H5N3O6': 56.6, 'C3H5N3O9': 344.6, 'C5H8N4O12': 502.3}


# Запрашиваем входные данные пока сумма процентов не будет равна 100
m = True
while m:
    subst_1, percentage_1 = (input('Введите химеческую формулу компонента 1: '),
                             int(input('Введите процент для компонента 1: ')))
    subst_2, percentage_2 = (input('Введите химеческую формулу компонента 2: '),
                             int(input('Введите процент для компонента 2: ')))
    subst_3, percentage_3 = (input('Введите химеческую формулу компонента 3: '),
                             int(input('Введите процент для компонента 3: ')))
    if percentage_1 + percentage_2 + percentage_3 == 100:
        m = False
    elif percentage_1 + percentage_2 + percentage_3 != 100:
        print('Процентное соотношение указано не верно')
    if len(subst_3) == 0 and percentage_3 != 0:
        percentage_3 = 0


# Функция по преобразованию формулы ВВ в словари
def process_chemical_formula(string):           # функция считает количество химических элементов и записывает их в виде списка
  match = re.findall(r"\(\w+\)\d+", string)     # Используем регулярное выражение, чтобы найти группы, заключенные в скобки и их коэффициент
  clean = re.sub(r"\(\w+\)\d+",'', string)      # Добавляем все кроме найденных групп в отдельную строку
  match2 = []
  match4 = []
  match6 = []

  for i in match:                               # Найденные группы со скобками преобразуем из вида (СО)3 в (СО)(СО)(СО)
    try:
      match2 += re.findall(r"\(\w+\)?", i) * int(re.sub(r"\(\w+\)?",'', i))
    except:
      match2 += re.findall(r"\(\w+\)?", i)
  for i in match2:                              # И добавляем их в конец строки clean
    clean+=i

  clean = re.sub(r'[\(\)]', '', clean)          # Избавляемся от скобок
  match3 = re.findall(r"[A-Z][a-z]+\d?", clean) # Ищем все элементы состоящие из (заглавной и маленькой буквы) и их коэффициент, напимер "Al2"
  clean = re.sub(r"[A-Z][a-z]+\d?",'', clean)   # Удаляем из строки clean найденные элементы

  for i in match3:                              # Найденные элементы преобразуем из вида Al2 в AlAl
    try:
      match4 += re.findall(r"[A-Z][a-z]", i) * int(re.sub(r"[A-Z][a-z]",'', i))
    except:
      match4 += re.findall(r"[A-Z][a-z]", i)    # И добавляем их в конец строки clean
  for i in match4:
    clean+=i

  match5 = re.findall(r"\w?\d+", clean)         # Ищем все элементы состоящие из заглавной буквы и их коэффициент, напимер "C2"
  clean = re.sub(r"\w?\d+",'', clean)           # Удаляем из строки clean найденные элементы

  for i in match5:                              # Найденные элементы преобразуем из вида C2 в CC
    try:
      match6 += re.findall(r"[A-Z]", i) * int(re.sub(r"[A-Z]",'', i))
    except:
      print(i)
  for i in match6:                              # И добавляем их в конец строки clean
    clean+=i


  clean2={}
  for i in range(len(clean)):                   # Цикл заполняет словарь clean2 ключами соответствующие химическим элементам
    try:
      if clean[i+1] == clean[i+1].lower():
        clean2[clean[i]+clean[i+1]] = 0
      else:
        if clean[i] == clean[i].upper():
          clean2[clean[i]] = 0
    except:
      if clean[i] == clean[i].upper():
        clean2[clean[i]] = 0


  for i in range(len(clean)):                   # Цикл считает количество химических элементов
    try:
      if clean[i+1] == clean[i+1].lower():
        clean2[clean[i]+clean[i+1]] += 1
      else:
        if clean[i] == clean[i].upper():
          clean2[clean[i]] += 1
    except:
        if clean[i] == clean[i].upper():
          clean2[clean[i]] += 1
        elif clean[i] == clean[i].lower():
          clean2[clean[i-1] + clean[i]] += 0
  return clean2


# Преобразование формул веществ в словари
subst_1_dict = process_chemical_formula(subst_1)
subst_2_dict = process_chemical_formula(subst_2)
subst_3_dict = process_chemical_formula(subst_3)


# Молярные массы каждого из веществ ВВ
molar_mass_1 = 0
molar_mass_2 = 0
molar_mass_3 = 0


# Подсчет молярных масс веществ
for k, v in subst_1_dict.items():
    molar_mass_1 += round(elements.symbol(k).mass) * v
for k, v in subst_2_dict.items():
    molar_mass_2 += round(elements.symbol(k).mass) * v
for k, v in subst_3_dict.items():
    molar_mass_3 += round(elements.symbol(k).mass) * v


# Количество моль вещества в условном килограмме
mole_in_kilo_1 = (percentage_1*10)/molar_mass_1
mole_in_kilo_2 = (percentage_2*10)/molar_mass_2
mole_in_kilo_3 = 0
try:
    mole_in_kilo_3 = (percentage_3*10)/molar_mass_3
except:
    mole_in_kilo_3 = 0


# Список строк грамм-атомов элементов
def gram_atoms_str_list():
    global mole_in_kilo_1
    global mole_in_kilo_2
    global mole_in_kilo_3
    global subst_1_dict
    global subst_2_dict
    global subst_3_dict

    dct_list = [subst_1_dict, subst_2_dict, subst_3_dict]

    moles_list = [round(mole_in_kilo_1, 3), round(mole_in_kilo_2, 3), round(mole_in_kilo_3, 3)]

    all_keys = list(set(subst_1_dict.keys()) | set(subst_2_dict.keys()) | set(subst_3_dict.keys()))

    main_dct = {}
    for el in all_keys:
        main_dct[el] = []
        for dct in dct_list:
            if el in dct:
                main_dct[el].append(dct[el])
            else:
                main_dct[el].append(0)

    str_list = []
    for k, vs in main_dct.items():
        num = 0
        string = ""
        string += f"{k} = "
        j = 0
        for i, v in enumerate(vs):
            if v == 0:
                continue
            if j > 0:
                string += " + "
            j += 1
            num += moles_list[i] * v
            string += f"{moles_list[i]}*{v}"
        string += f" = {num}"
        str_list.append(string)
    return str_list


# Вычисление общее количество каждого химического элемента
def count_brutto_formula_dict():
    global subst_1_dict
    global subst_2_dict
    global subst_3_dict
    global mole_in_kilo_1
    global mole_in_kilo_2
    global mole_in_kilo_3

    initial_mole_dict = {"C": 0, "H": 0, "N": 0, "O": 0, "Al": 0}
    moles_list = [mole_in_kilo_1, mole_in_kilo_2, mole_in_kilo_3]
    dct_list = [subst_1_dict, subst_2_dict, subst_3_dict]

    for el in initial_mole_dict:
        a = 0
        for i, dct in enumerate(dct_list):
            for k, v in dct.items():
                if k == el:
                    a += v * moles_list[i]
        initial_mole_dict[el] = a
    return initial_mole_dict

initial_mole_dict = count_brutto_formula_dict()
initial_mole_dict_print = count_brutto_formula_dict()


# Кислородный баланс и кислородный коэфициент
def count_oxygen_balance():
    global initial_mole_dict
    d = initial_mole_dict.copy()
    oxygen_balance_str = f'[{round(d["O"], 3)} - (2 * {round(d["C"], 3)} + 0.5 * {round(d["H"], 3)} + 1.5 * {round(d["Al"], 3)})] * 16/1000'
    oxygen_koef_str = f'{round(d["O"], 3)}/(2 * {round(d["C"], 3)} + 0.5 * {round(d["H"], 3)} + 1.5 * {round(d["Al"], 3)})'
    oxygen_balance = round((d["O"] - (2 * d["C"] + 0.5 * d["H"] + 1.5 * d["Al"]))*16/1000, 4)
    oxygen_koef =  round(d["O"]/(2 * d["C"] + 0.5 * d["H"] + 1.5 * d["Al"]), 2)
    return {"ox_balance": oxygen_balance, "ox_coef": oxygen_koef, "ox_balance_str": oxygen_balance_str, "ox_coef_str": oxygen_koef_str}

ox_balance = count_oxygen_balance()["ox_balance"]
ox_coef = count_oxygen_balance()["ox_coef"]
ox_balance_str = count_oxygen_balance()["ox_balance_str"]
ox_coef_str = count_oxygen_balance()["ox_coef_str"]



# Проверка общей массы элементов (в сумме должна быть 1000 грамм)
def total_mas_counter_str():
    global initial_mole_dict

    total_mass = 0
    main_str = ""
    i = 1
    for k, v in initial_mole_dict.items():
        total_mass += round(v, 3) * elements.symbol(k).mass
        main_str += f"{round(v, 3)} * {round(elements.symbol(k).mass)}"

        if i < len(initial_mole_dict):
            main_str += " + "
        i += 1
    return {"total_mass": total_mass, "total_mass_str": main_str}

total_mass = total_mas_counter_str()["total_mass"]
total_mass_str = total_mas_counter_str()["total_mass_str"]








product_mole_dict = {"Al2O3": 0, "H2O": 0, "H2": 0, "CO2": 0, "CO": 0, "C": 0, "O2": 0, "N2": 0} # пустой список для продуктов реакции взрыва

if initial_mole_dict["Al"]/2 < initial_mole_dict["O"]/3:                    # подсчет продуктов взрыва
  product_mole_dict["Al2O3"] += initial_mole_dict["Al"] / 2
  initial_mole_dict["O"] -= product_mole_dict["Al2O3"] * 3
elif initial_mole_dict["Al"]/2 >= initial_mole_dict["O"]/3:
  product_mole_dict["Al2O3"] += initial_mole_dict["Al"] / 2
  initial_mole_dict["O"] = 0

if initial_mole_dict["H"]/2 < initial_mole_dict["O"]:
  product_mole_dict["H2O"] += initial_mole_dict["H"] / 2
  initial_mole_dict["O"] -= product_mole_dict["H2O"]
elif initial_mole_dict["H"]/2 >= initial_mole_dict["O"]:
  product_mole_dict["H2O"] += initial_mole_dict["O"]
  initial_mole_dict["O"] = 0
  initial_mole_dict["H"] -= initial_mole_dict["O"]*2
  product_mole_dict["H2"] = initial_mole_dict["H"] / 2

if initial_mole_dict["C"] < initial_mole_dict["O"]:
  product_mole_dict["CO"] += initial_mole_dict["C"]
  initial_mole_dict["O"] -= product_mole_dict["CO"]
elif initial_mole_dict["C"] >= initial_mole_dict["O"]:
  product_mole_dict["CO"] += initial_mole_dict["O"]
  initial_mole_dict["O"] = 0
  initial_mole_dict["C"] -= initial_mole_dict["O"]
  product_mole_dict["C"] = initial_mole_dict["C"]

if product_mole_dict["CO"] < initial_mole_dict["O"]:
  product_mole_dict["CO2"] += product_mole_dict["CO"]
  product_mole_dict["CO"] -= product_mole_dict["CO"]
  initial_mole_dict["O"] -= product_mole_dict["CO2"]
elif product_mole_dict["CO"] >= initial_mole_dict["O"]:
  product_mole_dict["CO2"] += initial_mole_dict["O"]
  product_mole_dict["CO"] -= product_mole_dict["CO2"]
  initial_mole_dict["O"] = 0

product_mole_dict["O2"] += initial_mole_dict["O"] / 2
product_mole_dict['N2'] += initial_mole_dict["N"] / 2


Qpv = product_mole_dict["Al2O3"] * 1666.8 + product_mole_dict["H2O"] * 240.7 + product_mole_dict["CO"] * 113.7 + product_mole_dict["CO2"] * 395.7 + product_mole_dict["O2"] * 240.7
Qvv = (mole_in_kilo_1*substance_mass_dict[(str(dict(sorted((subst_1_dict).items()))).replace(':','').replace("'",'').replace('{','').replace('}','').replace(' ','').replace(',',''))] +
       mole_in_kilo_2*substance_mass_dict[(str(dict(sorted((subst_2_dict).items()))).replace(':','').replace("'",'').replace('{','').replace('}','').replace(' ','').replace(',',''))]) # upgreid
Q = Qpv - Qvv

Vpv = 22.4 * (product_mole_dict["H2O"]+product_mole_dict["CO2"]+product_mole_dict["CO"]+product_mole_dict["N2"]+product_mole_dict["O2"])/1000

niai = product_mole_dict["Al2O3"] * 24.97 + product_mole_dict["H2O"] * 16.76 + product_mole_dict["CO"] * 20.1 + product_mole_dict["CO2"] * 41.1 + product_mole_dict["O2"] * 20.1 + product_mole_dict['N2'] * 20.1
nibi = (product_mole_dict["Al2O3"] * 0 + product_mole_dict["H2O"] * 90.1 + product_mole_dict["CO"] * 18.86 + product_mole_dict["CO2"] * 24.3 + product_mole_dict["O2"] * 18.86 + product_mole_dict['N2'] * 18.86)/10000

temperature = (-niai + (niai**2+4*nibi*Q*1000)**0.5)/(2*nibi)
pressure = (1.01*10**5*Vpv*(temperature+273)*900)/(273*(1-0.001*Vpv*900))

A = Q*(1-(1.01*10**5/pressure)**0.09)
KPD = A*100/Q




def dict_to_str(dct, brackets=True):
    if len(dct) == 1:
        brackets = False
    dict_str = ""
    if brackets:
        dict_str += "("
    i = 1
    for k, v in dct.items():
        i += 1
        if v == 0:
            continue
        elif v == 1:
            dict_str += k
        else:
            dict_str += f"{round(v,3)}*{k}"
        if i <= len(dct):
            dict_str += " + "

    if brackets:
        dict_str += ")"
    return dict_str







print()



print(f"Компонет 1 - {subst_1} - {percentage_1} %")
print(f"Компонет 2 - {subst_2} - {percentage_2} %")
print(f"Компонет 3 - {subst_3} - {percentage_3} %")
print()

print('Грамм-молекурярный состав ВВ')
print(f"({percentage_1 * 10}/{round(molar_mass_1)}) * {subst_1} + ({percentage_2 * 10}/{round(molar_mass_2)}) * {subst_2} + ({percentage_3 * 10}/{round(molar_mass_3)}) * {subst_3}")
print(f"{round(mole_in_kilo_1, 3)} * {subst_1} + {round(mole_in_kilo_2, 3)} * {subst_2} + {round(mole_in_kilo_3, 3)} * {subst_3}")
print()

print('Суммарное количество грамм-атомов')
lst = gram_atoms_str_list()
for l in lst:
    print(l)
print()

print('Условная брутто-формула ВВ')
# print(f"({percentage_1 * 10}/{round(molar_mass_1)}) * {dict_to_str(subst_1_dict)} + ({percentage_2 * 10}/{round(molar_mass_2)}) * {dict_to_str(subst_2_dict)} + ({percentage_3 * 10}/{round(molar_mass_3)}) * {dict_to_str(subst_3_dict)}")
# print(f"{round(mole_in_kilo_1, 3)} * {dict_to_str(subst_1_dict)} + {round(mole_in_kilo_2, 3)} * {dict_to_str(subst_2_dict)} + {round(mole_in_kilo_3, 3)} * {dict_to_str(subst_3_dict)}")
print(dict_to_str(initial_mole_dict_print, brackets=False))
print()

print('Проверка суммарной массы')
print(f"{total_mass_str} = {round(total_mass)}")
print()

print(f"Кислородный баланс ВВ")
print(f"{ox_balance_str} = {ox_balance*100} %")
print(f"Кислородный коэффициент ВВ")
print(f"{ox_coef_str} = {ox_coef}")
print()



print()
print()
print()
print()
print()
print(f"Продукты взрыва - {dict_to_str(product_mole_dict, brackets=False)}")
print()

print(f"Температура взрыва - {round(temperature)} С°")
print(f"Давление возникающее при взрыве - {round(pressure / 10 ** 9, 3)} ГПа")
print(f"Идеальная работоспособность - {round(A)} кДж/кг")
print(f"КПД - {round(KPD, 2)} %")

# with open('Ответ.txt', 'w', encoding='utf-8') as f:
#   f.write('Исходные данные\n')
#   f.write(f"Компонет 1 - {a1} - {a2} %\n")
#   f.write(f"Компонет 2 - {b1} - {b2} %\n")
#   f.write(f"Компонет 3 - {c1} - {c2} %\n")
#   f.write('\n')
#
#   f.write(f"( ({a2*10}) / {round(a3)} ) {a1} + ( ( {b2 * 10} ) / {round(b3)} ) {b1} + (({c2*10}) / {round(c3)} ) {c1} ")
#   f.write(f"{a4} {a1} + {b4} {b1} + {c4} {c1} \n")
#   f.write(f"{round(summ_M, 3)} \n")
#   f.write(f"{el}\n")
#   # el2_ = dict((k, round(v, 3)) for k, v in el2.items())
#   f.write(f"{el2_}\n")
#
#   f.write(f"Продукты взрыва - {product}\n")
#   f.write("\n")
#   f.write('Термодинамические характеристики')
#   f.write(f"Температура взрыва - {round(T)} С°\n")
#   f.write(f"Давление возникающее при взрыве - {round(P / 10 ** 9, 3)} ГПа\n'")
#   f.write(f"Работа взрыва - {round(A)} кДж/кг\n")
#   f.write(f"КПД - {round(KPD, 1)} %\n")


"""
C3H5N3O9 -  17
NH4NO3 -    70
Al -        13
"""


"""
C3H5N3O9 - 15
NH4NO3 - 82
Al - 3
"""