"""
Liga de Algoritmos — 2ª Rodada — 08-06-2026
IFRO Campus Ariquemes — Tecnólogo em ADS — 1º período
Disciplina: Algoritmos e Lógica de Programação
Equipe: [Equipe 7]
Integrantes: [Matheus Teles de Andrade, Kelwin Eduardo Rodrigues dos Reis, João Gabriel Gomes de Brito, Matheus Henrique Xavier Ferreira]
Categoria: [Livre de Impacto Regional]
Desafio escolhido: [B]
"""

media_aprovacao = 6.0

turma = [{'nome': "João", 'notas': [8, 7, 6, 10]},
         {'nome': "Matheus Teles", 'notas': [6, 6, 6, 6]},
         {'nome': "Matheus Henrique", 'notas': [5, 6, 3, 7]},
         {'nome': "Kelwin", 'notas': [10, 10, 10, 10]},
         {'nome': "Geraldo", 'notas': [10, 9, 8, 7]}]

def media_aluno(aluno):
    #achar nome na turma
    #pegar a nota desse aluno
    #fazer a media
    #imprimir a media
    
    global turma
    indice = 0
    for estudante in turma:
        if turma[indice]['nome'] == aluno:
            notas = estudante['notas']
        indice += 1
    media = sum(notas)/len(notas)
    return media
    
def aprovados(turma):
    aprovados = []
    for estudante in turma:
        nome = estudante['nome']
        media = media_aluno(nome)
        if media >= 6.0:
            aprovados.append(nome)
    return aprovados

def em_queda(aluno):
    global turma
    em_queda = False
    primeira = 0
    segunda = 0
    terceira = 0
    quarta = 0

    for estudante in turma:
        if estudante['nome'] == aluno:
            if estudante['notas'][0] > estudante['notas'][1] and estudante['notas'][1] > estudante['notas'][2] and estudante['notas'][2] > estudante['notas'][3]:
                em_queda = True

    return em_queda


def alunos_em_risco(turma):
    lista = []
    for estudante in turma:
        if em_queda(estudante['nome']):
            lista.append(estudante['nome'])
            
    return lista



def media_turma(turma):
    soma_media = 0
    for estudante in turma:
        soma_media += media_aluno(estudante['nome'])
    media_turma = soma_media / len(turma)
    
    return media_turma


def imprimir_boletim(turma):
    print(f"| NOME | N1 | N2 | N3 | N4 | MEDIA | SITUAÇÂO |")
    for estudante in turma:
        print(f"| [{estudante['nome']}] | {estudante['notas'][0]} | {estudante['notas'][1]} | {estudante['notas'][2]} | {estudante['notas'][3]} | {media_aluno(estudante['nome'])} | {'RISCO' if em_queda(estudante['nome']) else ' Cursando '} |")
    print("")
    print(f"Média da Turma: {media_turma(turma)}")
    return


resposta = ''

while resposta != 'sair':
    
    print("=========== Menu Escolar ===========")
    print("1. Média de Aluno")
    print("2. Lista de Aprovados")
    print("3. Em Queda")
    print("4. Alunos Em Risco")
    print("5. Média Turma")
    print("6. Imprimir Boletim")
    
    resposta = input("Digite o número de uma função ou 'sair' para encerrar: ")
    print("")
    
    if resposta == "1":
        print("== Média Aluno ==")
        result = media_aluno(input("Digite o nome de um aluno: "))
        print(result)
        resposta = ''
        print('')
        
    elif resposta == "2":
        print("== Lista de Aprovados ==")
        result = aprovados(turma)
        print(result)
        resposta = ''
        print('')
        
    elif resposta == "3":
        print("== Em Queda ==")
        result = em_queda(input("Digite o nome de um aluno: "))
        print(result)
        resposta = ''
        print('')

    elif resposta == "4":
        print("== Alunos Em Risco ==")
        result = alunos_em_risco(turma)
        print(result)
        resposta = ''
        print('')
        
    elif resposta == "5":
        print("== Média da Turma ==")
        result = media_turma(turma)
        print(result)
        resposta = ''
        print('')

    elif resposta == "6":
        print('')
        print("== Imprimir Boletim ==")
        imprimir_boletim(turma)
        resposta = ''
        print('')
        
        
