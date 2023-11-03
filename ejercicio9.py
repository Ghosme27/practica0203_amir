palabra=input('introduzca una palabra:')
vocales=['a','e','i','o','u']
contador=0*len(vocales)
for i in palabra:
    if i==len(vocales):
        contador +=1
print('la palabra',palabra,'aparecen estas vocales estas veces',contador)
