"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""
from collections import Counter

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
        data = [line.replace("\n", "") for line in data]
        data_list = [line.split("\t") for line in data]
        data_con = [int(x[1]) for x in data_list]
        rta_1= sum(data_con)
    
    return rta_1


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from collections import Counter
    with open("data.csv", "r") as file:
        data = file.readlines()
        data = [line.replace("\n", "") for line in data]
        data_list = [line.split("\t") for line in data]
        data_tuple = [str(x[0]) for x in data_list]
        rta_2= sorted(Counter(data_tuple).most_common())
    return rta_2



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    from itertools import groupby
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
        data = [line.replace("\n", "") for line in data]
        data_list = [line.split("\t") for line in data]
        data_2 = [str(x[0:3]) for x in data]
        data_3 = [line.split("\t") for line in data_2]
        data_4 = [[x, int(n)] for x, n in data_3]

    summary_list = []
    for name, group in groupby(sorted(data_4), key=itemgetter(0)): 
       summary_list.append([name, sum(item[1] for item in group)])
    rta_3 = [tuple(l) for l in summary_list]
    return rta_3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter 
    with open("data.csv", "r") as file:
        data = file.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        data = [row[2] for row in data]
        data = [row.split("-") for row in data]
        data = [row[1] for row in data] 
        rta = Counter(data)
        rta_4 = list(rta.items())
        rta_4.sort(reverse = False)
    return rta_4



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    with open("data.csv", "r") as file:
        data = file.readlines()  
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        data = [row[0:2] for row in data]
        data = [(row[0], int(row[1])) for row in data] 
        rta_5 =[(k, max([y for (x,y) in data if x == k]), min([y for (x,y) in data if x == k])) for k in dict(data).keys()]
        rta_5.sort(reverse=False)
    return rta_5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    with open("data.csv", "r") as file:
        data = file.readlines()  
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        data = [row[3:] for row in data]
        
        col5 = []
        for index, element in enumerate (data):
            list5 = []
            for indice, fila in enumerate (element):
                if len(fila) > 1:
                    list5.append(fila)
            col5.append(list5)
        
        lista = []
        for index, element in enumerate (col5):
            lista.extend(element)
        
        lista = [(row[:3], int(row[4:])) for row in lista]
        rta_6 =[(k, min([y for (x,y) in lista if x == k]), max([y for (x,y) in lista if x == k])) for k in dict(lista).keys()]
        rta_6.sort(reverse = False) 
    return rta_6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as file:
        data = file.readlines()
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        data = [row[0:2] for row in data]
        data = [(int(row[1]), row[0]) for row in data] 
        
        counter = {}
        for key, value in data:
            if key in counter:       
                counter[key] += [value]
            else:
                counter[key] = [value]
        
        rta_7 = [(key, counter[key]) for key in counter]
        rta_7.sort(reverse = False)
    return rta_7



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    with open("data.csv", "r") as file:
        data = file.readlines()
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]   
        data = [row[0:2] for row in data]
        data = [(int(row[1]), row[0]) for row in data] 
        
        counter = {}
        for key, value in data:
            if key in counter:       
                counter[key] += [value]
            else:
                counter[key] = [value]
        
        rta_8 = [(key, counter[key]) for key in counter]
        rta_8 = [(row[0], list(set(row[1]))) for row in rta_8] 
        rta_8 = [(row[0], sorted(row[1])) for row in rta_8]     
        rta_8.sort(reverse = False)
    return rta_8

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    with open("data.csv", "r") as file:
        data = file.readlines()        
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        data = [row[3:] for row in data]
        
        col5 = []
        for index, element in enumerate (data):
            list5 = []
            for indice, fila in enumerate (element):
                if len(fila) > 1:
                    list5.append(fila)
            col5.append(list5)
        
            lista = []
            for index, element in enumerate (col5):
                lista.extend(element)
            
            #lista = [(row[:3], int(row[4:])) for row in lista]
            lista = [row.replace(":", ",") for row in lista]    
            lista = [row.split(',') for row in lista]  
            lista = [(row[0], (int(row[1]))) for row in lista] 

            counter = {}
            for key, value in lista:
                    if key in counter:       
                        counter[key] += 1
                    else:
                        counter[key] = 1

            rta = list(counter.items())
            rta.sort(reverse = False)
            rta_9 = dict (rta)
    return rta_9




def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as file:
        data = file.readlines()
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        col1 = [row[0] for row in data]  
        data = [row[3:] for row in data]

        col4 = []
        colm5 = []
        for index, element in enumerate (data):
            lista4 = []
            lista5 = []
            for indice, fila in enumerate (element):
                if len(fila) > 1:
                    lista5.append(fila)
                if len(fila) == 1:
                    lista4.append(fila)
            col4.append(lista4)
            colm5.append(lista5)
        
        col4 = [len(row) for row in col4]  
        colm5 = [len(row) for row in colm5]

        rta_10 =[]
        for index, element in enumerate (col1):
            rta_10.append((str(element), col4[index], colm5[index]))

    return rta_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", "r") as file:
        data = file.readlines()        
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        col2 = [row[1] for row in data]  
        data = [row[3:] for row in data]

        col4 = []
        for index, element in enumerate (data):
            lista4 = []
            for indice, fila in enumerate (element):
                if len(fila) == 1:
                    lista4.append(fila)
            col4.append(lista4)

        lista = []
        for index, element in enumerate (col4):
            lista.extend(element)

        clave = set(lista)
        clave = sorted(clave)

        rta_11 = {}
        for ind_clave, elem_clave in enumerate (clave): 
            for ind_c4, elem_c4 in enumerate(col4):
                if elem_clave in elem_c4:
                    if elem_clave in rta_11:
                        rta_11[elem_clave] += int(col2[ind_c4])
                    else: 
                        rta_11[elem_clave] = int(col2[ind_c4])

    return rta_11



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as file:
        data = file.readlines()        
        data = [row.replace("\n", "") for row in data]
        data = [row.replace("\t", ",") for row in data]
        data = [row.split(",") for row in data]
        col1= [row[0] for row in data]  
        data = [row[3:] for row in data]

        col5 = []
        for index, element in enumerate (data):
            lista5 = []
            for indice, fila in enumerate (element):
                if len(fila) > 1:
                    lista5.append(fila)
            col5.append(lista5)

        count_col5 = [[int(e[4:]) for e in row] for row in col5]
        count_col5 = [sum(row) for row in count_col5] 

        lista =[]
        for index, element in enumerate (col1):
            lista.append((str(element), count_col5[index]))
                    
        rta_12 = {}
        for key, value in lista:
            if key in rta_12:       
                rta_12[key] += value
            else:
                rta_12[key] = value        
            
        rta_12 = list(rta_12.items())
        rta_12.sort(reverse = False)
        rta_12 = dict (rta_12)

    return rta_12