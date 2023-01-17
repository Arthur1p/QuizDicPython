quiz = {
    "questao1": {
        "questao" : "Qual a capital do Brasil? ",
        "resposta": "Brasilia"
    },
    "questao2":{
        "questao": "Quantos pauzinhos pra construir um barco? ",
        "resposta": "Muitos"
    },
    "questao3":{
        "questao": "Qual a formula magica da paz?",
        "resposta": "Dinheiro"
    }
}

pontos = 0

for key, value in quiz.items():
    print(value['questao'])
    resposta = input("Resposta: ")

    if resposta.lower() == value['resposta'].lower():
        print("Certa resposta!")
        pontos = pontos + 1
        print("Seus pontos são " + str(pontos))

    else:
        print("Errou!")
        print("A resposta é: " + value['resposta'])
        print("Seus pontos são " + str(pontos))

print("Voce acertou " + str(pontos) + " de 3 perguntas.")
print("Seu percentual de acerto é " + str(int(pontos/3 * 100)) + "%")