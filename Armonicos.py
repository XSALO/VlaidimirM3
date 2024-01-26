import statistics 
n=int(input("ingrese los numeros que tiene la secuencia: "))
r=[]
for i in range(n):
    x= int(input(f"ingrese los numeros {i+1}"))
    r.append(x)
print(f"el resultado de la armonica es:{statistics.harmonic_mean(r)}")