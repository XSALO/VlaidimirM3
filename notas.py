import statistics
n=int(input("ingrese la cantidad de notas "))
r=[]
for i in range(n):
    x= int(input(f"ingrese la nota {i+1}"))
    r.append(x)
print(f"el promedio de las notas es:  {statistics.mean(r)}")