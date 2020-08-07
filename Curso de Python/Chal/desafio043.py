p = float(input('Informe seu peso: '))
a = float(input('Informe sua altura: '))
imc = p/(a**2)
if imc < 18.5:
    print('O seu IMC é {:.2f}, você está \033[34mabaixo do peso.\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('O seu IMC é {:.2f}, você está no \033[31mpeso ideal.\033[m'.format(imc))
elif 25 <= imc < 30:
    print('O seu IMC é {:.2f}, você está com \033[32msobrepeso.\033[m'.format(imc))
elif 30 <= imc < 40:
    print('O seu IMC é {:.2f}, você está com \033[35mobesidade.\033[m'.format(imc))
else:
    print('O seu IMC é {:.2f}, você está com \033[36mobesidade morbida.\033[m'.format(imc))