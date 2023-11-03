numeros=[]
while True:
    a=input('Dime los numeros ganadores de la loteria,cuando acabe ponga fin:')
    if a=='fin':
        break
    numeros.append(a)
numeros.sort()
for i in numeros:
    print('los numeros ganadores son',i)
