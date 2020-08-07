#print(x)#exceção -> NameErro
#n = int(input('Número: '))#exceção -> ValueError se digitar string
#print(f'Você digitou o número {n}')
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))#exceção->ZeroDivisionError - não pode ser 0
    r = a / b
#except Exception as erro:
    #print('Infelizmente tivemos um problema:(')
    #print(f'O Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

