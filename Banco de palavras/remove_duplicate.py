import json

txt_open_read = open("Banco de palavras/palavras_s_acento.txt", "r", encoding="utf8")
txt_open_write = open("Banco de palavras/palavras_final.txt", "w", encoding="utf8")
list_words = txt_open_read.readlines()
list_json = []

for palavra in list_words:
    c = list_words.count(palavra)
    if c > 1:
        for i in range(c - 1):
            id = list_words.index(palavra)
            del list_words[id]

for linha in list_words:
    list_json.append(linha.replace("\n", "").lower())
    txt_open_write.write(linha.lower())

print(len(list_words))

with open('Banco de palavras/json_words2.json', 'w') as outfile:
    json.dump(list_json, outfile)

txt_open_write.close()
txt_open_read.close()