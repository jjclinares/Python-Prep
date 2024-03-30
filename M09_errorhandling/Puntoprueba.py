class Funciónes:
    def __init__(self,lista):
        self.lista=lista
#Definir si es valor Primo
    def verificar_primo(self,numero):
        es_primo =True
        for i in range(2,numero):
            if numero % i == 0:
                es_primo =False
                break
        return es_primo

#Definir la moda 
    def moda(self,lista):
        frecuencia = {}
        for n in lista:
            if n in frecuencia:
                frecuencia[n]+=1
            else:
                frecuencia[n]=1
        max_repeticiones = max( frecuencia.values())
        mas_repetidos =[n for n ,repeticiones in frecuencia.items() if repeticiones == max_repeticiones]
        return mas_repetidos[0],max_repeticiones

#Conversión de grados Celsius,Farenhein,Kelvin
    
    def Conversión_de_grados(self,Valor,Origen,destino):
        if Origen == "Celsius":
            if destino == "Celsius":
                valor_destino = Valor
            elif destino == "Farenheit":
                valor_destino = (Valor * 9/5)+ 32
            elif destino == "Kelvin":
                valor_destino = (Valor + 273.15)
            else:
                print('Parámetro de Destino incorrecto')
        elif Origen == "Farenheit":
            if destino == "Celsius":
                valor_destino = (Valor - 32)* 5/9
            elif destino == "Farenheit":
                valor_destino = Valor 
            elif destino == "Kelvin":
                valor_destino = ((Valor -32)* 5/9) +273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif Origen == "Kelvin":
            if destino == "Celsius":
                valor_destino = Valor -273.15
            elif destino == "Farenheit":
                valor_destino = ((Valor - 273.15)*9/5)+32 
            elif destino == "Kelvin":
                valor_destino = Valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print(f"El dato proporcionado no es una medida de Temperatura valida")
        return(valor_destino)
    
    #Factorial 
    def factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero