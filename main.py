from tkinter import *
from matplotlib.pyplot import text
from functools import partial
from termo_func import *

import random
import json

# Inicializador
master = Tk()
list_button = []
tentativa = 0
word_parcial = "01234"
list_block, list_in, list_in_id, list_words = [], [], [], []


def create_label():
    with open("labels.json", "r") as read_file:
        dict_label = json.load(read_file)

    for key in dict_label:
        cr_label = Label(frame_title)
        for atribute in dict_label[key]:
            cr_label[atribute] = dict_label[key][atribute]

        cr_label.pack()


def create_box():
    i = 0
    for cy in range(10, 490, 80):
        list_partial = []
        j = 0
        for cx in range(50, 520, 104):
            b_object = Button(
                frame_box,
                text="",
                width=6,
                height=3,
                bd=5,
                relief="groove",
                command=partial(bt_click, i, j),
            )
            b_object.place(x=cx, y=cy)

            list_partial.append(b_object)
            j += 1
        list_button.append(list_partial)
        i += 1


def bt_click(i, j):
    if list_button[i][j]["bg"] == "yellow":
        list_button[i][j]["bg"] = "green"
    elif list_button[i][j]["bg"] == "green":
        list_button[i][j]["bg"] = "SystemButtonFace"
    else:
        list_button[i][j]["bg"] = "yellow"


def write_interface(entrada, step=0):
    for j, letra in enumerate(entrada):
        list_button[tentativa - step][j]["text"] = letra.upper()


def change_word():
    entrada = random.choice(list_words)
    write_interface(entrada, step=1)


def termo_detonado():
    global tentativa
    global word_parcial, list_in, list_block, list_words, list_in_id

    if tentativa == 0:
        write_interface("barco")

        word_termo, list_words = word_br()
    elif tentativa < 6:
        for j in range(5):
            letra = list_button[tentativa - 1][j]["text"].lower()
            cor = list_button[tentativa - 1][j]["bg"]

            letra_in = f"{letra}:{j}"
            if cor == "green":
                word_parcial = word_parcial.replace(str(j), letra)
            elif (
                (cor == "yellow")
                and (letra_in not in list_in_id)
                and (letra not in word_parcial)
            ):
                list_in_id.append(letra_in)

                if letra not in list_in:
                    list_in.append(letra)
            elif (
                (cor == "SystemButtonFace")
                and (letra not in list_block)
                and (letra not in word_parcial)
                and (letra not in list_in)
            ):
                list_block.append(letra)

        list_words = found_word(
            word_parcial, list_in, list_in_id, list_block, list_words
        )

        if not (list_words):
            # Colocar depois um código pra zerar o programa
            print("CHEGOU NA PALAVRA OU ELA NÃO EXISTE")
            b_enter1["state"] = "disable"

            return

        entrada = random.choice(list_words)
        write_interface(entrada)
        list_words.remove(entrada)

        for j, letra in enumerate(entrada):
            list_button[tentativa - 1][j]["state"] = "disable"
        print(len(list_words))
    else:
        b_enter1["state"] = "disable"
        print(tentativa)
        print(list_words)

    # Apresenta a quantidade de palavras restantes no banco de dadoss
    if len(list_words) < 6:
        l_cword["text"] = f"Banco de palavras: {list_words}"
    else:
        l_cword["text"] = f"Banco de palavras: {len(list_words)}"

    tentativa += 1


if __name__ == "__main__":
    title = "Detonando term.ooo"
    master.title(title)
    master.geometry("560x690+800+2")  # Defini tamanho e localização da janela
    master.resizable(True, True)  # Não permite redimensionar
    master.iconbitmap("Image/bomb.ico")  # colocar icone
    master["bg"] = "#6E5C62"

    frame_title = Frame(master, height=100, bg="#6E5C62")
    frame_title.pack(fill=X)

    frame_box = Frame(master, height=480, bg="#6E5C62")
    frame_box.pack(fill=X)

    frame_enter = Frame(master, height=150, bg="#6E5C62")
    frame_enter.pack(fill=X)

    create_label()
    create_box()

    b_enter1 = Button(
        frame_enter, text="Enter", width=8, height=3, command=lambda: termo_detonado()
    )
    b_enter1.place(x=250, y=50)

    b_troca = Button(
        frame_enter,
        text="Trocar palavra",
        width=12,
        height=3,
        command=lambda: change_word(),
    )
    b_troca.place(x=100, y=50)

    l_cword = Label(frame_enter, text="", bg="#6E5C62", width=50, height=1)
    l_cword.place(x=100, y=10)

    master.mainloop()