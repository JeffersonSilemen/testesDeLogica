number = int(input('Insira o número que deseja encontrar:'))
def  fib(number):
    i = 1;
    fibonacci = [0, 1];
    while (fibonacci[i] <= number):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i]);
        i = i + 1; 
    if number in fibonacci:
        print ('O número pertence a sequência de fibonacci');
        print(fibonacci);
    else:
        print ('O número NÃO pertence a sequência de fibonacci');
        print(fibonacci);

fib(number)