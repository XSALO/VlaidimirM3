import os 
os.system("cls")
# ax+b=0
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
if a == 0 :
    print(f"para la ecuacion {a}x+{b}=0 no hay solucion a la ecuacion")
elif a==0 and b ==0:
    print(f"para la ecuacion {a}x+{b}=0 no hay solucion unica")
if a != 0:
    x = (-b/a)
    print(f"para la ecuacion {a}x+{b}=0 la respuesta es x={x}")
    
    