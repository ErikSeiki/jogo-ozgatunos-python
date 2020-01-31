import pygame, time
from pygame import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYUP, K_SPACE
from random import randint
import os
from time import sleep
import zlib
import os


def Comprimir_Imagem(nome_imagemp):
    imagem_originalp = open(nome_imagemp, 'rb').read()
    compressaop = zlib.compress(imagem_originalp, zlib.Z_BEST_COMPRESSION)
    porcentagem_arquivo_comprimidop = (100 * len(compressaop)) / len(imagem_originalp)
    taxa_compressaop = 100 - porcentagem_arquivo_comprimidop

    print("A imagem {} original tem {} bytes, a imagem comprimida tem {} bytes, "
          "a compressão resulta em uma imagem {:.2f}% menor "
          .format(nome_imagemp, len(imagem_originalp), len(compressaop), float(taxa_compressaop)))
    return compressaop


def Descomprimir_Imagem(nome_imagemp):
    imagem_comprimidap = open(nome_imagemp, 'rb').read()
    descompressao = zlib.decompress(imagem_comprimidap)
    print("A imagem {} foi descomprimida".format(imagem_comprimidap))
    return descompressao


def Comprimir_Todas_Imagem():
    Roberval_Vivo_d_e_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des.png")
    Roberval_Vivo_f_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des.png")
    Roberval_Vivo_c_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des.png")
    Roberval_Vivo_d_e_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm.png")
    Roberval_Vivo_f_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm.png")
    Roberval_Vivo_c_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm.png")

    Roberson_Vivo_d_e_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des.png")
    Roberson_Vivo_f_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des.png")
    Roberson_Vivo_c_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des.png")
    Roberson_Vivo_d_e_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E.png")
    Roberson_Vivo_f_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F.png")
    Roberson_Vivo_c_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C.png")

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des_comp.png", 'wb') \
        .write(Roberval_Vivo_d_e_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des_comp.png", 'wb') \
        .write(Roberval_Vivo_f_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des_comp.png", 'wb') \
        .write(Roberval_Vivo_c_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm_comp.png", 'wb') \
        .write(Roberval_Vivo_d_e_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm_comp.png", 'wb') \
        .write(Roberval_Vivo_f_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm_comp.png", 'wb') \
        .write(Roberval_Vivo_c_Arm_comp)

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des_comp.png", 'wb') \
        .write(Roberson_Vivo_d_e_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des_comp.png", 'wb') \
        .write(Roberson_Vivo_f_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des_comp.png", 'wb') \
        .write(Roberson_Vivo_c_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Arm_comp.png", 'wb') \
        .write(Roberson_Vivo_d_e_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Arm_comp.png", 'wb') \
        .write(Roberson_Vivo_f_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Arm_comp.png", 'wb') \
        .write(Roberson_Vivo_c_Arm_comp)

    pasta = "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem"
    procura_imagem = os.listdir(pasta)

    for img in procura_imagem:
        if img == "Roberval_Vivo_D_E_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_F_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_C_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_D_E_Arm.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_F_Arm.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_C_Arm.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_D_E_Des_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_F_Des_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_C_Des_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_D_E_Arm_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_F_Arm_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_C_Arm_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))


def Descomprimir_Todas_Imagens():
    Roberval_Vivo_d_e_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des_comp.png")
    Roberval_Vivo_f_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des_comp.png")
    Roberval_Vivo_c_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des_comp.png")
    Roberval_Vivo_d_e_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm_comp.png")
    Roberval_Vivo_f_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm_comp.png")
    Roberval_Vivo_c_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm_comp.png")

    Roberson_Vivo_d_e_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des_comp.png")
    Roberson_Vivo_f_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des_comp.png")
    Roberson_Vivo_c_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des_comp.png")
    Roberson_Vivo_d_e_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Arm_comp.png")
    Roberson_Vivo_f_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Arm_comp.png")
    Roberson_Vivo_c_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Arm_comp.png")

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des.png", 'wb') \
        .write(Roberval_Vivo_d_e_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des.png", 'wb') \
        .write(Roberval_Vivo_f_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des.png", 'wb') \
        .write(Roberval_Vivo_c_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm.png", 'wb') \
        .write(Roberval_Vivo_d_e_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm.png", 'wb') \
        .write(Roberval_Vivo_f_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm.png", 'wb') \
        .write(Roberval_Vivo_c_Arm_descomp)

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des_Des.png", 'wb') \
        .write(Roberson_Vivo_d_e_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des_Des.png", 'wb') \
        .write(Roberson_Vivo_f_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des_Des.png", 'wb') \
        .write(Roberson_Vivo_c_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Arm_Des.png", 'wb') \
        .write(Roberson_Vivo_d_e_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Arm_Des.png", 'wb') \
        .write(Roberson_Vivo_f_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Arm_Des.png", 'wb') \
        .write(Roberson_Vivo_c_Arm_descomp)

    pasta = "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem"
    procura_imagem = os.listdir(pasta)

    for img in procura_imagem:
        if img == "Roberval_Vivo_D_E_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_F_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_C_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_D_E_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_F_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_C_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_D_E_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_F_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_C_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_D_E_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_F_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_C_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))


def Comprimir_Roberval_Imagem():
    Roberval_Vivo_d_e_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des.png")
    Roberval_Vivo_f_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des.png")
    Roberval_Vivo_c_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des.png")
    Roberval_Vivo_d_e_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm.png")
    Roberval_Vivo_f_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm.png")
    Roberval_Vivo_c_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm.png")

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des_comp.png", 'wb') \
        .write(Roberval_Vivo_d_e_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des_comp.png", 'wb') \
        .write(Roberval_Vivo_f_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des_comp.png", 'wb') \
        .write(Roberval_Vivo_c_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm_comp.png", 'wb') \
        .write(Roberval_Vivo_d_e_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm_comp.png", 'wb') \
        .write(Roberval_Vivo_f_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm_comp.png", 'wb') \
        .write(Roberval_Vivo_c_Arm_comp)

    pasta = "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem"
    procura_imagem = os.listdir(pasta)

    for img in procura_imagem:
        if img == "Roberval_Vivo_D_E_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_F_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_C_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_D_E_Arm.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_F_Arm.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberval_Vivo_C_Arm.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))


def Comprimir_Roberson_Imagem():
    Roberson_Vivo_d_e_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des.png")
    Roberson_Vivo_f_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des.png")
    Roberson_Vivo_c_Des_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des.png")
    Roberson_Vivo_d_e_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Arm.png")
    Roberson_Vivo_f_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Arm.png")
    Roberson_Vivo_c_Arm_comp = Comprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Arm.png")

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des_comp.png", 'wb') \
        .write(Roberson_Vivo_d_e_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des_comp.png", 'wb') \
        .write(Roberson_Vivo_f_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des_comp.png", 'wb') \
        .write(Roberson_Vivo_c_Des_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Arm_comp.png", 'wb') \
        .write(Roberson_Vivo_d_e_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Arm_comp.png", 'wb') \
        .write(Roberson_Vivo_f_Arm_comp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Arm_comp.png", 'wb') \
        .write(Roberson_Vivo_c_Arm_comp)

    pasta = "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem"
    procura_imagem = os.listdir(pasta)

    for img in procura_imagem:
        if img == "Roberson_Vivo_D_E_Des_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_F_Des_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_C_Des_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_D_E_Arm_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_F_Arm_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))
        elif img == "Roberson_Vivo_C_Arm_Des.png":
            os.remove('C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}'.format(img))


def Descomprimir_Roberval_Imagens():
    Roberval_Vivo_d_e_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des_comp.png")
    Roberval_Vivo_f_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des_comp.png")
    Roberval_Vivo_c_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des_comp.png")
    Roberval_Vivo_d_e_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm_comp.png")
    Roberval_Vivo_f_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm_comp.png")
    Roberval_Vivo_c_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm_comp.png")

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Des.png", 'wb') \
        .write(Roberval_Vivo_d_e_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Des.png", 'wb') \
        .write(Roberval_Vivo_f_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Des.png", 'wb') \
        .write(Roberval_Vivo_c_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_D_E_Arm.png", 'wb') \
        .write(Roberval_Vivo_d_e_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_F_Arm.png", 'wb') \
        .write(Roberval_Vivo_f_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberval_Vivo_C_Arm.png", 'wb') \
        .write(Roberval_Vivo_c_Arm_descomp)

    pasta = "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem"
    procura_imagem = os.listdir(pasta)

    for img in procura_imagem:
        if img == "Roberval_Vivo_D_E_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_F_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_C_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_D_E_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_F_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberval_Vivo_C_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))


def Descomprimir_Roberson_Imagens():
    Roberson_Vivo_d_e_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des_comp.png")
    Roberson_Vivo_f_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des_comp.png")
    Roberson_Vivo_c_Des_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des_comp.png")
    Roberson_Vivo_d_e_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Arm_comp.png")
    Roberson_Vivo_f_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Arm_comp.png")
    Roberson_Vivo_c_Arm_descomp = Descomprimir_Imagem(
        "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Arm_comp.png")

    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Des.png", 'wb') \
        .write(Roberson_Vivo_d_e_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Des.png", 'wb') \
        .write(Roberson_Vivo_f_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Des.png", 'wb') \
        .write(Roberson_Vivo_c_Des_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_D_E_Arm.png", 'wb') \
        .write(Roberson_Vivo_d_e_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_F_Arm.png", 'wb') \
        .write(Roberson_Vivo_f_Arm_descomp)
    open("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/Roberson_Vivo_C_Arm.png", 'wb') \
        .write(Roberson_Vivo_c_Arm_descomp)

    pasta = "C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem"
    procura_imagem = os.listdir(pasta)

    for img in procura_imagem:
        if img == "Roberson_Vivo_D_E_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_F_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_C_Des_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_D_E_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_F_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))
        elif img == "Roberson_Vivo_C_Arm_comp.png":
            os.remove("C:/Users/Erik Seiki/PycharmProjects/Smaug/Imagem/{}".format(img))


def Calcular_Menu(menu_opcoesp, fontep):
    global indice_menu
    for opcaop in menu_opcoesp:
        opcao_renderizadap = fontep.render(opcaop["text"], True, opcaop["cor"])
        opcaop["surface"] = opcao_renderizadap
        opcaop["rect"] = opcao_renderizadap.get_rect()
        opcaop["rect"].x = opcaop["pos"][0]
        opcaop["rect"].y = opcaop["pos"][1]
    if indice_menu < 0:
        indice_menu = 0

    if indice_menu >= len(menu_opcoesp):
        indice_menu = len(menu_opcoesp) - 1


def Menu_Escolha_Alternativa(tempo_pausadop):
    global status_questao, status_button, total_tempo_pausado, total_tempo_pausado2, tela_atual, indice_menu, status_numero_guarda, display, frase_acertou, frase_errou
    display.fill((0, 0, 0))
    if tela_atual == 2:
        if indice_menu == 1:
            status_numero_guarda = 0
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_acertou, (100, 300))
        else:
            status_numero_guarda = 1
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_errou, (170, 300))
    if tela_atual == 3:
        if indice_menu == 3:
            status_numero_guarda = 0
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_acertou, (100, 300))
        else:
            status_numero_guarda = 1
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_errou, (170, 300))
    if tela_atual == 4:
        if indice_menu == 2:
            status_numero_guarda = 0
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_acertou, (100, 300))
        else:
            status_numero_guarda = 1
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_errou, (170, 300))
    if tela_atual == 5:
        if indice_menu == 1:
            status_numero_guarda = 0
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_acertou, (100, 300))
        else:
            status_numero_guarda = 1
            pygame.draw.rect(display, cor["Preto"], (80, 300, 680, 100), 0)
            display.blit(frase_errou, (170, 300))
    pygame.display.update()
    porta_abrindo_som.play()
    sleep(1.5)
    porta_fechando_som.play()
    status_questao = 0
    status_button = 0

    total_tempo_pausado += tempo_pausadop
    total_tempo_pausado2 += tempo_pausadop


def Pintar_Menu(displayp, menu_opcoesp, corp):
    global indice_menu
    for opcaop in menu_opcoesp:
        displayp.blit(opcaop["surface"], opcaop["pos"])
    menu_selecionadop = menu_opcoesp[indice_menu]
    posp = menu_selecionadop["pos"]
    pygame.draw.circle(displayp, corp["Amarelo"], posp, 5)


def Capturar_Menu(menu_opcoesp, ep):
    for opcaop in menu_opcoesp:
        if opcaop["rect"].collidepoint(ep.pos[0], ep.pos[1]):
            opcaop["execute"]()


def Menu_Escolha_Personagem():
    global estado
    estado = 2


def Menu_Sobre_Jogo():
    global estado
    estado = 3


def Roberval_Escolhido():
    global personagem_escolhido, ladrao_Vivo_load_d_e_Des, ladrao_Vivo_load_f_Des, ladrao_Vivo_load_c_Des, ladrao_Vivo_load_d_e_Arm, ladrao_Vivo_load_f_Arm, ladrao_Vivo_load_c_Arm
    personagem_escolhido = 1
    ladrao_Vivo_load_d_e_Des, ladrao_Vivo_load_f_Des, ladrao_Vivo_load_c_Des, ladrao_Vivo_load_d_e_Arm, ladrao_Vivo_load_f_Arm, ladrao_Vivo_load_c_Arm = Mudando_Personagem(
        personagem_escolhido)
    Menu_Principal()


def Roberson_Escolhido():
    global personagem_escolhido, ladrao_Vivo_load_d_e_Des, ladrao_Vivo_load_f_Des, ladrao_Vivo_load_c_Des, ladrao_Vivo_load_d_e_Arm, ladrao_Vivo_load_f_Arm, ladrao_Vivo_load_c_Arm
    personagem_escolhido = 2
    ladrao_Vivo_load_d_e_Des, ladrao_Vivo_load_f_Des, ladrao_Vivo_load_c_Des, ladrao_Vivo_load_d_e_Arm, ladrao_Vivo_load_f_Arm, ladrao_Vivo_load_c_Arm = Mudando_Personagem(
        personagem_escolhido)
    Menu_Principal()


def Menu_Principal():
    global estado, indice_menu
    estado = 0
    indice_menu = 0


def Menu_Como_Jogar():
    global estado
    estado = 4


def Menu_Historia():
    global estado
    estado = 5


def Menu_Regras():
    global estado
    estado = 6


def Menu_Jogar():
    global estado, status_dados, tempo_inicial_jogo, tempo_inicial, status_button, tela_atual, total_tempo_pausado, indice_menu, status_numero_guarda, tempo_minutos, total_tempo_pausado2, personagem_escolhido
    pygame.mixer.music.play()
    estado = 1
    total_tempo_pausado = 0
    total_tempo_pausado2 = 0
    tempo_minutos = 0
    tela_atual = 1
    status_arma[0] = 0
    status_dados = 1
    status_numero_guarda = 1
    tempo_inicial = (int(round(time.time())) % 10000)
    tempo_inicial_jogo = (int(round(time.time())) % 10000)
    status_button = 0
    if personagem_escolhido == 1:
        Comprimir_Roberson_Imagem()
    else:
        Comprimir_Roberval_Imagem()



def Limpar_Dados():
    personagemp = []
    quantidade_personagensp = 0
    personagem_dadosp = {}
    vel_dadosp = {}
    direcaop = {}
    personagem_colisaop = {}
    personagem_imagemp = {}
    numero_blocop = 0
    paredep = []
    lanterna_colisaop = {}
    perigop = 0
    return personagemp, quantidade_personagensp, personagem_dadosp, vel_dadosp, direcaop, personagem_colisaop, personagem_imagemp, numero_blocop, paredep, lanterna_colisaop, perigop


def Construcao_de_Dados(lista_xyp, lista_direcaop, guarda_Vivo_loadp, ladrao_Vivo_load_d_ep, tela_atualp, blocop,
                        bancada_vidraçap, bancada_completap, status_numero_guardap, bancada_diamantep):
    personagemp, quantidade_personagensp, personagem_dadosp, vel_dadosp, direcaop, personagem_colisaop, personagem_imagemp, numero_blocop, paredep, lanterna_colisaop, perigop = Limpar_Dados()
    personagemp.append("Jogador")
    for a in range(1, 6):
        if tela_atual == a:
            if a != 5:
                if status_numero_guardap == 1:
                    for b in range(0, a + 1):
                        personagemp.append("Guarda" + str(b + 1))
                else:
                    for b in range(0, a):
                        personagemp.append("Guarda" + str(b + 1))
            else:
                if status_numero_guardap == 1:
                    for b in range(0, a):
                        personagemp.append("Guarda" + str(b + 1))
                else:
                    for b in range(0, a - 1):
                        personagemp.append("Guarda" + str(b + 1))
    quantidade_personagensp = len(personagemp)
    personagem_dadosp["Jogador"] = [lista_xyp[tela_atualp - 1][0][0], lista_xy[tela_atualp - 1][0][1], 60, 40, 1]
    for a in range(1, 6):
        if tela_atual == a:
            if a != 5:
                if status_numero_guardap == 1:
                    for b in range(0, a + 1):
                        personagem_dadosp["Guarda" + str(b + 1)] = [lista_xyp[a - 1][b + 1][0],
                                                                    lista_xyp[a - 1][b + 1][1],
                                                                    60, 40, 1]
                else:
                    for b in range(0, a):
                        personagem_dadosp["Guarda" + str(b + 1)] = [lista_xyp[a - 1][b + 1][0],
                                                                    lista_xyp[a - 1][b + 1][1],
                                                                    60, 40, 1]
            else:
                if status_numero_guardap == 1:
                    for b in range(0, a):
                        personagem_dadosp["Guarda" + str(b + 1)] = [lista_xyp[a - 1][b + 1][0],
                                                                    lista_xyp[a - 1][b + 1][1],
                                                                    60, 40, 1]
                else:
                    for b in range(0, a - 1):
                        personagem_dadosp["Guarda" + str(b + 1)] = [lista_xyp[a - 1][b + 1][0],
                                                                    lista_xyp[a - 1][b + 1][1],
                                                                    60, 40, 1]
    vel_dadosp["Jogador"] = [0, 0]
    for a in range(1, 6):
        if tela_atual == a:
            if a != 5:
                if status_numero_guardap == 1:
                    for b in range(0, a + 1):
                        vel_dadosp["Guarda" + str(b + 1)] = [0, 0]
                else:
                    for b in range(0, a):
                        vel_dadosp["Guarda" + str(b + 1)] = [0, 0]
            else:
                if status_numero_guardap == 1:
                    for b in range(0, a):
                        vel_dadosp["Guarda" + str(b + 1)] = [0, 0]
                else:
                    for b in range(0, a - 1):
                        vel_dadosp["Guarda" + str(b + 1)] = [0, 0]
    direcaop["Jogador"] = 0
    for a in range(1, 6):
        if tela_atual == a:
            if a != 5:
                if status_numero_guardap == 1:
                    for b in range(0, a + 1):
                        direcaop["Guarda" + str(b + 1)] = lista_direcaop[a - 1][b]
                else:
                    for b in range(0, a):
                        direcaop["Guarda" + str(b + 1)] = lista_direcaop[a - 1][b]
            else:
                if status_numero_guardap == 1:
                    for b in range(0, a):
                        direcaop["Guarda" + str(b + 1)] = lista_direcaop[a - 1][b]
                else:
                    for b in range(0, a - 1):
                        direcaop["Guarda" + str(b + 1)] = lista_direcaop[a - 1][b]
    personagem_colisaop["Jogador"] = ""
    for a in range(1, 6):
        if tela_atual == a:
            if a != 5:
                if status_numero_guardap == 1:
                    for b in range(0, a + 1):
                        personagem_colisaop["Guarda" + str(b + 1)] = ""
                else:
                    for b in range(0, a):
                        personagem_colisaop["Guarda" + str(b + 1)] = ""
            else:
                if status_numero_guardap == 1:
                    for b in range(0, a):
                        personagem_colisaop["Guarda" + str(b + 1)] = ""
                else:
                    for b in range(0, a - 1):
                        personagem_colisaop["Guarda" + str(b + 1)] = ""
    personagem_imagemp["Jogador"] = pygame.transform.scale(ladrao_Vivo_load_d_ep, (60, 80))

    for a in range(1, 6):
        if tela_atual == a:
            if a != 5:
                if status_numero_guardap == 1:
                    for b in range(0, a + 1):
                        personagem_imagemp["Guarda" + str(b + 1)] = pygame.transform.scale(guarda_Vivo_loadp, (60, 80))
                else:
                    for b in range(0, a):
                        personagem_imagemp["Guarda" + str(b + 1)] = pygame.transform.scale(guarda_Vivo_loadp, (60, 80))
            else:
                if status_numero_guardap == 1:
                    for b in range(0, a):
                        personagem_imagemp["Guarda" + str(b + 1)] = pygame.transform.scale(guarda_Vivo_loadp, (60, 80))
                else:
                    for b in range(0, a - 1):
                        personagem_imagemp["Guarda" + str(b + 1)] = pygame.transform.scale(guarda_Vivo_loadp, (60, 80))

    for guar in range(0, quantidade_personagensp):
        lanterna_colisaop[personagemp[guar]] = ""

    if tela_atualp == 1:
        numero_blocop = len(blocop[0])
    elif tela_atualp == 2:
        numero_blocop = len(blocop[1])
    elif tela_atualp == 3:
        numero_blocop = len(blocop[2])
    elif tela_atualp == 4:
        numero_blocop = len(blocop[3])
    elif tela_atualp == 5:
        numero_blocop = len(blocop[4])
    for a in range(0, numero_blocop):
        paredep.append(0)
    status_dadosp = 0
    for a in range(0, numero_blocop):
        if blocop[tela_atualp - 1][a][4] == 0:
            blocop[tela_atualp - 1][a].append(pygame.transform.scale(bancada_vidraçap, (80, 80)))
        elif blocop[tela_atualp - 1][a][4] == 1:
            blocop[tela_atualp - 1][a].append(pygame.transform.scale(bancada_completap, (80, 120)))
        elif blocop[tela_atualp - 1][a][4] == 2:
            blocop[tela_atualp - 1][a].append(pygame.transform.scale(bancada_diamantep, (80, 120)))
    return personagemp, quantidade_personagensp, personagem_dadosp, vel_dadosp, direcaop, personagem_colisaop, status_dadosp, personagem_imagemp, numero_blocop, paredep, lanterna_colisaop, perigop, blocop,


def Quant_Pontos(ponto_direcaop, tela_atualp):
    if tela_atualp == 1:
        quant_pontosp = len(ponto_direcaop[0])
    if tela_atualp == 2:
        quant_pontosp = len(ponto_direcaop[1])
    if tela_atualp == 3:
        quant_pontosp = len(ponto_direcaop[2])
    if tela_atualp == 4:
        quant_pontosp = len(ponto_direcaop[3])
    if tela_atualp == 5:
        quant_pontosp = len(ponto_direcaop[4])
    return quant_pontosp


def Mudando_Direcao(ponto_direcaop, direcaop):
    if ponto_direcaop[2] == 1:
        if ponto_direcaop[3] == 1:
            novadirecaop = 0
        elif ponto_direcaop[3] == 2:
            novadirecaop = 90
        elif ponto_direcaop[3] == 3:
            novadirecaop = 180
        elif ponto_direcaop[3] == 4:
            novadirecaop = 270
    elif ponto_direcaop[2] == 2:
        if ponto_direcaop[3] == 1:
            if direcaop == 180:
                novadirecaop = 90
            elif direcaop == 270:
                novadirecaop = 0
        elif ponto_direcaop[3] == 2:
            if direcaop == 90:
                novadirecaop = 0
            elif direcaop == 180:
                novadirecaop = 270
        elif ponto_direcaop[3] == 3:
            if direcaop == 0:
                novadirecaop = 90
            elif direcaop == 270:
                novadirecaop = 180
        elif ponto_direcaop[3] == 4:
            if direcaop == 0:
                novadirecaop = 270
            elif direcaop == 90:
                novadirecaop = 180
    elif ponto_direcaop[2] == 3:
        nova_direcao_randp = randint(1, 2)
        if ponto_direcaop[3] == 1:
            if direcaop == 0:
                if nova_direcao_randp == 1:
                    novadirecaop = 0
                elif nova_direcao_randp == 2:
                    novadirecaop = 90
            elif direcaop == 180:
                if nova_direcao_randp == 1:
                    novadirecaop = 90
                elif nova_direcao_randp == 2:
                    novadirecaop = 180
            elif direcaop == 270:
                if nova_direcao_randp == 1:
                    novadirecaop = 0
                elif nova_direcao_randp == 2:
                    novadirecaop = 180
        elif ponto_direcaop[3] == 2:
            if direcaop == 90:
                if nova_direcao_randp == 1:
                    novadirecaop = 0
                elif nova_direcao_randp == 2:
                    novadirecaop = 90
            elif direcaop == 180:
                if nova_direcao_randp == 1:
                    novadirecaop = 90
                elif nova_direcao_randp == 2:
                    novadirecaop = 270
            elif direcaop == 270:
                if nova_direcao_randp == 1:
                    novadirecaop = 0
                elif nova_direcao_randp == 2:
                    novadirecaop = 270
        elif ponto_direcaop[3] == 3:
            if direcaop == 0:
                if nova_direcao_randp == 1:
                    novadirecaop = 0
                elif nova_direcao_randp == 2:
                    novadirecaop = 270
            elif direcaop == 90:
                if nova_direcao_randp == 1:
                    novadirecaop = 0
                elif nova_direcao_randp == 2:
                    novadirecaop = 180
            elif direcaop == 180:
                if nova_direcao_randp == 1:
                    novadirecaop = 180
                elif nova_direcao_randp == 2:
                    novadirecaop = 270
        elif ponto_direcaop[3] == 4:
            if direcaop == 0:
                if nova_direcao_randp == 1:
                    novadirecaop = 90
                elif nova_direcao_randp == 2:
                    novadirecaop = 270
            elif direcaop == 90:
                if nova_direcao_randp == 1:
                    novadirecaop = 90
                elif nova_direcao_randp == 2:
                    novadirecaop = 180
            elif direcaop == 270:
                if nova_direcao_randp == 1:
                    novadirecaop = 180
                elif nova_direcao_randp == 2:
                    novadirecaop = 270
    elif ponto_direcaop[2] == 4:
        nova_direcao_randp = randint(1, 3)
        if direcaop == 0:
            if nova_direcao_randp == 1:
                novadirecaop = 0
            elif nova_direcao_randp == 2:
                novadirecaop = 90
            elif nova_direcao_randp == 3:
                novadirecaop = 270
        elif direcaop == 90:
            if nova_direcao_randp == 1:
                novadirecaop = 0
            elif nova_direcao_randp == 2:
                novadirecaop = 90
            elif nova_direcao_randp == 3:
                novadirecaop = 180
        elif direcaop == 180:
            if nova_direcao_randp == 1:
                novadirecaop = 90
            elif nova_direcao_randp == 2:
                novadirecaop = 180
            elif nova_direcao_randp == 3:
                novadirecaop = 270
        elif direcaop == 270:
            if nova_direcao_randp == 1:
                novadirecaop = 0
            elif nova_direcao_randp == 2:
                novadirecaop = 180
            elif nova_direcao_randp == 3:
                novadirecaop = 270
    return novadirecaop


def Testando_pontos_direçao(tela_atualp, personagem_dadosp, direcaop, ponto_direcaop, quant_pontosp):
    if tela_atualp == 1:
        for pd in range(0, quant_pontosp):
            if (personagem_dadosp[0] + 30) == ponto_direcaop[0][pd][0] and personagem_dadosp[1] + 20 == \
                    ponto_direcaop[0][pd][1]:

                nova_direcaop2 = Mudando_Direcao(ponto_direcaop[0][pd], direcaop)
                break
            else:
                nova_direcaop2 = direcaop
    elif tela_atualp == 2:
        for pd in range(0, quant_pontosp):
            if (personagem_dadosp[0] + 30) == ponto_direcaop[1][pd][0] and personagem_dadosp[1] + 20 == \
                    ponto_direcaop[1][pd][1]:

                nova_direcaop2 = Mudando_Direcao(ponto_direcaop[1][pd], direcaop)
                break
            else:
                nova_direcaop2 = direcaop
    elif tela_atualp == 3:
        for pd in range(0, quant_pontosp):
            if (personagem_dadosp[0] + 30) == ponto_direcaop[2][pd][0] and personagem_dadosp[1] + 20 == \
                    ponto_direcaop[2][pd][1]:
                nova_direcaop2 = Mudando_Direcao(ponto_direcaop[2][pd], direcaop)
                break
            else:
                nova_direcaop2 = direcaop
    elif tela_atualp == 4:
        for pd in range(0, quant_pontosp):
            if (personagem_dadosp[0] + 30) == ponto_direcaop[3][pd][0] and personagem_dadosp[1] + 20 == \
                    ponto_direcaop[3][pd][1]:

                nova_direcaop2 = Mudando_Direcao(ponto_direcaop[3][pd], direcaop)
                break
            else:
                nova_direcaop2 = direcaop
    elif tela_atualp == 5:
        for pd in range(0, quant_pontosp):
            if (personagem_dadosp[0] + 30) == ponto_direcaop[4][pd][0] and personagem_dadosp[1] + 20 == \
                    ponto_direcaop[4][pd][1]:
                nova_direcaop2 = Mudando_Direcao(ponto_direcaop[4][pd], direcaop)
                break
            else:
                nova_direcaop2 = direcaop
    return nova_direcaop2


def Mudando_Direcao_Esbarrao(quantidade_personagensp, personagem_especificop, personagemp,
                             personagem_colisao_especificop, personagem_colisaop, direcao_especificap,
                             personagem_dadosp):
    if personagem_dadosp[4] == 1:
        for guarp in range(1, quantidade_personagensp):
            if personagem_especificop != personagemp[guarp]:
                if personagem_colisao_especificop.colliderect(personagem_colisaop[personagemp[guarp]]):
                    if personagem_dados[personagemp[guarp]][4] == 1:
                        if direcao_especificap == 0:
                            nova_direcaop = 180
                            return nova_direcaop
                        elif direcao_especificap == 90:
                            nova_direcaop = 270
                            return nova_direcaop
                        elif direcao_especificap == 180:
                            nova_direcaop = 0
                            return nova_direcaop
                        elif direcao_especificap == 270:
                            nova_direcaop = 90
                            return nova_direcaop
                        else:
                            nova_direcaop = direcao_especificap
                else:
                    nova_direcaop = direcao_especificap
            else:
                nova_direcaop = direcao_especificap
    else:
        nova_direcaop = direcao_especificap
    return nova_direcaop


def Movimento(personagem_dadosp, velp):
    if personagem_dadosp[4] == 1:
        if personagem_dadosp[0] > -1 and personagem_dadosp[0] < 741:
            personagem_dadosp[0] += velp[0]
        else:
            if personagem_dadosp[0] < 0:
                personagem_dadosp[0] += 1
            else:
                personagem_dadosp[0] -= 1

        if personagem_dadosp[1] > 39 and personagem_dadosp[1] < 641:
            personagem_dadosp[1] += velp[1]
        else:
            if personagem_dadosp[1] < 40:
                personagem_dadosp[1] += 1
            else:
                personagem_dadosp[1] -= 1


def Velocidade_Guarda(direcaop, vel_dadosp, perigop, personagem_dadosp):
    if perigop == 0:
        if direcaop == 0:
            vel_dadosp[0] = 0.125
            vel_dadosp[1] = 0
        elif direcaop == 90:
            vel_dadosp[1] = -0.125
            vel_dadosp[0] = 0
        elif direcaop == 180:
            vel_dadosp[0] = -0.125
            vel_dadosp[1] = 0
        elif direcaop == 270:
            vel_dadosp[1] = 0.125
            vel_dadosp[0] = 0
    else:
        if personagem_dadosp[4] == 1:
            if direcaop == 0:
                if personagem_dadosp[0] % 0.25 != 0:
                    personagem_dadosp[0] -= 0.125
                if personagem_dadosp[1] % 0.25 != 0:
                    personagem_dadosp[1] -= 0.125
            elif direcaop == 90:
                if personagem_dadosp[0] % 0.25 != 0:
                    personagem_dadosp[0] -= 0.125
                if personagem_dadosp[1] % 0.25 != 0:
                    personagem_dadosp[1] -= 0.125
            elif direcaop == 180:
                if personagem_dadosp[0] % 0.25 != 0:
                    personagem_dadosp[0] += 0.125
                if personagem_dadosp[1] % 0.25 != 0:
                    personagem_dadosp[1] += 0.125
            elif direcaop == 270:
                if personagem_dadosp[0] % 0.25 != 0:
                    personagem_dadosp[0] += 0.125
                if personagem_dadosp[1] % 0.25 != 0:
                    personagem_dadosp[1] += 0.125
        if direcaop == 0:
            vel_dadosp[0] = 0.25
            vel_dadosp[1] = 0
        elif direcaop == 90:
            vel_dadosp[1] = -0.25
            vel_dadosp[0] = 0
        elif direcaop == 180:
            vel_dadosp[0] = -0.25
            vel_dadosp[1] = 0
        elif direcaop == 270:
            vel_dadosp[1] = 0.25
            vel_dadosp[0] = 0


def Construcao_Personagem_Colisao(personagem_dadosp):
    personagem_colisaop = pygame.Rect((personagem_dadosp[0], personagem_dadosp[1]),
                                      (personagem_dadosp[2], personagem_dadosp[3]))
    return personagem_colisaop


def Construcao_Obstaculo_Colisao(tela_atualp, blocop, numero_blocop, paredep):
    for a in range(0, numero_blocop):
        paredep[a] = pygame.Rect((blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1]),
                                 (blocop[tela_atualp - 1][a][2], blocop[tela_atualp - 1][a][3]))
    return paredep


def Construcao_Arma_Colisao(status_armap, armap, tela_atualp):
    if status_armap[0] == 0:
        arma_colisaop = pygame.Rect((armap[tela_atualp - 1][0], armap[tela_atualp - 1][1]),
                                    (armap[tela_atualp - 1][2], armap[tela_atualp - 1][3]))
    else:
        arma_colisaop = ""
    return arma_colisaop


def Construcao_Saida_Colisao(saidasp, tela_atualp):
    saidas_colisaop = pygame.Rect(saidasp[tela_atualp - 1][0], saidasp[tela_atualp - 1][1], saidasp[tela_atualp - 1][2],
                                  saidasp[tela_atualp - 1][3])

    return saidas_colisaop


def Colisoes(personagem_espicp, personagem_colisao_espeficp, bloco_personagemp, parede_personagem_colip):
    if personagem_colisao_espeficp.colliderect(parede_personagem_colip):
        if (personagem_espicp[0] + personagem_espicp[2]) < (bloco_personagemp[0] + 2) and (personagem_espicp[0] + personagem_espicp[2]) > bloco_personagemp[0]:
            personagem_espicp[0] -= 0.5
        elif personagem_espicp[0] > (bloco_personagemp[0] + bloco_personagemp[2] - 2) and personagem_espicp[0] < (bloco_personagemp[0] + bloco_personagemp[2]):
            personagem_espicp[0] += 0.5
        if (personagem_espicp[1] + personagem_espicp[3]) < (bloco_personagemp[1] + 2) and (
                personagem_espicp[1] + personagem_espicp[3]) > (bloco_personagemp[1]):
            personagem_espicp[1] -= 0.5
        elif (personagem_espicp[1]) > (bloco_personagemp[1] + bloco_personagemp[3] - 2) and (personagem_espicp[1]) < (
                bloco_personagemp[1] + bloco_personagemp[3]):
            personagem_espicp[1] += 0.5


def Teste_Colisao_Blocos(personagem_dadosp, persongem_colisaop, blocop, numero_blocop, paredep, tela_atualp):
    if tela_atualp == 1:
        for a in range(0, numero_blocop):
            Colisoes(personagem_dadosp, persongem_colisaop, blocop[0][a], paredep[a])
    if tela_atualp == 2:
        for a in range(0, numero_blocop):
            Colisoes(personagem_dadosp, persongem_colisaop, blocop[1][a], paredep[a])
    if tela_atualp == 3:
        for a in range(0, numero_blocop):
            Colisoes(personagem_dadosp, persongem_colisaop, blocop[2][a], paredep[a])
    if tela_atualp == 4:
        for a in range(0, numero_blocop):
            Colisoes(personagem_dadosp, persongem_colisaop, blocop[3][a], paredep[a])
    if tela_atualp == 5:
        for a in range(0, numero_blocop):
            Colisoes(personagem_dadosp, persongem_colisaop, blocop[4][a], paredep[a])


def Cenario(displayp):
    displayp.fill(cor["Bisque3"])
    for y in range(40, 680, 80):
        for x in range(0, 800, 80):
            pygame.draw.rect(displayp, cor["Preto"], (x, y, 80, 80), 3)
    for x in range(0, 800, 80):
        pygame.draw.rect(displayp, cor["Laranja"], (x, 0, 80, 40), 0)


def Barra(displayp):
    pygame.draw.rect(displayp, cor["Preto"], (800, 0, 100, 680), 0)


def Perigo_Imagem(displayp, perigop, alarme_rendp):
    if perigop == 1:
        displayp.blit(alarme_rendp, (808, 30))


def Tempo_Imagem(displayp, tempo_imgp):
    pygame.draw.rect(displayp, cor["Azul"], ((803, 205), (93, 32)), 2)
    displayp.blit(tempo_imgp, (810, 205))


def Arma_Imagem(displayp, status_armap, status_armado_Imgp, status_desarmado_Imgp):
    if status_armap[0] == 0:
        displayp.blit(status_desarmado_Imgp, (815, 300))
    elif status_armap[0] == 1:
        displayp.blit(status_armado_Imgp, (815, 300))


def Sobreposicao_Tela_Personagem(personagem_dadosp):
    sob0 = personagem_dadosp[1] < 40
    sob1 = personagem_dadosp[1] >= 40 and personagem_dadosp[1] < 80
    sob2 = personagem_dadosp[1] >= 80 and personagem_dadosp[1] < 120
    sob3 = personagem_dadosp[1] >= 120 and personagem_dadosp[1] < 160
    sob4 = personagem_dadosp[1] >= 160 and personagem_dadosp[1] < 200
    sob5 = personagem_dadosp[1] >= 200 and personagem_dadosp[1] < 240
    sob6 = personagem_dadosp[1] >= 240 and personagem_dadosp[1] < 280
    sob7 = personagem_dadosp[1] >= 280 and personagem_dadosp[1] < 320
    sob8 = personagem_dadosp[1] >= 320 and personagem_dadosp[1] < 360
    sob9 = personagem_dadosp[1] >= 360 and personagem_dadosp[1] < 400
    sob10 = personagem_dadosp[1] >= 400 and personagem_dadosp[1] < 440
    sob11 = personagem_dadosp[1] >= 440 and personagem_dadosp[1] < 480
    sob12 = personagem_dadosp[1] >= 480 and personagem_dadosp[1] < 520
    sob13 = personagem_dadosp[1] >= 520 and personagem_dadosp[1] < 560
    sob14 = personagem_dadosp[1] >= 560 and personagem_dadosp[1] < 600
    sob15 = personagem_dadosp[1] >= 600 and personagem_dadosp[1] < 640
    sob16 = personagem_dadosp[1] >= 640 and personagem_dadosp[1] < 680
    if sob0:
        sob = 0
    elif sob1:
        sob = 1
    elif sob2:
        sob = 2
    elif sob3:
        sob = 3
    elif sob4:
        sob = 4
    elif sob5:
        sob = 5
    elif sob6:
        sob = 6
    elif sob7:
        sob = 7
    elif sob8:
        sob = 8
    elif sob9:
        sob = 9
    elif sob10:
        sob = 10
    elif sob11:
        sob = 11
    elif sob12:
        sob = 12
    elif sob13:
        sob = 13
    elif sob14:
        sob = 14
    elif sob15:
        sob = 15
    elif sob16:
        sob = 16
    return sob


def Construcao_Personagem_Imagem(direcaop, personagem_Vivo_load_l_d_Desp, personagem_Vivo_load_c_Desp,
                                 personagem_Vivo_load_f_Desp,
                                 personagem_imagemp, personagem_Morto_load_l_d_Desp, personagem_Morto_load_f_Desp,
                                 personagem_Morto_load_c_Desp, personagem_dadosp, personagem_Vivo_load_l_d_Armp,
                                 personagem_Vivo_load_c_Armp, personagem_Vivo_load_f_Armp,
                                 personagem_Morto_load_l_d_Armp, personagem_Morto_load_f_Armp,
                                 personagem_Morto_load_c_Armp):
    if status_arma == [0]:
        if personagem_dadosp[4] == 1:
            if direcaop == 0:
                personagem_imagemp = pygame.transform.scale(personagem_Vivo_load_l_d_Desp, (60, 80))
            if direcaop == 180:
                personagem_imagp = pygame.transform.scale(personagem_Vivo_load_l_d_Desp, (60, 80))
                personagem_imagemp = pygame.transform.flip(personagem_imagp, True, False)
            if direcaop == 90:
                personagem_imagemp = pygame.transform.scale(personagem_Vivo_load_c_Desp, (60, 80))
            if direcaop == 270:
                personagem_imagemp = pygame.transform.scale(personagem_Vivo_load_f_Desp, (60, 80))
        elif personagem_dadosp[4] == 0:
            if direcaop == 0:
                personagem_imagemp = pygame.transform.scale(personagem_Morto_load_l_d_Desp, (80, 60))
            if direcaop == 180:
                personagem_imagp = pygame.transform.scale(personagem_Morto_load_l_d_Desp, (80, 60))
                personagem_imagemp = pygame.transform.flip(personagem_imagp, True, False)
            if direcaop == 90:
                personagem_imagemp = pygame.transform.scale(personagem_Morto_load_c_Desp, (60, 80))
            if direcaop == 270:
                personagem_imagemp = pygame.transform.scale(personagem_Morto_load_f_Desp, (60, 80))
    else:
        if personagem_dadosp[4] == 1:
            if direcaop == 0:
                personagem_imagemp = pygame.transform.scale(personagem_Vivo_load_l_d_Armp, (60, 80))
            if direcaop == 180:
                personagem_imagp = pygame.transform.scale(personagem_Vivo_load_l_d_Armp, (60, 80))
                personagem_imagemp = pygame.transform.flip(personagem_imagp, True, False)
            if direcaop == 90:
                personagem_imagemp = pygame.transform.scale(personagem_Vivo_load_c_Armp, (60, 80))
            if direcaop == 270:
                personagem_imagemp = pygame.transform.scale(personagem_Vivo_load_f_Armp, (60, 80))
        elif personagem_dadosp[4] == 0:
            if direcaop == 0:
                personagem_imagemp = pygame.transform.scale(personagem_Morto_load_l_d_Armp, (80, 60))
            if direcaop == 180:
                personagem_imagp = pygame.transform.scale(personagem_Morto_load_l_d_Armp, (80, 60))
                personagem_imagemp = pygame.transform.flip(personagem_imagp, True, False)
            if direcaop == 90:
                personagem_imagemp = pygame.transform.scale(personagem_Morto_load_c_Armp, (60, 80))
            if direcaop == 270:
                personagem_imagemp = pygame.transform.scale(personagem_Morto_load_f_Armp, (60, 80))
    return personagem_imagemp


def Construcao_Imagem(displayp, tela_atualp, personagemp, quantidade_personagemp, personagem_dadosp,
                      blocop, saidasp, armap, teaser_chao_rendp, status_armap, personagem_imagemp, seq_cont_blocp,
                      saida_Imgp):
    if status_armap[0] == 0:
        displayp.blit(teaser_chao_rendp,
                      (armap[tela_atualp - 1][0], armap[tela_atualp - 1][1]))
    displayp.blit(saida_Imgp,
                  (saidas[tela_atualp - 1][0], saidasp[tela_atualp - 1][1]))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 0:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if personagem_dados[personagem[pers]][4] == 1:
            if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 0:
                displayp.blit(personagem_imagemp[personagemp[pers]],
                              (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))

    # 1º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][0], seq_cont_blocp[tela_atualp - 1][1]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 1:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 1:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 2:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 2:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    # 2º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][1], seq_cont_blocp[tela_atualp - 1][2]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 3:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 3:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 4:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 4:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    # 3º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][2], seq_cont_blocp[tela_atualp - 1][3]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 5:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 5:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 6:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 6:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    # 4º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][3], seq_cont_blocp[tela_atualp - 1][4]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 7:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 7:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 8:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 8:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    # 5º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][4], seq_cont_blocp[tela_atualp - 1][5]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 9:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 9:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 10:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 10:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    # 6º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][5], seq_cont_blocp[tela_atualp - 1][6]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 11:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 11:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 12:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 12:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    # 7º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][6], seq_cont_blocp[tela_atualp - 1][7]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 13:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 13:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 14:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 14:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    # 8º fileira
    for a in range(seq_cont_blocp[tela_atualp - 1][7], seq_cont_blocp[tela_atualp - 1][8]):
        displayp.blit(blocop[tela_atualp - 1][a][5],
                      (blocop[tela_atualp - 1][a][0], blocop[tela_atualp - 1][a][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 15:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 15:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))
    if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[0]]) == 16:
        displayp.blit(personagem_imagemp[personagemp[0]],
                      (personagem_dadosp[personagemp[0]][0], personagem_dadosp[personagemp[0]][1] - 40))
    for pers in range(1, quantidade_personagemp):
        if Sobreposicao_Tela_Personagem(personagem_dadosp[personagemp[pers]]) == 16:
            displayp.blit(personagem_imagemp[personagemp[pers]],
                          (personagem_dadosp[personagemp[pers]][0], personagem_dadosp[personagemp[pers]][1] - 40))


def Troca_de_Tela(tela_atualp, status_dadosp, personagem_colisaop, personagemp, saida_colisaop, jogop2):
    global indice_menu, alerta_som, choque_som
    if tela_atualp == 1 and status_dadosp == 0:
        if personagem_colisaop[personagemp[0]].colliderect(saida_colisaop):
            alerta_som.stop()
            choque_som.stop()
            tela_atualp = 2
            status_dadosp = 1
            jogop = jogop2
            status_questaop = 1
            indice_menu = 1
            status_questao_inicialp = 1
        else:
            status_questaop = 0
            jogop = jogop2
            status_questao_inicialp = 0
    elif tela_atualp == 2 and status_dadosp == 0:
        if personagem_colisaop[personagemp[0]].colliderect(saida_colisaop):
            alerta_som.stop()
            choque_som.stop()
            tela_atualp = 3
            status_dadosp = 1
            jogop = jogop2
            status_questaop = 1
            indice_menu = 1
            status_questao_inicialp = 1
        else:
            jogop = jogop2
            status_questaop = 0
            status_questao_inicialp = 0
    elif tela_atualp == 3 and status_dadosp == 0:
        if personagem_colisaop[personagemp[0]].colliderect(saida_colisaop):
            alerta_som.stop()
            choque_som.stop()
            tela_atualp = 4
            status_dadosp = 1
            jogop = jogop2
            status_questaop = 1
            indice_menu = 1
            status_questao_inicialp = 1
        else:
            jogop = jogop2
            status_questaop = 0
            status_questao_inicialp = 0
    elif tela_atualp == 4 and status_dadosp == 0:
        if personagem_colisaop[personagemp[0]].colliderect(saida_colisaop):
            alerta_som.stop()
            choque_som.stop()
            tela_atualp = 5
            status_dadosp = 1
            jogop = jogop2
            status_questaop = 1
            indice_menu = 1
            status_questao_inicialp = 1
        else:
            jogop = jogop2
            status_questaop = 0
            status_questao_inicialp = 0
    elif tela_atualp == 5 and status_dadosp == 0:
        if personagem_colisaop[personagemp[0]].colliderect(saida_colisaop):
            alerta_som.stop()
            choque_som.stop()
            jogop = 2
            status_questaop = 0
            status_questao_inicialp = 0
        else:
            jogop = jogop2
            status_questaop = 0
            status_questao_inicialp = 0
    else:
        jogop = jogop2
        status_questaop = 0
        status_questao_inicialp = 0
    return tela_atualp, status_dadosp, jogop, status_questaop, status_questao_inicialp


def Pegar_Arma(arma_colisaop, personagem_colisaop, personagemp, status_armap, quantidade_personagensp,
               personagem_dadosp, direcaop):
    if arma_colisaop != "":
        if personagem_colisaop[personagemp[0]].colliderect(arma_colisaop):
            if status_armap[0] == 0:
                status_armap[0] = 1
    else:
        Bater_Guarda(quantidade_personagensp, personagem_colisaop, personagemp, status_armap, personagem_dadosp,
                     direcaop)


def Bater_Guarda(quantidade_personagensp, personagem_colisaop, personagemp, status_armap, personagem_dadosp, direcaop):
    global choque_som
    for guar in range(1, quantidade_personagensp):
        if personagem_dadosp[personagem[guar]][4] == 1:
            if personagem_colisaop[personagemp[0]].colliderect(personagem_colisaop[personagemp[guar]]):
                if direcaop[personagemp[0]] == direcaop[personagemp[guar]]:
                    if status_armap[0] == 1:
                        choque_som.play()
                        status_armap[0] = 0
                    if personagem_dadosp[personagemp[guar]][4] == 1:
                        personagem_dadosp[personagemp[guar]][4] = 0
                        personagem_dadosp[personagemp[guar]][2] = 60
                        personagem_dadosp[personagemp[guar]][3] = 40
                        if direcaop[personagemp[guar]] == 0 or direcaop[personagemp[guar]] == 180:
                            personagem_dadosp[personagemp[guar]][1] += 40


def Eventos(velp, personagemp, personagem_colisaop, arma_colisaop, status_armap, quantidade_personagensp, direcaop,
            personagem_dadosp, lista_opcoesp, lista_opcoes_personagemp, lista_opcoes_sobrep, lista_opcoes_como_jogarp,
            lista_opcoes_historiap, tempo_pausadop, lista_opcoes_questao1p, lista_opcoes_questao2p,
            lista_opcoes_questao3p, lista_opcoes_questao4p,
            tela_atualp, lista_opcoes_regrasp):
    global estado
    global indice_menu
    global status_button
    global status_questao
    for e in pygame.event.get():

        if e.type == QUIT:
            if estado == 1:
                if personagem_escolhido == 1:
                    Descomprimir_Roberson_Imagens()
                else:
                    Descomprimir_Roberval_Imagens()
            exit()
        if e.type == KEYDOWN:
            if estado == 0:
                if e.key == K_UP:
                    indice_menu -= 1
                elif e.key == K_DOWN:
                    indice_menu += 1
                if e.key == K_SPACE:
                    lista_opcoesp[indice_menu]["execute"]()
                    indice_menu = 0
            elif estado == 1:
                if status_questao == 0:
                    if e.key == K_UP and status_button == 0:
                        velp[personagemp[0]][1] = -0.5
                        status_button = 1
                        direcaop[personagemp[0]] = 90
                    elif e.key == K_DOWN and status_button == 0:
                        velp[personagemp[0]][1] = 0.5
                        status_button = 2
                        direcaop[personagemp[0]] = 270
                    elif e.key == K_LEFT and status_button == 0:
                        velp[personagemp[0]][0] = -0.5
                        status_button = 3
                        direcaop[personagemp[0]] = 180
                    elif e.key == K_RIGHT and status_button == 0:
                        velp[personagemp[0]][0] = 0.5
                        status_button = 4
                        direcaop[personagemp[0]] = 0
                    if e.key == K_SPACE:
                        Pegar_Arma(arma_colisaop, personagem_colisaop, personagemp, status_armap,
                                   quantidade_personagensp,
                                   personagem_dadosp, direcaop)
                    if e.key == K_ESCAPE:
                        Menu_Principal()
                        pygame.mixer.music.stop()
                        if personagem_escolhido == 1:
                            Descomprimir_Roberson_Imagens()
                        else:
                            Descomprimir_Roberval_Imagens()
                else:
                    if e.key == K_SPACE:
                        if tela_atualp == 2:
                            lista_opcoes_questao1p[indice_menu]["execute"](tempo_pausadop)
                        if tela_atualp == 3:
                            lista_opcoes_questao2p[indice_menu]["execute"](tempo_pausadop)
                        if tela_atualp == 4:
                            lista_opcoes_questao3p[indice_menu]["execute"](tempo_pausadop)
                        if tela_atualp == 5:
                            lista_opcoes_questao4p[indice_menu]["execute"](tempo_pausadop)
                    if e.key == K_LEFT:
                        if indice_menu > 1:
                            indice_menu -= 1
                    elif e.key == K_RIGHT:
                        indice_menu += 1
            elif estado == 2:
                if e.key == K_LEFT:
                    indice_menu -= 1
                elif e.key == K_RIGHT:
                    if indice_menu < 1:
                        indice_menu += 1
                elif e.key == K_DOWN:
                    indice_menu = 2
                elif e.key == K_UP:
                    indice_menu = 0
                if e.key == K_SPACE:
                    lista_opcoes_personagemp[indice_menu]["execute"]()
                    indice_menu = 0
            elif estado == 3:
                if e.key == K_DOWN:
                    indice_menu += 1
                elif e.key == K_UP:
                    indice_menu -= 1
                if e.key == K_SPACE:
                    lista_opcoes_sobrep[indice_menu]["execute"]()
                    indice_menu = 0
            elif estado == 4:
                if e.key == K_SPACE:
                    lista_opcoes_como_jogarp[indice_menu]["execute"]()
                    indice_menu = 0
                if e.key == K_ESCAPE:
                    estado = 3
                    indice_menu = 0
            elif estado == 5:
                if e.key == K_SPACE:
                    lista_opcoes_historiap[indice_menu]["execute"]()
                    indice_menu = 0
                if e.key == K_ESCAPE:
                    estado = 3
                    indice_menu = 0
            elif estado == 6:
                if e.key == K_SPACE:
                    lista_opcoes_regrasp[indice_menu]["execute"]()
                    indice_menu = 0
                if e.key == K_ESCAPE:
                    estado = 3
                    indice_menu = 0
        elif e.type == KEYUP:
            if estado == 1:
                if status_questao == 0:
                    if e.key == K_UP:
                        velp[personagemp[0]][1] = 0
                        if status_button == 1:
                            status_button = 0
                    elif e.key == K_DOWN:
                        velp[personagemp[0]][1] = 0
                        if status_button == 2:
                            status_button = 0
                    elif e.key == K_LEFT:
                        velp[personagemp[0]][0] = 0
                        if status_button == 3:
                            status_button = 0
                    elif e.key == K_RIGHT:
                        velp[personagemp[0]][0] = 0
                        if status_button == 4:
                            status_button = 0


def Calculo_Tempo(tempo_inicialp2, status_tempop, fontep, tempo_inicial_jogop):
    global tempo_minutos, total_tempo_pausado, total_tempo_pausado2
    tempo_segundos_jogop = (int(round(time.time())) % 10000) - tempo_inicial_jogop - total_tempo_pausado2
    tempo_segundosp = (int(round(time.time())) % 10000) - tempo_inicialp2 - total_tempo_pausado
    if tempo_segundosp > 59:
        tempo_minutos += 1
        total_tempo_pausado = 0
        status_tempop = 1
    if status_tempop == 1:
        tempo_inicialp = (int(round(time.time())) % 10000)
        status_tempop = 0
    else:
        tempo_inicialp = tempo_inicialp2
    if tempo_minutos < 10:
        tempo_minuto_stringp = "0" + str(tempo_minutos)
    else:
        tempo_minuto_stringp = str(tempo_minutos)
    if tempo_segundosp < 10:
        tempo_segundo_stringp = "0" + str(tempo_segundosp)
    else:
        tempo_segundo_stringp = str(tempo_segundosp)
    tempo_imgp = fontep.render(str(tempo_minuto_stringp) + ":" + str(tempo_segundo_stringp), True, cor["Azul"])
    return tempo_imgp, status_tempop, tempo_inicialp, tempo_segundos_jogop


def Lanterna_Imagem(displayp, direcaop, personagem_dadosp, luzp):
    if personagem_dadosp[4] == 1:
        if direcaop == 0:
            luzp = pygame.transform.rotate(luzp, 180)
            displayp.blit(luzp, ((personagem_dadosp[0] + personagem_dadosp[2]), (personagem_dadosp[1])))
        elif direcaop == 90:
            luzp = pygame.transform.rotate(luzp, 270)
            displayp.blit(luzp, (
                (personagem_dadosp[0]), (personagem_dadosp[1] - personagem_dadosp[3])))
        elif direcaop == 180:
            displayp.blit(luzp, ((personagem_dadosp[0] - personagem_dadosp[2]), (personagem_dadosp[1])))
        elif direcaop == 270:
            luzp = pygame.transform.rotate(luzp, 90)
            displayp.blit(luzp, (
                (personagem_dadosp[0]), (personagem_dadosp[1] + personagem_dadosp[3])))


def Construção_Lanterna_Colisão(direcaop, personagem_dadosp):
    if direcaop == 0:
        lanterna_colisaop = pygame.Rect(
            ((personagem_dadosp[0] + personagem_dadosp[2]), (personagem_dadosp[1])),
            (personagem_dadosp[2], (personagem_dadosp[3] / 2) * 2.5))
    elif direcaop == 90:
        lanterna_colisaop = pygame.Rect(
            ((personagem_dadosp[0] + (personagem_dadosp[2] / 2)), (personagem_dadosp[1] - personagem_dadosp[3] / 8)),
            (1, personagem_dadosp[3]))
    elif direcaop == 180:
        lanterna_colisaop = pygame.Rect(
            ((personagem_dadosp[0] - personagem_dadosp[2]), (personagem_dadosp[1])),
            (personagem_dadosp[2], (personagem_dadosp[3] / 2) * 2.5))
    elif direcaop == 270:
        lanterna_colisaop = pygame.Rect(
            ((personagem_dadosp[0] + (personagem_dadosp[2] / 2)), (personagem_dadosp[1] + personagem_dadosp[3])),
            (1, personagem_dadosp[3]))
    return lanterna_colisaop


def Pega_Ladrao(lanterna_colisaop, personagem_colisaop, personagem_dadosp, jogop):
    if jogop == 0:
        if personagem_dadosp[4] == 1:
            if lanterna_colisaop.colliderect(personagem_colisaop):
                jogop = 1
            else:
                jogop = 0
        else:
            jogop = 0
    else:
        jogop = jogop
    return jogop


def Encontrar_Guarda_Desmaiado(lanterna_colisaop, personagem_colisaop, personagem_dadosp, quantidade_personagensp,
                               personagem_espp,
                               personagemp, perigop1):
    global alerta_som
    for guarp in range(1, quantidade_personagensp):
        if perigop1 == 0:
            if lanterna_colisaop.colliderect(personagem_colisaop[personagemp[guarp]]):
                if personagem_espp != personagem[guarp]:
                    if personagem_dadosp[personagemp[guarp]][4] == 0:
                        perigop = 1
                        alerta_som.play()
                        break
                    else:
                        perigop = 0
                else:
                    perigop = 0
            else:
                perigop = 0
        else:
            perigop = 1
    return perigop


def Jogando(displayp, jogop, estadop, tela_atualp, status_armap2, frase_perdeup, frase_ganhoup):
    global indice_menu, alerta_som, choque_som
    if jogop == 1:
        game_over_som.play()
        alerta_som.stop()
        choque_som.stop()
        pygame.mixer.music.stop()
        pygame.draw.rect(displayp, cor["Preto"], (110, 300, 650, 100), 0)
        displayp.blit(frase_perdeup, (130, 300))
        pygame.display.update()
        sleep(2)
        estadop = 0
        tela_atualp = 1
        status_armap = [0]
        jogop = 0
        indice_menu = 0
        if personagem_escolhido == 1:
            Descomprimir_Roberson_Imagens()
        else:
            Descomprimir_Roberval_Imagens()
    elif jogop == 2:
        alerta_som.stop()
        choque_som.stop()
        pygame.mixer.music.stop()
        pygame.draw.rect(displayp, cor["Preto"], (80, 300, 680, 100), 0)
        displayp.blit(frase_ganhoup, (100, 300))
        pygame.display.update()
        sleep(2)
        estadop = 0
        tela_atualp = 1
        status_armap = [0]
        jogop = 0
        indice_menu = 0
        if personagem_escolhido == 1:
            Descomprimir_Roberson_Imagens()
        else:
            Descomprimir_Roberval_Imagens()
    else:
        estadop = estadop
        tela_atualp = tela_atualp
        status_armap = status_armap2
    return estadop, jogop, tela_atualp, status_armap


def Fundo_Menu_Imagem(displayp, menu_fundop):
    displayp.blit(menu_fundop, (0, 0))


def Tempo_Tela(tempo_segundos_jogop):
    if tempo_segundos_jogop > 299:
        jogop = 1
    else:
        jogop = 0
    return jogop


def Mudando_Personagem(personagem_escolhidop):
    global Roberval_Vivo_load_d_e_Des, Roberval_Vivo_load_f_Des, Roberval_Vivo_load_c_Des, Roberval_Vivo_load_d_e_Arm, Roberval_Vivo_load_f_Arm
    global Roberval_Vivo_load_c_Arm, Roberson_Vivo_load_d_e_Des, Roberson_Vivo_load_f_Des, Roberson_Vivo_load_c_Des, Roberson_Vivo_load_d_e_Arm
    global Roberson_Vivo_load_f_Arm, Roberson_Vivo_load_c_Arm
    if personagem_escolhidop == 1:
        ladrao_Vivo_load_d_e_Desp = Roberval_Vivo_load_d_e_Des
        ladrao_Vivo_load_f_Desp = Roberval_Vivo_load_f_Des
        ladrao_Vivo_load_c_Desp = Roberval_Vivo_load_c_Des
        ladrao_Vivo_load_d_e_Armp = Roberval_Vivo_load_d_e_Arm
        ladrao_Vivo_load_f_Armp = Roberval_Vivo_load_f_Arm
        ladrao_Vivo_load_c_Armp = Roberval_Vivo_load_c_Arm
    else:
        ladrao_Vivo_load_d_e_Desp = Roberson_Vivo_load_d_e_Des
        ladrao_Vivo_load_f_Desp = Roberson_Vivo_load_f_Des
        ladrao_Vivo_load_c_Desp = Roberson_Vivo_load_c_Des
        ladrao_Vivo_load_d_e_Armp = Roberson_Vivo_load_d_e_Arm
        ladrao_Vivo_load_f_Armp = Roberson_Vivo_load_f_Arm
        ladrao_Vivo_load_c_Armp = Roberson_Vivo_load_c_Arm
    return ladrao_Vivo_load_d_e_Desp, ladrao_Vivo_load_f_Desp, ladrao_Vivo_load_c_Desp, ladrao_Vivo_load_d_e_Armp, ladrao_Vivo_load_f_Armp, ladrao_Vivo_load_c_Armp


def Calculo_Tempo_Pausado(status_questaop, status_questao_inicialp, tempo_inicial_pausadosp2):
    if status_questaop == 1:
        if status_questao_inicialp == 1:
            tempo_inicial_pausadosp = (int(round(time.time())) % 10000)
            status_questao_inicialp = 0
        else:
            status_questao_inicialp = 0
            tempo_inicial_pausadosp = tempo_inicial_pausadosp2
        tempo_segundos_pausadosp = (int(round(time.time())) % 10000) - tempo_inicial_pausadosp
        return status_questao_inicialp, tempo_inicial_pausadosp, tempo_segundos_pausadosp


cor = {"Vermelho": [255, 0, 0], "Verde": [0, 225, 0], "Azul": [22, 5, 185], "Amarelo": [255, 255, 0],
       "Lilas": [255, 0, 255], "Azul Bebe": [0, 255, 255], "Branco": [255, 255, 255], "Bisque3": [0, 128, 128],
       "Laranja": [255, 165, 0], "Preto": [0, 0, 0], "Cinza": [127, 127, 127]}

status_jogo = 0
status_button = 0
# Menu
estado = 0
indice_menu = 0
lista_opcoes = []
lista_opcoes.append({"text": "Jogar", "pos": [400, 365], "cor": cor["Azul"], "execute": Menu_Jogar})
lista_opcoes.append({"text": "Sobre o Jogo", "pos": [310, 445], "cor": cor["Azul"], "execute": Menu_Sobre_Jogo})
lista_opcoes.append(
    {"text": "Escolha de Personagem", "pos": [180, 525], "cor": cor["Azul"], "execute": Menu_Escolha_Personagem})
lista_opcoes.append({"text": "Sair", "pos": [420, 605], "cor": cor["Azul"], "execute": exit})

lista_opcoes_personagem = []
lista_opcoes_personagem.append(
    {"text": "Roberval", "pos": [150, 420], "cor": cor["Azul"], "execute": Roberval_Escolhido})
lista_opcoes_personagem.append(
    {"text": "Roberson", "pos": [500, 420], "cor": cor["Azul"], "execute": Roberson_Escolhido})
lista_opcoes_personagem.append(
    {"text": "Voltar", "pos": [325, 590], "cor": cor["Azul"], "execute": Menu_Principal})

lista_opcoes_sobre = []
lista_opcoes_sobre.append(
    {"text": "Historia", "pos": [350, 185], "cor": cor["Azul"], "execute": Menu_Historia})
lista_opcoes_sobre.append(
    {"text": "Regras", "pos": [360, 275], "cor": cor["Azul"], "execute": Menu_Regras})
lista_opcoes_sobre.append(
    {"text": "Como Jogar", "pos": [315, 365], "cor": cor["Azul"], "execute": Menu_Como_Jogar})
lista_opcoes_sobre.append(
    {"text": "Voltar", "pos": [360, 525], "cor": cor["Azul"], "execute": Menu_Principal})

lista_opcoes_regras = []
lista_opcoes_regras.append({"text": "Voltar", "pos": [325, 590], "cor": cor["Azul"], "execute": Menu_Sobre_Jogo})

lista_opcoes_como_jogar = []
lista_opcoes_como_jogar.append({"text": "Voltar", "pos": [325, 590], "cor": cor["Azul"], "execute": Menu_Sobre_Jogo})

lista_opcoes_historia = []
lista_opcoes_historia.append({"text": "Voltar", "pos": [325, 590], "cor": cor["Azul"], "execute": Menu_Sobre_Jogo})

lista_opcoes_questao1 = []
lista_opcoes_questao1.append({"text": "f(x) = X^4, Calcule: f'(1/2)", "pos": [280, 170], "cor": cor["Azul"]})
lista_opcoes_questao1.append(
    {"text": "a)0,5", "pos": [250, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao1.append(
    {"text": "b)1", "pos": [425, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao1.append(
    {"text": "c)1,5", "pos": [595, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})

lista_opcoes_questao2 = []
lista_opcoes_questao2.append({"text": "f(x) = x^(-3), Calcule f'(x)", "pos": [310, 170], "cor": cor["Azul"]})
lista_opcoes_questao2.append(
    {"text": "a)3x^(4)", "pos": [240, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao2.append(
    {"text": "b)-3x^(-2)", "pos": [400, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao2.append(
    {"text": "c)-3x^(-4)", "pos": [570, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})

lista_opcoes_questao3 = []
lista_opcoes_questao3.append({"text": "g(x) = 1/x, Calcule g'(x)", "pos": [320, 170], "cor": cor["Azul"]})
lista_opcoes_questao3.append(
    {"text": "a)1/x^2", "pos": [240, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao3.append(
    {"text": "b)-(1/x^2)", "pos": [395, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao3.append(
    {"text": "c)1/x^(-2)", "pos": [570, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})

lista_opcoes_questao4 = []
lista_opcoes_questao4.append({"text": "g(x) = x^2, Calcule g'(e)", "pos": [320, 170], "cor": cor["Azul"]})
lista_opcoes_questao4.append(
    {"text": "a)e^2", "pos": [245, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao4.append(
    {"text": "b)cos(e)", "pos": [405, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
lista_opcoes_questao4.append(
    {"text": "c)1/e", "pos": [585, 390], "cor": cor["Azul"], "execute": Menu_Escolha_Alternativa})
# Personagem
personagem = []
quantidade_personagens = 0
personagem_dados = {}
lista_xy = [
    # Tela 1
    [[720, 640], [10, 140], [730, 380]],
    # Tela 2
    [[0, 40], [490, 220], [250, 460], [650, 620]],
    # Tela 3
    [[720, 40], [170, 300], [570, 300], [730, 300], [410, 300]],
    # Tela 4
    [[720, 40], [410, 60], [250, 300], [90, 540], [330, 620], [650, 620]],
    # Tela 5
    [[0, 40], [410, 220], [10, 460], [730, 460], [250, 620], [570, 620]]
]
vel_dados = {}
direcao = {}
lista_direcao = [
    # Tela 1
    [270, 180],
    # Tela 2
    [180, 180, 0],
    # Tela 3
    [0, 270, 270, 180],
    # Tela 4
    [270, 90, 180, 90, 90],
    # Tela 5
    [0, 0, 180, 90, 90]
]
personagem_colisao = {}
status_dados = 1

# Ferramentas
arma = [
    # Tela 1
    [20, 220, 40, 40, cor["Lilas"]],
    # Tela 2
    [20, 620, 40, 40, cor["Lilas"]],
    # Tela 3
    [20, 620, 40, 40, cor["Lilas"]],
    # Tela 4
    [740, 620, 40, 40, cor["Lilas"]],
    # Tela 5
    [740, 60, 40, 40, cor["Lilas"]]
]
status_arma = [0]
arma_colisao = ""
lanterna_colisao = {}

saidas = [
    # Tela 1
    [20, 620, 40, 40, cor["Vermelho"]],
    # Tela 2
    [740, 60, 40, 40, cor["Vermelho"]],
    # Tela 3
    [740, 620, 40, 40, cor["Vermelho"]],
    # Tela 4
    [20, 620, 40, 40, cor["Vermelho"]],
    # Tela 5
    [420, 380, 40, 40, cor["Vermelho"]]
]
saidas_colisao = ""

# Cenario
tela_atual = 1
bloco = [
    # Tela 1
    [
        # 1º fileira
        [0, 40, 80, 80, 1], [80, 40, 80, 80, 0],
        [240, 40, 80, 80, 1], [320, 40, 80, 80, 1], [400, 40, 80, 80, 1],
        # 2º fileira
        [80, 120, 80, 80, 1],
        [560, 120, 80, 240, 0], [560, 200, 80, 80, 0], [560, 280, 80, 80, 1],
        [720, 120, 80, 80, 0], [720, 200, 80, 80, 0], [720, 280, 80, 80, 1],
        # 3º fileira
        [320, 200, 80, 80, 0], [320, 280, 80, 80, 1],
        [400, 200, 80, 80, 0], [400, 280, 80, 80, 1],
        # 4º fileira
        [0, 280, 80, 80, 1], [80, 280, 80, 80, 1], [160, 280, 80, 80, 1],
        # 5º fileira
        # 6º fileira
        [80, 440, 80, 80, 1], [160, 440, 80, 80, 1], [240, 440, 80, 80, 0],
        [400, 440, 80, 80, 0], [480, 440, 80, 80, 1],
        [640, 440, 80, 80, 0], [720, 440, 80, 80, 1],
        # 7º fileira
        [240, 520, 80, 80, 0], [240, 600, 80, 80, 1],
        [400, 520, 80, 80, 0], [400, 600, 80, 80, 1],
        [640, 520, 80, 80, 1],
        # 8º fileira
        [80, 600, 80, 80, 1]
    ],
    # Tela 2
    [
        # 1º fileira
        [160, 40, 80, 80, 0], [160, 120, 80, 80, 0], [160, 200, 80, 80, 0],
        [160, 280, 80, 80, 0], [160, 360, 80, 80, 1],
        [400, 40, 80, 160, 0], [400, 120, 80, 80, 1],
        [560, 40, 80, 80, 0], [560, 120, 80, 80, 0], [560, 200, 80, 80, 0],
        [560, 280, 80, 80, 1],
        # 2º fileira
        # 3º fileira
        [0, 200, 80, 80, 1],
        [720, 200, 80, 80, 1],
        # 4º fileira
        [320, 280, 80, 80, 0], [320, 360, 80, 80, 1], [400, 280, 80, 80, 0],
        [400, 360, 80, 80, 1],
        # 5º fileira
        [80, 360, 80, 80, 1],
        # 6º fileira
        [560, 440, 80, 80, 0], [640, 440, 80, 80, 1],
        # 7º fileira
        [80, 520, 80, 80, 0], [80, 600, 80, 80, 1],
        [320, 520, 80, 80, 0], [320, 600, 80, 80, 1],
        [560, 520, 80, 80, 0], [560, 600, 80, 80, 1],
        # 8º fileira

    ],
    # Tela 3
    [
        # 1º fileira
        [0, 40, 80, 80, 0], [80, 40, 80, 80, 1], [160, 40, 80, 80, 1],
        [560, 40, 80, 80, 1],
        # 2º fileira
        [0, 120, 80, 80, 0], [0, 200, 80, 80, 0], [0, 280, 80, 80, 0],
        [0, 360, 80, 80, 1],
        [320, 120, 80, 80, 0],
        # 3º fileira
        [240, 200, 80, 80, 1], [320, 200, 80, 80, 1], [400, 200, 80, 80, 1],
        [480, 200, 80, 80, 1],
        [560, 200, 80, 80, 1], [640, 200, 80, 80, 0], [720, 200, 80, 80, 1],
        # 4º fileira
        [640, 280, 80, 80, 0], [640, 360, 80, 80, 1],
        # 5º fileira
        [80, 360, 80, 80, 1],
        [240, 360, 80, 80, 0], [320, 360, 80, 80, 0], [240, 440, 80, 80, 1],
        [320, 440, 80, 80, 1],
        # 6º fileira
        [480, 440, 80, 80, 0], [480, 520, 80, 80, 0], [480, 600, 80, 80, 1],
        # 7º fileira
        [80, 520, 80, 80, 0], [80, 600, 80, 80, 1],
        [560, 520, 80, 80, 1],
        [720, 520, 80, 80, 1],
        # 8º fileira
        [160, 600, 80, 80, 1], [240, 600, 80, 80, 1]
    ],
    # Tela 4
    [
        # 1º fileira
        [0, 40, 240, 80, 0], [80, 40, 80, 80, 1], [160, 40, 80, 80, 1],
        [320, 40, 80, 240, 0], [320, 120, 80, 80, 0], [320, 200, 80, 80, 1],
        # 2º fileira
        [0, 120, 80, 80, 0], [0, 200, 80, 80, 0], [0, 280, 80, 80, 1],
        # 3º fileira
        [480, 200, 80, 80, 0], [560, 200, 80, 80, 0], [480, 280, 80, 80, 1],
        [560, 280, 80, 80, 1],
        # 4º fileira
        # 5º fileira
        [160, 360, 80, 80, 0], [160, 440, 80, 80, 0], [160, 520, 80, 80, 0],
        [320, 360, 80, 80, 0], [320, 440, 80, 80, 1],
        [720, 360, 80, 80, 0], [720, 440, 80, 80, 0], [720, 520, 80, 80, 1],
        # 6º fileira
        [80, 440, 80, 80, 1], [640, 440, 80, 80, 1],
        # 7º fileira
        [480, 520, 80, 80, 0],
        # 8º fileira
        [80, 600, 80, 80, 1], [160, 600, 80, 80, 1], [240, 600, 80, 80, 1],
        [400, 600, 80, 80, 1], [480, 600, 80, 80, 1], [560, 600, 80, 80, 1]
    ],
    # Tela 5
    [
        # 1º fileira
        # 2º fileira
        [240, 120, 80, 80, 0], [320, 120, 80, 80, 1], [400, 120, 80, 80, 1],
        [480, 120, 80, 80, 1], [560, 120, 80, 80, 0],
        # 3º fileira
        [80, 200, 80, 80, 1], [160, 200, 80, 80, 1], [240, 200, 80, 80, 0],
        [560, 200, 80, 80, 0], [640, 200, 80, 80, 1],
        # 4º fileira
        [240, 280, 80, 80, 0], [240, 360, 80, 80, 0], [240, 440, 80, 80, 1],
        [400, 280, 80, 80, 2],
        [560, 280, 80, 80, 0], [560, 360, 80, 80, 0], [560, 440, 80, 80, 1],
        # 5º fileira
        [0, 360, 80, 80, 1], [80, 360, 80, 80, 1],
        [720, 360, 80, 80, 1],
        # 6º fileira
        [320, 440, 80, 80, 1], [480, 440, 80, 80, 1],
        # 7º fileira
        [0, 520, 80, 80, 0], [0, 600, 80, 80, 1],
        [720, 520, 80, 80, 0],
        # 8º fileira
        [80, 600, 80, 80, 1], [160, 600, 80, 80, 1],
        [320, 600, 80, 80, 1], [400, 600, 80, 80, 1], [480, 600, 80, 80, 1],
        [640, 600, 160, 80, 1], [720, 600, 80, 80, 1]
    ]
]
seq_cont_bloc = [
    # Tela 1
    [0, 5, 12, 16, 19, 19, 26, 31, 32],
    # Tela 2
    [0, 11, 11, 13, 17, 18, 20, 26, 26],
    # Tela 3
    [0, 4, 9, 16, 18, 23, 26, 30, 32],
    # Tela 4
    [0, 6, 9, 13, 13, 21, 23, 24, 30],
    # Tela 5
    [0, 0, 5, 10, 17, 20, 22, 25, 32]
]
ponto_direcao = [
    # Tela 1
    [  # 1º fileira
        [200, 80, 1, 4], [520, 80, 2, 2], [680, 80, 3, 3], [760, 80, 1, 3],
        # 2º fileira
        [40, 160, 1, 4], [200, 160, 3, 2], [280, 160, 3, 3], [520, 160, 3, 4],
        # 3º fileira
        [40, 240, 2, 1], [200, 240, 3, 1], [280, 240, 3, 4],
        # 5º fileira
        [40, 400, 2, 2], [280, 400, 3, 1], [360, 400, 3, 3], [520, 400, 3, 1], [600, 400, 3, 3],
        [680, 400, 3, 1], [760, 400, 1, 3],
        # 6º fileira
        [40, 560, 3, 2], [200, 560, 2, 4], [520, 560, 2, 2], [600, 560, 3, 4], [760, 560, 1, 4],
        # 7º fileira
        [40, 640, 1, 2], [200, 640, 1, 2], [360, 640, 1, 2], [520, 640, 2, 1], [600, 640, 3, 1],
        # 8º fileira
        [760, 640, 2, 3]
    ],
    # Tela 2
    [
        # 1º fileira
        [40, 80, 2, 2], [120, 80, 2, 4], [280, 80, 2, 2], [360, 80, 1, 4], [520, 80, 1, 4], [680, 80, 2, 2],
        [760, 80, 2, 4],
        # 2º fileira
        [40, 160, 2, 1], [120, 160, 3, 4], [680, 160, 3, 2], [760, 160, 2, 3],
        # 3º fileira
        [280, 240, 3, 2], [360, 240, 3, 1], [520, 240, 3, 4],
        # 4º fileira
        [40, 320, 2, 2], [120, 320, 2, 3], [680, 320, 3, 2], [760, 320, 2, 4],
        # 5º fileira
        [520, 400, 3, 2], [680, 400, 3, 1], [760, 400, 3, 4],
        # 6º fileira
        [40, 480, 3, 2], [200, 480, 3, 3], [280, 480, 4], [440, 480, 3, 3], [520, 480, 3, 4],
        # 7º fileira
        [680, 560, 2, 2], [760, 560, 3, 4],
        # 8º fileira
        [40, 640, 1, 2], [200, 640, 2, 1], [280, 640, 2, 3], [440, 640, 2, 1], [520, 640, 2, 3], [680, 640, 2, 1],
        [760, 640, 2, 3]

    ],
    # Tela 3
    [
        # 1º fileira
        [280, 80, 2, 2], [440, 80, 3, 3], [520, 80, 2, 4], [680, 80, 2, 2], [760, 80, 2, 4],
        # 2º fileira
        [120, 160, 2, 2], [200, 160, 3, 3], [280, 160, 2, 3], [440, 160, 2, 1], [520, 160, 3, 1], [680, 160, 3, 1],
        [760, 160, 2, 3],
        # 3º fileira
        # 4º fileira
        [120, 320, 2, 1], [200, 320, 4], [440, 320, 3, 3], [600, 320, 2, 4], [760, 320, 1, 4],
        # 5º fileira
        [440, 400, 3, 2], [600, 400, 3, 4],
        # 6º fileira
        [40, 480, 2, 2], [200, 480, 3, 4], [600, 480, 2, 1], [680, 480, 3, 3], [760, 480, 2, 3],
        # 7º fileira
        [200, 560, 2, 1], [360, 560, 3, 3], [440, 560, 3, 4],
        # 8º fileira
        [40, 640, 1, 2], [360, 640, 2, 1], [440, 640, 2, 3], [600, 640, 1, 1], [680, 640, 3, 1], [760, 640, 1, 3],

    ],
    # Tela 4
    [
        # 1º fileira
        [280, 80, 1, 4], [440, 80, 2, 2], [680, 80, 3, 3], [760, 80, 2, 4],
        # 2º fileira
        [120, 160, 2, 2], [280, 160, 3, 4], [440, 160, 3, 2], [680, 160, 4], [760, 160, 3, 4],
        # 3º fileira
        [120, 240, 3, 2], [280, 240, 3, 4],
        # 4º fileira
        [120, 320, 3, 2], [280, 320, 4], [440, 320, 3, 4], [680, 320, 3, 2], [760, 320, 2, 3],
        # 5º fileira
        [40, 400, 2, 2], [120, 400, 2, 3], [440, 400, 3, 2], [600, 400, 3, 3], [680, 400, 2, 3],
        # 6º fileira
        [440, 480, 3, 2], [600, 480, 3, 4],
        # 7º fileira
        [40, 560, 3, 2], [120, 560, 1, 3], [280, 560, 2, 1], [360, 560, 3, 3], [440, 560, 2, 3], [600, 560, 2, 1],
        [680, 560, 2, 4],
        # 8º fileira
        [40, 640, 1, 2], [360, 640, 1, 2], [680, 640, 2, 1], [760, 640, 1, 3]
    ],
    # Tela 5
    [
        # 1º fileira
        [40, 80, 2, 2], [200, 80, 3, 3], [680, 80, 3, 3], [760, 80, 2, 4],
        # 2º fileira
        [40, 160, 3, 2], [200, 160, 2, 3], [680, 160, 2, 1], [760, 160, 3, 4],
        # 3º fileira
        [360, 240, 2, 2], [520, 240, 2, 4],
        # 4º fileira
        [40, 320, 2, 1], [200, 320, 2, 4], [680, 320, 2, 2], [760, 320, 2, 3],
        # 5º fileira
        [360, 400, 2, 1], [440, 400, 3, 3], [520, 400, 2, 3],
        # 6º fileira
        [40, 480, 1, 1], [120, 480, 3, 3], [200, 480, 3, 4], [680, 480, 3, 2], [760, 480, 1, 3],
        # 7º fileira
        [120, 560, 2, 1], [200, 560, 3, 1], [280, 560, 3, 3], [440, 560, 3, 1], [600, 560, 3, 3], [680, 560, 2, 3],
        # 8º fileira
        [280, 640, 1, 2], [600, 640, 1, 2]
    ]
]
quant__pontos = 0
parede = []
numero_bloco = 0

tempo_inicial = (int(round(time.time())) % 10000)
tempo_inicial_jogo = (int(round(time.time())) % 10000)
tempo_minutos = 0
tempo_segundos_jogo = 0
status_tempo = 0
perigo = 0
jogo = 0
os.environ['SDL_VIDEO_CENTERED'] = '1'

personagem_escolhido = 1

pygame.init()
display = pygame.display.set_mode((900, 680), 0, 32)
Roberval_Vivo_load_d_e_Des = pygame.image.load("Imagem/Roberval_Vivo_D_E_Des.png").convert_alpha()
Roberval_Vivo_load_f_Des = pygame.image.load("Imagem/Roberval_Vivo_F_Des.png").convert_alpha()
Roberval_Vivo_load_c_Des = pygame.image.load("Imagem/Roberval_Vivo_C_Des.png").convert_alpha()
Roberval_Vivo_load_d_e_Arm = pygame.image.load("Imagem/Roberval_Vivo_D_E_Arm.png").convert_alpha()
Roberval_Vivo_load_f_Arm = pygame.image.load("Imagem/Roberval_Vivo_F_Arm.png").convert_alpha()
Roberval_Vivo_load_c_Arm = pygame.image.load("Imagem/Roberval_Vivo_C_Arm.png").convert_alpha()

Roberson_Vivo_load_d_e_Des = pygame.image.load("Imagem/Roberson_Vivo_D_E_Des.png").convert_alpha()
Roberson_Vivo_load_f_Des = pygame.image.load("Imagem/Roberson_Vivo_F_Des.png").convert_alpha()
Roberson_Vivo_load_c_Des = pygame.image.load("Imagem/Roberson_Vivo_C_Des.png").convert_alpha()
Roberson_Vivo_load_d_e_Arm = pygame.image.load("Imagem/Roberson_Vivo_D_E_Arm.png").convert_alpha()
Roberson_Vivo_load_f_Arm = pygame.image.load("Imagem/Roberson_Vivo_F_Arm.png").convert_alpha()
Roberson_Vivo_load_c_Arm = pygame.image.load("Imagem/Roberson_Vivo_C_Arm.png").convert_alpha()

ladrao_Vivo_load_d_e_Des = Roberval_Vivo_load_d_e_Des
ladrao_Vivo_load_f_Des = Roberval_Vivo_load_f_Des
ladrao_Vivo_load_c_Des = Roberval_Vivo_load_c_Des
ladrao_Vivo_load_d_e_Arm = Roberval_Vivo_load_d_e_Arm
ladrao_Vivo_load_f_Arm = Roberval_Vivo_load_f_Arm
ladrao_Vivo_load_c_Arm = Roberval_Vivo_load_c_Arm



guarda_Vivo_load_d_e = pygame.image.load("Imagem/Guarda_Vivo_D_E.png").convert_alpha()
guarda_Vivo_load_f = pygame.image.load("Imagem/Guarda_Vivo_F.png").convert_alpha()
guarda_Vivo_load_c = pygame.image.load("Imagem/Guarda_Vivo_C.png").convert_alpha()
guarda_Morto_load_d_e = pygame.image.load("Imagem/Guarda_Morto_D_E.png").convert_alpha()
guarda_Morto_load_c = pygame.image.load("Imagem/Guarda_Vivo_C.png").convert_alpha()
guarda_Morto_load_f = pygame.image.load("Imagem/Guarda_Morto_F.png").convert_alpha()

icone_Roberval = pygame.transform.scale(Roberval_Vivo_load_d_e_Des, (180, 240))
icone_Roberson = pygame.transform.scale(Roberson_Vivo_load_d_e_Des, (180, 240))

bancada_completa = pygame.image.load("Imagem/BancadaCompleta.png").convert_alpha()
bancada_vidraça = pygame.image.load("Imagem/BancadaGr.png").convert_alpha()
bancada_dimante = pygame.image.load("Imagem/DiamanteBancada.png").convert_alpha()

status_armado_Img = pygame.image.load("Imagem/Icone_Com_Arma.png").convert_alpha()

status_desarmado_Img = pygame.image.load("Imagem/Icone_Sem_Arma.png").convert_alpha()


menu_fundo2 = pygame.image.load("Imagem/MenuGatun.png").convert_alpha()
menu_fundo = pygame.transform.scale(menu_fundo2, (900, 680))

alarme = pygame.image.load("Imagem/Perigo.png").convert_alpha()
alarme_rend = pygame.transform.scale(alarme, (80, 80))

teaser_chao = pygame.image.load("Imagem/Teaser.png").convert_alpha()
teaser_chao_rend = pygame.transform.scale(teaser_chao, (40, 40))

luz = pygame.image.load("Imagem/Luz.png").convert_alpha()
luz_rend = pygame.transform.scale(luz, (60, 60))

saida_Img = pygame.image.load("Imagem/Entrada.png").convert_alpha()

historia_fnd = pygame.image.load("Imagem/História.png").convert_alpha()
historia_fnd_rend = pygame.transform.scale(historia_fnd, (900, 680))
porta_fnd = pygame.image.load("Imagem/Questões.png").convert_alpha()
porta_fnd_rend = pygame.transform.scale(porta_fnd, (900, 680))
regras_fnd = pygame.image.load("Imagem/Regras.png").convert_alpha()
regras_fnd_rend = pygame.transform.scale(regras_fnd, (900, 680))
selecao_fnd = pygame.image.load("Imagem/SeleçãoPers.png").convert_alpha()
selecao_fnd_rend = pygame.transform.scale(selecao_fnd, (900, 680))
sobre_jogo_fnd = pygame.image.load("Imagem/SobreJogo.png").convert_alpha()
sobre_jogo_fnd_rend = pygame.transform.scale(sobre_jogo_fnd, (900, 680))
como_jogar_fnd = pygame.image.load("Imagem/ComoJogar.png").convert_alpha()
como_jogar_fnd_rend = pygame.transform.scale(como_jogar_fnd, (900, 680))

fonte = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 29)
fonte_menu = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 48)
fonte_gp = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 90)
fonte_questao1 = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 25)
fonte_questao2 = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 20)
fonte_questao3 = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 20)
fonte_questao4 = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 20)
frase_perdeu = fonte_gp.render("Voce Perdeu!", True, cor["Azul"])
frase_ganhou = fonte_gp.render("Voce Ganhou!", True, cor["Azul"])
frase_acertou = fonte_gp.render("Voce Acertou!", True, cor["Azul"])
frase_errou = fonte_gp.render("Voce Errou!", True, cor["Azul"])
personagem_imagem = {}
status_questao = 0
tempo_pausado = 0
total_tempo_pausado = 0
total_tempo_pausado2 = 0
tempo_inicial_pausados = 0
status_questao_inicial = 0
status_numero_guarda = 0
choque_som = pygame.mixer.Sound("Sons/Taser.ogg")
alerta_som = pygame.mixer.Sound("Sons/Som de Alerta.ogg")
porta_abrindo_som = pygame.mixer.Sound("Sons/Porta Abrindo.ogg")
porta_fechando_som = pygame.mixer.Sound("Sons/Porta Fechando.ogg")
game_over_som = pygame.mixer.Sound("Sons/Game Over 2.ogg")
pygame.mixer.music.load("Sons/Fundo_musica.ogg")
while True:
    print(personagem_dados)
    # Calcular regras
    if estado == 0:
        Calcular_Menu(lista_opcoes, fonte_menu)
    elif estado == 1:
        if status_questao == 0:
            if status_dados == 1:
                personagem, quantidade_personagens, personagem_dados, vel_dados, direcao, personagem_colisao, status_dados, personagem_imagem, numero_bloco, parede, lanterna_colisao, perigo, bloco = Construcao_de_Dados(
                    lista_xy, lista_direcao, guarda_Vivo_load_d_e, ladrao_Vivo_load_d_e_Des, tela_atual, bloco,
                    bancada_vidraça, bancada_completa, status_numero_guarda, bancada_dimante)
            for pers in range(1, quantidade_personagens):
                Velocidade_Guarda(direcao[personagem[pers]], vel_dados[personagem[pers]], perigo,
                                  personagem_dados[personagem[pers]])
            for pers in range(0, quantidade_personagens):
                Movimento(personagem_dados[personagem[pers]], vel_dados[personagem[pers]])
            quant__pontos = Quant_Pontos(ponto_direcao, tela_atual)
            for pers in range(1, quantidade_personagens):
                direcao[personagem[pers]] = Testando_pontos_direçao(tela_atual, personagem_dados[personagem[pers]],
                                                                    direcao[personagem[pers]], ponto_direcao,
                                                                    quant__pontos)
            for pers in range(0, quantidade_personagens):
                personagem_colisao[personagem[pers]] = Construcao_Personagem_Colisao(personagem_dados[personagem[pers]])
            for guar in range(1, quantidade_personagens):
                direcao[personagem[guar]] = Mudando_Direcao_Esbarrao(quantidade_personagens, personagem[guar],
                                                                     personagem,
                                                                     personagem_colisao[personagem[guar]],
                                                                     personagem_colisao,
                                                                     direcao[personagem[guar]],
                                                                     personagem_dados[personagem[guar]])

            parede = Construcao_Obstaculo_Colisao(tela_atual, bloco, numero_bloco, parede)
            arma_colisao = Construcao_Arma_Colisao(status_arma, arma, tela_atual)
            saidas_colisao = Construcao_Saida_Colisao(saidas, tela_atual)
            for pers in range(0, quantidade_personagens):
                Teste_Colisao_Blocos(personagem_dados[personagem[pers]], personagem_colisao[personagem[pers]], bloco,
                                     numero_bloco, parede, tela_atual)
            for pers in range(1, quantidade_personagens):
                Colisoes(personagem_dados[personagem[0]], personagem_colisao[personagem[0]],
                         personagem_dados[personagem[pers]],
                         personagem_colisao[personagem[pers]])
            tempo_img, status_tempo, tempo_inicial, tempo_segundos_jogo = Calculo_Tempo(
                tempo_inicial,
                status_tempo,
                fonte,
                tempo_inicial_jogo)
            for guar in range(1, quantidade_personagens):
                lanterna_colisao[personagem[guar]] = Construção_Lanterna_Colisão(direcao[personagem[guar]],
                                                                                 personagem_dados[personagem[guar]])
            for guar in range(1, quantidade_personagens):
                jogo = Pega_Ladrao(lanterna_colisao[personagem[guar]], personagem_colisao[personagem[0]],
                                   personagem_dados[personagem[guar]], jogo)
            if jogo == 0:
                jogo = Tempo_Tela(tempo_segundos_jogo)
            for guar in range(1, quantidade_personagens):
                perigo = Encontrar_Guarda_Desmaiado(lanterna_colisao[personagem[guar]], personagem_colisao,
                                                    personagem_dados,
                                                    quantidade_personagens, personagem[guar], personagem, perigo)
        else:
            status_questao_inicial, tempo_inicial_pausados, tempo_pausado = Calculo_Tempo_Pausado(status_questao,
                                                                                                  status_questao_inicial,
                                                                                                  tempo_inicial_pausados)
            Calcular_Menu(lista_opcoes_questao1, fonte_questao1)
            Calcular_Menu(lista_opcoes_questao2, fonte_questao2)
            Calcular_Menu(lista_opcoes_questao3, fonte_questao3)
            Calcular_Menu(lista_opcoes_questao4, fonte_questao4)
    elif estado == 2:
        Calcular_Menu(lista_opcoes_personagem, fonte_menu)
    elif estado == 3:
        Calcular_Menu(lista_opcoes_sobre, fonte_menu)
    elif estado == 4:
        Calcular_Menu(lista_opcoes_como_jogar, fonte_menu)
    elif estado == 5:
        Calcular_Menu(lista_opcoes_historia, fonte_menu)
    elif estado == 6:
        Calcular_Menu(lista_opcoes_regras, fonte_menu)
    # Desenhar tela

    if estado == 0:
        Fundo_Menu_Imagem(display, menu_fundo)
        Pintar_Menu(display, lista_opcoes, cor)
    elif estado == 1:
        if status_questao == 0:
            Cenario(display)
            for guar in range(1, quantidade_personagens):
                Lanterna_Imagem(display, direcao[personagem[guar]], personagem_dados[personagem[guar]], luz_rend)
            Barra(display)
            Perigo_Imagem(display, perigo, alarme_rend)
            Tempo_Imagem(display, tempo_img)
            Arma_Imagem(display, status_arma, status_armado_Img, status_desarmado_Img)
            personagem_imagem[personagem[0]] = Construcao_Personagem_Imagem(direcao[personagem[0]],
                                                                            ladrao_Vivo_load_d_e_Des,
                                                                            ladrao_Vivo_load_c_Des,
                                                                            ladrao_Vivo_load_f_Des,
                                                                            personagem_imagem[personagem[0]],
                                                                            guarda_Morto_load_d_e, guarda_Morto_load_f,
                                                                            guarda_Morto_load_c,
                                                                            personagem_dados[personagem[0]],
                                                                            ladrao_Vivo_load_d_e_Arm,
                                                                            ladrao_Vivo_load_c_Arm,
                                                                            ladrao_Vivo_load_f_Arm,
                                                                            guarda_Morto_load_d_e, guarda_Morto_load_f,
                                                                            guarda_Morto_load_c)
            for pers in range(1, quantidade_personagens):
                personagem_imagem[personagem[pers]] = Construcao_Personagem_Imagem(direcao[personagem[pers]],
                                                                                   guarda_Vivo_load_d_e,
                                                                                   guarda_Vivo_load_c,
                                                                                   guarda_Vivo_load_f,
                                                                                   personagem_imagem[personagem[pers]],
                                                                                   guarda_Morto_load_d_e,
                                                                                   guarda_Morto_load_f,
                                                                                   guarda_Morto_load_c,
                                                                                   personagem_dados[personagem[pers]],
                                                                                   guarda_Vivo_load_d_e,
                                                                                   guarda_Vivo_load_c,
                                                                                   guarda_Vivo_load_f,
                                                                                   guarda_Morto_load_d_e,
                                                                                   guarda_Morto_load_f,
                                                                                   guarda_Morto_load_c)
            Construcao_Imagem(display, tela_atual, personagem, quantidade_personagens, personagem_dados,
                              bloco, saidas, arma, teaser_chao_rend, status_arma, personagem_imagem, seq_cont_bloc,
                              saida_Img)
            estado, jogo, tela_atual, status_arma = Jogando(display, jogo, estado, tela_atual, status_arma,
                                                            frase_perdeu, frase_ganhou)
        else:
            Fundo_Menu_Imagem(display, porta_fnd_rend)
            if tela_atual == 2:
                Pintar_Menu(display, lista_opcoes_questao1, cor)
            elif tela_atual == 3:
                Pintar_Menu(display, lista_opcoes_questao2, cor)
            elif tela_atual == 4:
                Pintar_Menu(display, lista_opcoes_questao3, cor)
            elif tela_atual == 5:
                Pintar_Menu(display, lista_opcoes_questao4, cor)
    elif estado == 2:
        Fundo_Menu_Imagem(display, selecao_fnd_rend)
        display.blit(icone_Roberval, (180, 150))
        display.blit(icone_Roberson, (530, 150))
        pygame.draw.rect(display, cor["Preto"], (130, 400, 280, 80), 0)
        pygame.draw.rect(display, cor["Preto"], (480, 400, 280, 80), 0)
        pygame.draw.rect(display, cor["Preto"], (305, 570, 230, 80), 0)
        Pintar_Menu(display, lista_opcoes_personagem, cor)
    elif estado == 3:
        Fundo_Menu_Imagem(display, sobre_jogo_fnd_rend)
        pygame.draw.rect(display, cor["Preto"], (330, 175, 255, 75), 0)
        pygame.draw.rect(display, cor["Preto"], (340, 265, 225, 75), 0)
        pygame.draw.rect(display, cor["Preto"], (305, 355, 315, 75), 0)
        pygame.draw.rect(display, cor["Preto"], (350, 515, 210, 75), 0)
        Pintar_Menu(display, lista_opcoes_sobre, cor)
    elif estado == 4:
        Fundo_Menu_Imagem(display, como_jogar_fnd_rend)
        pygame.draw.rect(display, cor["Preto"], (315, 580, 210, 75), 0)
        Pintar_Menu(display, lista_opcoes_como_jogar, cor)
    elif estado == 5:
        Fundo_Menu_Imagem(display, historia_fnd_rend)
        pygame.draw.rect(display, cor["Preto"], (315, 580, 210, 75), 0)
        Pintar_Menu(display, lista_opcoes_historia, cor)
    elif estado == 6:
        Fundo_Menu_Imagem(display, regras_fnd_rend)
        pygame.draw.rect(display, cor["Preto"], (315, 580, 210, 75), 0)
        Pintar_Menu(display, lista_opcoes_regras, cor)
    pygame.display.update()
    # Capturar eventos
    Eventos(vel_dados, personagem, personagem_colisao, arma_colisao, status_arma, quantidade_personagens, direcao,
            personagem_dados, lista_opcoes, lista_opcoes_personagem, lista_opcoes_sobre, lista_opcoes_como_jogar,
            lista_opcoes_historia, tempo_pausado, lista_opcoes_questao1, lista_opcoes_questao2, lista_opcoes_questao3,
            lista_opcoes_questao4, tela_atual, lista_opcoes_regras)
    if estado == 1:
        if status_questao == 0:
            tela_atual, status_dados, jogo, status_questao, status_questao_inicial = Troca_de_Tela(tela_atual,
                                                                                                   status_dados,
                                                                                                   personagem_colisao,
                                                                                                   personagem,
                                                                                                   saidas_colisao, jogo)