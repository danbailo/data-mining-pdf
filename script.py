import textract
import re
import os

def get_pdfs(directory):
    return os.listdir(directory)

def print_result(pdf_name, planos, regioes, saude_valores):
    print(f"PDF: {pdf_name}\n")
    
    print(f"Cálculo a ser armazenado: {calculo}")

    if len(planos) == len(regioes) == len(saude_valores):
        for i in range(len(planos)):
            print(f"Plano {planos[i]}")
            print(f"Região: {regioes[i]}")
            print(f"Saúde(R$): {saude_valores[i]}")
            print()
        print("="*100)
        print()
    else: 
        assert("Tamanho das listas dos dados são diferentes!")
        exit()

        

if __name__ == "__main__":
    
    directory = "pdfs"

    for pdf in get_pdfs(directory):    
        text = textract.process(os.path.join(directory,pdf))

        text = text.decode("utf-8").split("\n")

        calculo_pattern = re.compile(r"(Identiﬁque o cálculo a ser armazenado*)")
        plano_pattern = re.compile(r"Plano: (.*)")
        regiao_pattern = re.compile(r"Região: (.*)")
        cifrao_pattern = re.compile(r"(R\$$)")
        adiante_pattern = re.compile(r"(adiante)")
        valor_pattern = re.compile(r"R\$.*")

        for i in text:
            if i == '': text.remove(i)

        planos = []
        regioes = []
        saude_valores = []
        for i in range(len(text)):    
            if calculo_pattern.match(text[i]):
                calculo = text[i+1]
            if plano_pattern.match(text[i]):
                planos.append(plano_pattern.match(text[i])[1])
            if regiao_pattern.match(text[i]):
                regioes.append(regiao_pattern.match(text[i])[1])
            if re.match(pattern=r".*anos", string=text[i]):
                saude_valores.append(text[i+1])
            if re.match(pattern=r"(\d\d a \d\d)", string=text[i]):
                saude_valores.append(text[i+1])
            if re.match(pattern=r".*adiante", string=text[i]):
                saude_valores.append(text[i+1])                