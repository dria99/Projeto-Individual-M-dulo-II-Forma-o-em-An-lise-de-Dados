candidatos_list = []

class Candidato:
    def __init__(self, numero_cand, entrevista, teste_teorico, teste_pratico, av_softskill):
        self.numero_cand = int(numero_cand)
        self.entrevista = float(entrevista)
        self.teste_teorico = float(teste_teorico)
        self.teste_pratico = float(teste_pratico)
        self.av_softskill = float(av_softskill)

    def armazenar_candidato(self):
        numero_cand = int(input("Digite o número do Candidato: "))
        entrevista = float(input("Digite a nota mínima da Entrevista: "))
        teste_teorico = float(input("Digite a nota mínima do Teste teórico: "))
        teste_pratico = float(input("Digite a nota mínima do Teste prático: "))
        av_softskill = float(input("Digite a nota mínima na Avaliação de Soft Skill's: "))
        candidato = [numero_cand, entrevista, teste_teorico, teste_pratico, av_softskill]
        candidatos_list.append(candidato)
        return candidatos_list

    def buscar_candidato(self, entrevista, teste_teorico, teste_pratico, av_softskill):
        candidatos_atendem = []
        for candidato in candidatos_list:
            if (candidato[1] >= entrevista and
                candidato[2] >= teste_teorico and
                candidato[3] >= teste_pratico and
                candidato[4] >= av_softskill):
                candidatos_atendem.append(candidato)
        if candidatos_atendem:
            print("Os candidatos que atendem aos critérios são:")
            for candidato in candidatos_atendem:
                print(f"Número do Candidato: {candidato[0]}")
        else:
            print("Nenhum candidato atende aos critérios especificados.")

while True:
    print("Olá colaborador! Seja bem vindo à tela de filtro de candidatos.")
    print("Por favor, selecione o que deseja fazer no momento: ")
    print("1 - Buscar candidato")
    print("2 - Armazenar candidato")
    print("3 - Sair")

    opcao = input("Digite o número da sua opção: ")

    if opcao == "1":
        entrevista = float(input("Digite a nota mínima da Entrevista: "))
        teste_teorico = float(input("Digite a nota mínima do Teste teórico: "))
        teste_pratico = float(input("Digite a nota mínima do Teste prático: "))
        av_softskill = float(input("Digite a nota mínima na Avaliação de Soft Skill's: "))
        candidato = Candidato(0, entrevista, teste_teorico, teste_pratico, av_softskill)
        candidato.buscar_candidato(entrevista, teste_teorico, teste_pratico, av_softskill)
    elif opcao == "2":
        candidato = Candidato(0, 0, 0, 0, 0)
        candidato.armazenar_candidato()
        opcao2 = input("Candidato armazenado com sucesso! Deseja continuar? (S/N): ")
        if opcao2 != "S" or "s" or "sim" or "SIM" or "Sim":
            print("Saindo... Até logo!")
            break
    elif opcao == "3":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")