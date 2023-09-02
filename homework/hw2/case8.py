def sort_chemical_elements(chemical_elements: list) -> list:
    # sorted(chemical_elements, key=lambda element: element[1])
    # почему выделяет return (если использовать конструкцию выше, то не выделяет)? Вроде же список возвращает
    return chemical_elements.sort(key=lambda element: element[1])


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(sort_chemical_elements(elements))
