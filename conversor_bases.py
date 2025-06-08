num = int(input('Digite um número: '))
base = int(input('Qual será a base da conversão: [ 1 = binario] [ 2 = octal] [ 3 = hexadecimal] ' ))

if base == 1:
    print(f'O número {num} em BINÁRIO É : {bin(num)[2:]}')
elif base == 2:
    print(f'O número {num} em OCTAL É : {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num} em HEXADECIMAL É : {hex(num)[2:]}')
else:
    print('A opção escolhida não está acessível!')




