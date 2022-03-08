import random
import regex


def word_br():
    """[Gera uma lista com todas as palavras de 5 letras da lingua pt-br]

    Returns:
        [string] -- [palavra escolhida aleatóriamente na lista]
        [list] -- [lista com todas as palavras de 5 letras da lingua pt-br]
    """
    txt_open_read = open("Banco de palavras/palavras_final.txt", "r", encoding="utf8")
    list_words = txt_open_read.readlines()

    # Removendo os "\n"
    for i, word in enumerate(list_words):
        list_words[i] = word.replace("\n", "")

    # Palavra a ser descoberta
    word_random = random.choice(list_words)
    # list_words.remove(word_random)

    return word_random, list_words


def valid_entrada(list_words):
    """[Valida a entrada fornecida pelo usuário]

    Arguments:
        list_words {[list]} -- [lista com todas as palavras de 5 letras da lingua pt-br]

    Returns:
        [string] -- [palavra escolhida]
    """

    # Validação da entrada
    entrada = input("Digite uma palavra com 5 letras: ")
    while True:
        if not (len(entrada) == 5):
            print("DIGITE UMA PALAVRA COM 5 LETRAS")
        elif entrada not in list_words:
            print("PALAVRA INEXISTENTE")
        else:
            break

        entrada = input("Digite novamente uma palavra com 5 letras: ")

    return entrada


def regex_list(w_regex, list_words):

    r = regex.compile(w_regex)
    list_words = list(filter(r.search, list_words))

    return list_words


def create_regex_or(list_or, condition):

    if condition == "or":
        # Or
        word_regex_in = f"("
        for i, letra in enumerate(list_or):
            if i == (len(list_or) - 1):
                word_regex_in += f"{letra})"
                break

            word_regex_in += f"{letra}|"
    else:
        # AND (?=.*p)(?=.*o)
        word_regex_in = f""
        for i, letra in enumerate(list_or):
            word_regex_in += f"(?=.*{letra})"

    return word_regex_in


def found_word(word_parcial, list_in, list_in_id, list_block, list_words):

    # Gerando a regex
    word_regex = ""
    for letra in word_parcial:
        if letra.isdigit():
            word_regex += "[a-z]{1}"
        else:
            word_regex += letra

    # Removendo conforme letras com posições definidas
    list_words = regex_list(word_regex, list_words)

    # Removendo conforme letras sem posição definidas
    if list_in:
        word_regex_in = create_regex_or(list_in, "and")
        list_words = regex_list(word_regex_in, list_words)

        list_remove = []
        for letra in list_in_id:
            aux = letra.split(":")
            for palavra in list_words:
                if aux[0] in palavra:
                    for i, l in enumerate(palavra):
                        if (l == aux[0]) and (i == int(aux[1])):
                            list_remove.append(palavra)
                            break

        for palavra_e in list_remove:
            if palavra_e in list_words:
                list_words.remove(palavra_e)

    # Removendo conforme letras que não fazem parte
    if list_block:
        word_regex_block = create_regex_or(list_block, "or")
        list_words_block = regex_list(word_regex_block, list_words)

        for palavra_remove in list_words_block:
            list_words.remove(palavra_remove)

    return list_words