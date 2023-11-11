class MiClase:
    def __init__(self, Valencia, Tempo, Tonos, listaCanciones, listaBailabilidad):
        self.Valencia = Valencia
        self.Tempo = Tempo
        self.Tonos = Tonos
        self.listaCanciones = listaCanciones
        self.listaBailabilidad = listaBailabilidad

    def ObtieneValencia(self, numero):
        # Convierte el número en una cadena para contar los dígitos impares
        numero_str = str(numero)
        digitos_impares = [int(digit) for digit in numero_str if int(digit) % 2 != 0]
        return len(digitos_impares)

    def DivisibleTempo(self, numero):
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        return divisores

    def ObtieneMasBailable(self, lista):
        if not lista:
            return None
        return max(lista)

    def VerificaListaCanciones(self, lista):
        if any(song is None for song in lista):
            return False
        return True
    
    def Encuentra(self, lista, elemento):
        if elemento in lista:
            return True
        return False
    
################################################################################################
#Ejemplo de ejecución
# Crear un objeto de la clase MiClase
objeto = MiClase(5, 120, 12, ["Snowman", "Jingle Bell Rock", "All I want for Christmas"], [0.8, 0.9, 0.7])
# Ejemplo de uso de los métodos
print(objeto.ObtieneValencia(1234567))  # Debería imprimir 4
print(objeto.DivisibleTempo(15))  # Debería imprimir [1, 2, 5, 10]
print(objeto.ObtieneMasBailable([0.1, 0.6, 0.4]))  # Debería imprimir 0.9
print(objeto.VerificaListaCanciones(["Like Flames", "Daylight", "Make Me Feel Better"]))  # Debería imprimir True