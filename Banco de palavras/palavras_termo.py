import unidecode
import unicodedata

txt_open_read = open("Banco de palavras/banco_usp.txt", "r", encoding="utf8")
txt_open_write = open("Banco de palavras/palavras_s_acento.txt", "w", encoding="utf8")

for linha in txt_open_read:
    linha = linha.replace("\n", "")
    linha = unidecode.unidecode(linha)
    # linha = linha.encode("ascii", "ignore")
    # linha = linha.decode("utf-8")

    if not (("." in linha) or ("-" in linha)):
        if len(linha) == 5:
            txt_open_write.write(linha.lower() + "\n")

txt_open_write.close()
txt_open_read.close()

# zool.
