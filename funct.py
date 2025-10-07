from classes import *
import os
import datetime


def main():
    menu()


def menu():
    while True:
        metadados = {}
        os.system("pause")
        os.system("cls")
        print("Gerador de Relatórios")
        paragrafos = []
        while True:
            texto = input(
                "Insira um parágrafo ao relatório (ou 'sair' para terminar):\n--> "
            )
            paragrafos.append(texto)
            if texto.lower() == "sair":
                break
        tt = input("Deseja inserir um título ao relatório?\n(não) ")
        if tt.lower() != "nao" or "não":
            tituloo = input("Insira seu título: \n--> ")
        else:
            tituloo == ""
        rr = input("Deseja inserir um rodapé ao relatório?\n(não) ")
        if rr.lower() != "nao" or "não":
            rodapee = input("Insira seu rodapé: \n--> ")
        else:
            rodapee == ""
        mm = input("Deseja inserir metadados ao relatório?")
        if mm.lower() != "nao" or "não":
            Autor = os.environ.get("USERNAME")
            metadados["Autor"] = Autor
            Data = datetime.datetime.today().strftime("%d/%m/%Y")
            metadados["Data"] = Data
            Versão = input("Versão do relatório (ex: v1.0): ")
            metadados["Versão"] = Versão
        relatorio_final = GerarRelatorio.Gerar(
            *paragrafos,
            titulo=tituloo,
            rodape=rodapee,
            metadados=metadados,
        )
        print("\n--- Relatório Final ---\n")
        print(relatorio_final)


menu()
