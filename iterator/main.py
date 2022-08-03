from time import sleep
from database import DbSimulator
from iterator import DatabaseIterable


def main():
    record_paginator = DatabaseIterable(DbSimulator(), "select * from person")

    # Em seguida podemos usar o for pra iterar
    # Nesse momento o ITERADOR é criado implicitamente
    for page in record_paginator:
        # faz algo com a pagina, que é uma lista de resultados
        for record in page:
            print(f"{record['name']} is {record['age']} years old")


def exercicio():
    list = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    ]
    itera = iter(list)
    for i in range(len(list)):
        a = next(itera)
        print(a)
        print(i)


exercicio()
sleep(1)
main()
