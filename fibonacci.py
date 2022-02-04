

# Funcion Python que retorna una lista de fibonacci

def fibonacci(n, lista=[0,1]):
        if n == 0:
            return lista
        if n == 1:
            return lista
        if len(lista) < 2:
            return fibonacci(n-1, lista + [1])

        return fibonacci(n-1, lista + [lista[-1] + lista[-2]])

print(fibonacci(10))