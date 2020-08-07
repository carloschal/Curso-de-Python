nome = str(input('Qual é seu nome? '))
if nome =='Carlos':
    print('\033[33mQue nome bonito!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\033[35mseu nome é popular no Brasil\033[m')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('\033[34mBelo nome feminino!\033[m')
else:
    print('\033[36mSeu nome é bem normal.\033[m')
print('\033[7;33mTenha um bom dia, {}\033[m'.format(nome))