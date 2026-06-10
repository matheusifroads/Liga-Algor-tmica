"""
Liga de Algoritmos — 1ª Rodada — 08-06-2026
IFRO Campus Ariquemes — Tecnólogo em ADS — 1º período
Disciplina: Algoritmos e Lógica de Programação
Equipe: [Equipe 7]
Integrantes: [Matheus Teles de Andrade, Kelwin Eduardo Rodrigues dos Reis, João Gabriel Gomes de Brito, Matheus Henrique Xavier Ferreira]
Categoria: [Livre de Impacto Regional]
Desafio escolhido: [B]

"""

dias_semana = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")
cadastro = {"Setor 01":{'comum':["seg", "qua", "sex"], 'reciclavel':["ter"]},
            "Setor 02":{'comum':["ter", "qui", "sab"], 'reciclavel':["sex"]},
            "Setor 03":{'comum':["seg", "qua", "sex"], 'reciclavel':["qui"]},}

def setor_existe(setor):
    if setor in cadastro:
        print("Setor existe.")
        return True
    else:
        print("Setor não existe.")
        return False

def consultar_dia(setor, dia):

    encontrou = setor_existe(setor)
    
    for tipo_lixo, lista_dias in cadastro[setor].items():
        
        if dia in lista_dias:
            return f"{dia} tem coleta de lixo {tipo_lixo}"
            encontrou = True
            
    if not encontrou:
        "O Setor não tem coleta neste dia."

def dia_valido(dia):
    if dia in dias_semana:
        print("Dia válido")
        return True
    else:
        print("Dia não é válido")
        return False

def calendario_do_setor(setor):
    print(f'A semana do {setor}:', cadastro[setor])
    
def imprimir_calendario(setor):

    if setor not in cadastro:
        print(f"Erro: O setor '{setor}' não foi encontrado no cadastro.")
        return

    print(f"\n=========================================")
    print(f"       CRONOGRAMA DE COLETA: {setor.upper()}   ")
    print(f"=========================================")
    

    dados_setor = cadastro[setor]
    

    for dia in dias_semana:
        tipos_coleta = []
        

        for tipo_lixo, lista_dias in dados_setor.items():
            if dia in lista_dias:
                tipos_coleta.append(tipo_lixo)
        
 
        dia_formatado = dia.capitalize()
        if tipos_coleta:

            status_coleta = " + ".join(tipos_coleta)
            print(f"{dia_formatado}: [ {status_coleta} ]")
        else:
            print(f"{dia_formatado}: Sem coleta")
            
    print(f"=========================================\n")

def setores_no_dia(dia):
    dia = dia.lower()
    
    if dia not in dias_semana:
        print(f"Erro: '{dia}' não é um dia da semana válido.")
        return []
        
    setores_atendidos = []
    
    for setor, agendamento in cadastro.items():
        for lista_dias in agendamento.values():
            if dia in lista_dias:
                setores_atendidos.append(setor)
                break
                
    return setores_atendidos
