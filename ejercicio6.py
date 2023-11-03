asignaturas=['Fisica','Quimica','Lengua','Historia','Matematicas']
notas=[]
nota_min=5
print(asignaturas)
while True:
    a=(input('Introduzca sus notas en el orden de la lista que vio antes y cuando acabe ponga fin:'))
    if a=='fin':
        break
    nota=int(a)
    notas.append(notas)
recuperar=[asignatura for asignatura in notas if nota>=nota_min]
for recuperar in recuperar:
    del notas[recuperar]
print('Tienes que recuperar',recuperar)