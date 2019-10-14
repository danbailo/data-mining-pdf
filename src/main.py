from core import Pdf
from core import Database
import datetime
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Por favor, passe somente o caminho de uma pasta que contenha os arquivos pdf's ou de um arquivo pdf!")
        print("\nExemplo:")
        print("\t python main.py CAMINHO_DA_PASTA")
        exit(-1)

    file = sys.argv[1]

    pdf = Pdf(file)
    pdf.get_result()

    # data = {
    #     "extrator": "Bradesco",
    #     "dt_extracao": datetime.datetime.now(),
    #     "campo_01": "Compulsório + de 1 titular 30 a 99 vds SP Capit. saude efeti",
    #     "campo_02": "TNOE",
    #     "campo_03": "São Paulo Capital",
    #     "campo_04":"",
    #     "campo_05":"",
    #     "campo_06":"",
    #     "faixa_01": float(' 248.61'),
    #     "faixa_02": float(' 293.36'),
    #     "faixa_03": float(' 354.96'),
    #     "faixa_04": float(' 425.96'),
    #     "faixa_05": float(' 485.59'),
    #     "faixa_06": float(' 500.16'),
    #     "faixa_07": float(' 608.97'),
    #     "faixa_08": float(' 716.27'),
    #     "faixa_09": float(' 852.37'),
    #     "faixa_10": float(' 1491.65'),
    # }

    # db = Database('daniel', "123456789")
    # db.insert_into_extracao_pdf(data)
    # db.close()
