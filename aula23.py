# aula 23 - erros e excessoes

try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Problema com os tipos de dados')
except ZeroDivisionError:
    print('Problema de divisão por zero')
except KeyboardInterrupt:
    print('Execução do programa finalizada pelo usuario')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'o resultado é {r:.1f}')
finally:
    print('Programa finalizado.')

