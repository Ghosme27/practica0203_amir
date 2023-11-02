asignaturas=['Fisica','Quimica','Lengua','Historia','Matematicas']
notas=[]
print(asignaturas)
while True:
    a=(input('Introduzca sus notas en el orden de la lista que vio antes y cuando acabe ponga fin:'))
    if a=='fin':
        break
    notas.append(a)
asignatura_nota=list(zip(asignaturas,notas))
for asignaturas, notas in asignatura_nota:
    print('Esta es tu nota',notas,'en',asignaturas)