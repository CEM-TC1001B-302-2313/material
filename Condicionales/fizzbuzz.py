# Ingresar un número entero n
# si n es divisible entre 3 -> Fizz
# si n es divisible entre 5 -> Buzz
# si n es divisible entre 3 y entre 5 -> FizzBuzz
# si n no es divisible ni entre 3 ni entre 5 -> n
n = int(input("Ingrese el valor de n: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)