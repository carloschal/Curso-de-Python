def notas(*n, sit=False):
    """
    ->  Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valos opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa principal
resp = notas(4, 5.5, 9, 6.5, sit=True)
print(resp)
help(notas)
