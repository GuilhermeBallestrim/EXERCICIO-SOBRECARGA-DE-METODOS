from classes import *


def main():
    pass


def menu():
    while True:
        os.system("pause")
        os.system("cls")
        print("Gerador de Relatórios")
        try:
            ch = int(
                input(
                    f"\n1 - Relatório Simples (Apenas Corpo)"
                    f"\n2 - Relatório Com Título"
                    f"\n3 - Relatório Com Título e Rodapé"
                    f"\n4 - Relatório Com Título, Rodapé e Metadados"
                    f"\n0 - Sair"
                    f"\n\n---> "
                )
            )
        except ValueError:
            print("\nValor Inválido, tente novamente...")
            continue
        match ch:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 0:
                os.system("pause")
                break
            case _:
                print("Inválido, tente novamente")


menu()
