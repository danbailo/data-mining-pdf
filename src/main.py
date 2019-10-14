import sys
from core import Pdf

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Por favor, passe somente o caminho de uma pasta que contenha os arquivos pdf's ou de um arquivo pdf!")
        print("\nExemplo:")
        print("\t python main.py CAMINHO_DA_PASTA")
        exit(-1)

    file = sys.argv[1]

    pdf = Pdf(file)
    pdf.get_result()
