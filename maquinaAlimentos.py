# Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011 en el campus Vitacura.

# Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10, $50 y $100.

# Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio del producto, el programa debe entregar las monedas de vuelto, una por una.

producto = {
    "A":270,
    "B":320,
    "C":390,
}
cont=0
print("Catalogo de Productos maquina expendedora.")
for i,val in enumerate.items(producto):
    cont += 1
    print(f"\t#{cont}{i}----------- ${val}" )
opc=int(input("seleccione el producto a adquirir.\n"))
plata= 0
i=(list(producto)[opc-1])
precio=producto.get(i)
while (plata<precio):
    
    print("insertar dinero")
    print("1. $10")
    print("2. $50")
    print("3. $100")
    moneda=int(input())
    match(moneda):
        case 1:
            plata = plata + 10
        case 2:
            plata = plata + 50
        case 3:
            plata = plata + 100
        case _:
            print("el monto no esta disponible")
    print(f"el producto{i} tiene un valor de ${val}el dinero ingresado es {plata}")
    
