def Palindromos (texto):
    textoes= texto.replace(" ", "")
    textoes == textoes[::-1]
    
palabra= input("ingrese la palabra a verificar: ")
if Palindromos(palabra):
    print(f"la palabra {palabra} es un palindromo")
else:
    print(f"la palabra {palabra} no es un palindromo")
    
