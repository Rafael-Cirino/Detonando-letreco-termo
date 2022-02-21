txt_open_read = open("Banco de palavras/palavras_termo.txt", "r", encoding="utf8")
txt_open_write = open("Banco de palavras/palavras_termo2.txt", "w", encoding="utf8")
list_words = txt_open_read.readlines()

for palavra in list_words:
    c = list_words.count(palavra)
    if c > 1:
        for i in range(c - 1):
            id = list_words.index(palavra)
            del list_words[id]

for linha in list_words:
    txt_open_write.write(linha.lower())

print(len(list_words))

txt_open_write.close()
txt_open_read.close()