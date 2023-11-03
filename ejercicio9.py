palabra=input('introduzca una palabra:')
vocales=['a','e','i','o','u']
contador=[0]*len(vocales)
for i in palabra:
    if i==len(vocales):
        contador[len(vocales)] +=1
print('la palabra',palabra,'de todas estas vocales',vocales,'aparece este numero de veces',contador)
