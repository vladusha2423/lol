# Ясно для чего
def df_to_dict(df):
    lst = df.values.tolist()
    dict = {}
    for i in range(len(lst)):
        dict[i + 1] = {}
        for j in range(len(lst[i])):
            dict[i + 1]["Company"] = lst[i][0]
            dict[i + 1]["Product"] = lst[i][1]
            dict[i + 1]["TypeName"] = lst[i][2]
            dict[i + 1]["Inches"] = lst[i][3]
            dict[i + 1]["ScreenResolution"] = lst[i][4]
            dict[i + 1]["Cpu"] = lst[i][5]
            dict[i + 1]["Ram"] = lst[i][6]
            dict[i + 1]["Memory"] = lst[i][7]
            dict[i + 1]["Gpu"] = lst[i][8]
            dict[i + 1]["OpSys"] = lst[i][9]
            dict[i + 1]["Weight"] = lst[i][10]
            dict[i + 1]["Price_euros"] = lst[i][11]
    return dict


# Для Company, TypeName, Inches, Ram, OS
# На вход - Notebooks(словарь, который фильтруем), характеристика(из тех что выше),
# список выбранных пользователем значений
def filter_by_specification(dct, specification, lst):
    new_dct = {}
    counter = 0
    for notebook in dct.values():
        if notebook[specification] in lst:
            new_dct[counter] = notebook
        counter += 1
    return new_dct


# Для Company, TypeName, Inches, Ram, OS
# Вообще - ненужная для проекта штука. Но чисто так можно почекать какие есть различные значения той или иной
# характеристики. На вход по классике Notebooks, и нужная характеристика
def unique_specifications(dct, specification):
    lst = []
    for notebook in dct.values():
        if notebook[specification] not in lst:
            lst.append(notebook[specification])
    return lst


# Аналогично для Cpu
def get_cpu(dct):
    lst_cpu = []
    for i in unique_specifications(dct, "Cpu"):
        kek = i.split()
        if kek[0] + ' ' + kek[1] == "Intel Core":
            lol = kek[0] + ' ' + kek[1] + ' ' + kek[2]
        else:
            lol = kek[0] + ' ' + kek[1]
        if lol not in lst_cpu:
            lst_cpu.append(lol)
    return lst_cpu


# Фильтр по CPU. На вход подается Notebooks, список значений
def filter_by_cpu(dct, cpus):
    new_dct = {}
    counter = 0
    for notebook in dct.values():
        kek = notebook["Cpu"].split()
        if kek[0] + ' ' + kek[1] == "Intel Core":
            lol = kek[0] + ' ' + kek[1] + ' ' + kek[2]
            if lol in cpus:
                new_dct[counter] = notebook
        else:
            lol = kek[0] + ' ' + kek[1]
            if lol in cpus:
                new_dct[counter] = notebook
        counter += 1
    return new_dct


# Вспомогательная
def is_lst_in_str(lst, str):
    for i in lst:
        if i in str:
            return True
    return False


# Фильтр по памяти. На вход подается Notebooks, список значений
def filter_by_memory(dct, lst):
    new_dct = {}
    counter = 0
    for notebook in dct.values():
        if is_lst_in_str(lst, notebook["Memory"]):
            new_dct[counter] = notebook
        counter += 1
    return new_dct


# Фильтр по GPU. На вход подается Notebooks, список значений
def filter_by_gpu(dct, lst):
    new_dct = {}
    counter = 0
    for notebook in dct.values():
        if notebook["Gpu"].split()[0] in lst:
            new_dct[counter] = notebook
        counter += 1
    return new_dct


# Вспомогательная, можно почекать какие есть разрешения экрана
def find_screen_resolution(dct):
    lst1 = []
    for i in dct.values():
        lst = i["ScreenResolution"].split()
        if lst[-1] not in lst1:
            lst1.append(lst[-1])
    return lst1


# Фильтр по разрешению экрана. На вход подается Notebooks, список значений
def filter_by_screen_resolution(dct, lst_srch):
    lst = {}
    counter = 0
    for i in dct.values():
        for j in lst_srch:
            if j in i["ScreenResolution"]:
                lst[counter] = i
        counter += 1
    return lst


# Фильтр по весу ноутбука. На вход подается Notebooks, список значений
def filter_by_weight(dct, lst_srch):
    lst = {}
    counter = 0
    for i in dct.values():
        a = i['Weight'].split('kg')
        b = float(a[0])
        if 'under 1' in lst_srch:
            if b < 1.:
                lst[counter] = i
        if 'from 1 to 2' in lst_srch:
            if 1. <= b <= 2.0:
                lst[counter] = i
        if 'from 2' in lst_srch:
            if b > 2.:
                lst[counter] = i
        counter += 1
    return lst


# Фильтр по цене. На вход подается Notebooks, список значений
def filter_by_price(dct, lst_srch):
    new_dct = {}
    index = 0
    price_begin, price_end = lst_srch[1], lst_srch[2]
    for i in dct.values():
        if (i['Price_euros'] >= price_begin) and (i["Price_euros"] <= price_end):
            new_dct[index] = i
            index += 1
    return new_dct


# Преобразует словарь словарей Notebooks в список строк,
# каждая строка в списке соответсвует строке в исходной таблице.
# Вспомогательная функция для Tkinter
def strings(dct):
    lst = []
    for i in dct.values():
        i['Inches'] = str(i['Inches'])
        i['Price_euros'] = str(i['Inches'])
        a = ' '.join(i.values())
        lst.append(a)
    return lst


# функция возвращающая среднюю цену для характеристики
def aver_prices(notebooks, specification):
    avers = {}
    specs = unique_specifications(notebooks, specification)
    for spec in specs:
        price_values = [notebook["Price_euros"] for notebook in notebooks.values() if notebook[specification] == spec]
        avers[spec] = sum(price_values) / len(price_values)
    return avers


