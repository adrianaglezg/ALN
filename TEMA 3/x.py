x = [1 ,2 ,3, 4, 5, 6]

for i in range(len(x)):
    for j in range(len(x)):
        if j != i:
            pass

from sympy import symbols

x = symbols('x')

polinomio = x**2 + 3*x + 5

print(polinomio)

resultado = polinomio.subs(x, 2)  
print("Polinomio evaluado en x=2:", resultado)
