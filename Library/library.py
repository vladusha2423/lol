def import_lib(import_filename):
    """
    Функция для загрузки базы из файла
    Формальные переменные: import_filename - имя загружаемого файла, libfile - указатель на файл
    Возвращает: импортированную базу данных
    Автор: Ракина А.С. БИВ174
    """
    import pickle
    from tkinter.messagebox import showerror
    try:
        libfile = open(import_filename, 'rb')
    except:
        showerror(title='Ошибка!', message="Файл не найден!")
    else:
        lib = pickle.load(libfile)
        libfile.close()
    return lib

def fetch_record(base, fieldnames, entries):
    """
    Функция для сбора информации о записи по ключу
    Формальные переменные: base - словарь, база данных;
    fieldnames - кортеж кортежей, первый элемент кортежа - название поля, второй элемент - соответствующее ему русское название;
    entries - словарь входных значений;
    key – значение из поля для строки, record – словарь с информацией по запрашиваемой книге
    Возвращает: -
    Автор: Поздняков Филипп БИВ174
    """
    from tkinter import END
    from tkinter.messagebox import showerror
    key = entries['Ключ'].get()
    try:
        record = base[key]
    except:
        showerror(title='Ошибка', message='Неправильный ключ!')
    else:
        for field in fieldnames:
            entries[field[1]].delete(0, END)
            entries[field[1]].insert(0, record[field[0]])
