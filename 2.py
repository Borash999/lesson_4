# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление

def hashable_dicts(**kwargs):
    equipment = dict()
    for a, b in kwargs.items():
        if isinstance(b, (list, dict, set, bytearray)):
            b = str(b)
        equipment[b] = a
    return equipment
print(hashable_dicts(aircraft='f-16', helicopter={'k-52': 2, 'k-26': 3}, tank=['Leopard', 'Abrams', 't-14'],
                     bmp={'bmp-1', 'bmp-2'}))

