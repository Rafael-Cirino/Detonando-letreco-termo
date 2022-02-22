import random
from termo_func import *


def termo_jogo(modo):
    # Jogo do termo, podendo ser de forma automatica ou manual

    # palavra a ser descoberta
    word_termo, list_words = word_br()

    # print(word_termo)

    tentativa = 0
    # Isso precisa iniciar antes do while
    word_parcial = "01234"
    list_block, list_in, list_in_id = [], [], []

    if modo == "aut_estat":
        while tentativa != 7:
            if not(list_words):
                return [False, entrada, tentativa]
                
            entrada = random.choice(list_words)  # valid_entrada(list_words)

            if entrada == word_termo:
                return [True, entrada, tentativa]
            tentativa += 1

            # Comparando palavras
            for i, letra in enumerate(entrada):
                letra_in = f"{letra}:{i}"
                if letra == word_termo[i]:
                    word_parcial = word_parcial.replace(str(i), letra)
                elif (letra in word_termo) and (letra_in not in list_in_id):
                    list_in_id.append(letra_in)
                    if letra not in list_in:
                        list_in.append(letra)
                elif (letra not in word_termo) and (letra not in list_block):
                    list_block.append(letra)

            list_words.remove(entrada)
            list_words = found_word(
                word_parcial, list_in, list_in_id, list_block, list_words
            )

        # [Se acertou, palavra termo, numero de tentativas]
        return [False, entrada, tentativa]
    elif modo == "detonado":
        list_words = found_word(
            word_parcial, list_in, list_in_id, list_block, list_words
        )


if __name__ == "__main__":
    rodadas = 10000
    tx_sucesso, tentativa_sucesso = 0, 0
    for i in range(rodadas):
        resultado = termo_jogo("aut_estat")

        if resultado[0]:
            # print(f"{i}: {resultado[1]} -> palavra encontrada com {resultado[2]}")
            tx_sucesso += 1
            tentativa_sucesso += resultado[2]
        else:
            print(f"{i}: {resultado[1]} -> palavra não encontrada: {resultado[2]}\n")

    print(f"\nMédia de sucesso: {(tx_sucesso/rodadas)*100} %")
    print(f"Média de tentativa: {tentativa_sucesso/tx_sucesso}")
