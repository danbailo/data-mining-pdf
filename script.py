import textract
import re
import os

def get_pdfs(directory):
    return os.listdir(directory)

if __name__ == "__main__":
    
    directory = "pdfs"

    for pdf in get_pdfs(directory):    
        text = textract.process(os.path.join(directory,pdf))

        text = text.decode("utf-8").split("\n")

        calculo_pattern = re.compile(r"(Identiﬁque o cálculo a ser armazenado*)")
        plano_pattern = re.compile(r"Plano: (.*)")
        regiao_pattern = re.compile(r"Região: (.*)")
        cifrao_pattern = re.compile(r"(R\$$)")

        saude_pattern_1 = re.compile(r"(.*anos)")
        saude_pattern_1 = re.compile(r"(\d\d a \d\d)")
        saude_pattern_1 = re.compile(r"(.*adiante)")

        for i in text:
            if i == '': text.remove(i)

        planos = []
        regioes = []
        saude = []
        saude_valores = []
        for i in range(len(text)):  
            if calculo_pattern.match(text[i]):
                calculo = text[i+1]
            elif plano_pattern.match(text[i]):
                planos.append(plano_pattern.match(text[i])[1])
            elif regiao_pattern.match(text[i]):
                regioes.append(regiao_pattern.match(text[i])[1])
            elif re.match(pattern=r"(.*anos)", string=text[i]):
                saude_valores.append(text[i+1])
            elif re.match(pattern=r"(\d\d a \d\d)", string=text[i]):
                saude_valores.append(text[i+1])
            elif re.match(pattern=r"(.*adiante)", string=text[i]):
                saude_valores.append(text[i+1])  
            elif len(saude_valores) != 0 and len(saude_valores)%10 == 0:   
                if saude_valores not in saude:
                    saude.append(saude_valores.copy())
                    saude_valores.clear()
        # print(saude)
        print(f"Nome do arquivo: {pdf}\n")
        print(f"Cálculo a ser armazenado: {calculo}")
        print(f"Plano {planos}")
        print(f"Região: {regioes}")
        print(f"Saúde(R$): {saude_valores}\n")
        print("="*100)
        print()