class ParesChiquitos():
    
    def __init__(self):
        self.par = 0

    def __iter__(self):
        self.par = 0
        return self

    def __next__(self):
        self.par += 2
        if self.par > 10:
            raise StopIteration
        return self.par
    

# Funciones Generadoras (clausula yield)

def paresChiquitos():
    par = 0
    while True:
        par += 2
        if par > 10:
            # Return en funcion generadora es igual a stop iteration
            return
        sent = (yield par)
        if sent is not None:
            par = sent

# Funciones Anonimas (no tiene nombre)
lambda a, b : a + b

# Suma dos numeros
def suma(a,b):
    return a + b


