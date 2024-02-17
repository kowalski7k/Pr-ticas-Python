from time import sleep

alunos = {}

while True:
    print("1) Adicionar alunos; \n2) Ver alunos \n3) Ranking de notas \n4) Sair")

    opcao = int(input(">>> "))

    if opcao == 1:
        print("Gerenciador de notas:")
        while True:
            nota = int(input("Digite a nota do aluno: "))
            nome = input("Digite o nome do aluno: ")
            alunos[nome] = nota

            continuar = input("Continuar? (S/N): ").lower()
            if continuar == "s":
                continue
            else:
                break

    elif opcao == 2:
        print("Alunos:")
        for k in alunos.keys():
            print(f"{k}")

    elif opcao == 3:
        posicao = 1
        print("Ranking dos alunos:")

        for k, i in dict(sorted(alunos.items(), key=lambda item: item[1])).items():
            sleep(posicao)
            print(f"{k} - {i}")
            posicao += 1
            sleep(posicao * 2)

    elif opcao == 4:
        break

    else:
        print("Opção inválida")
