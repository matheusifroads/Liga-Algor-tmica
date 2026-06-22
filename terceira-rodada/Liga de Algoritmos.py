"""
Liga de Algoritmos — 3ª Rodada — 15-06-2026
IFRO Campus Ariquemes — Tecnólogo em ADS — 1º período
Disciplina: Algoritmos e Lógica de Programação
Equipe: [Equipe 7]
Integrantes: [Matheus Teles de Andrade, Kelwin Eduardo Rodrigues dos Reis, João Gabriel Gomes de Brito, Matheus Henrique Xavier Ferreira]
Categoria: [Empresa e Comunidade]
Desafio escolhido: [3]
"""
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

segundos = 60
transacoes = [{'cliente': 'A', 'valor': 1, 'momento': 1},
              {'cliente': 'A', 'valor': 1, 'momento': 2},
              {'cliente': 'A', 'valor': 1, 'momento': 10},
              {'cliente': 'A', 'valor': 1, 'momento': 30},
              {'cliente': 'D', 'valor': 1, 'momento': 1},
              {'cliente': 'E', 'valor': 1, 'momento': 1},
              {'cliente': 'F', 'valor': 1, 'momento': 1},
              {'cliente': 'G', 'valor': 1, 'momento': 1},
              {'cliente': 'H', 'valor': 1, 'momento': 1},
              {'cliente': 'I', 'valor': 1, 'momento': 1},
              {'cliente': 'J', 'valor': 1, 'momento': 1}]

janelas = defaultdict(lambda: deque(maxlen=3))
for transacao in transacoes:
    janelas[transacao["cliente"]].append(transacao)
dicio_janelas = dict(janelas)

def registrar(tx, janelas):
    janelas[tx['cliente']].append(tx)
    return

def em_burst(cliente, janelas, segundos):
    for chave, transacoes in janelas.items():
        if cliente == chave:
            if transacoes[0]['momento'] - transacoes[2]['momento'] <= segundos:
                return True
    return False

'''
def clientes_em_burst(base, segundos):
    

def imprimir_alertas(base, segundos)
'''
resposta = ''

while resposta != 'sair':
    
    print("=========== Detecção de Transações em Rajada ===========")
    print("1. Registrar")
    print("2. Em Burst")
    print("3. Clientes em Burst")
    print("4. Imprimir Alertas")
    
    resposta = input("Digite o número de uma função ou 'sair' para encerrar: ")
    print("")
    
    if resposta == "1":
        print("== Registrar ==") 
        nova_transacao = {'cliente': input("Digite o nome do cliente: "),
                          'valor': float(input("Digite o valor da transação: ")),
                          'momento': int(input("Digite o momento da transação: "))}
        transacoes.append(registrar(nova_transacao, dicio_janelas))
        resposta = ''
        print('')
        
    elif resposta == "2":
        print("== Em Burst ==")
        print(em_burst(input("Digite o nome do cliente: "), dicio_janelas, segundos))
        resposta = ''
        print('')
        
    elif resposta == "3":
        print("== Clientes em Burst ==")
        resposta = ''
        print('')

    elif resposta == "4":
        print("== Imprimir Alertas ==")
        resposta = ''
        print('')
