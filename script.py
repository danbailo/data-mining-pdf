import textract
import re
import os

def get_pdfs(directory):
    return os.listdir(directory)

def get_result(pdf_name, planos, regioes, saude):
    print(f"PDF: {pdf_name}\n")
    
    print(f"Cálculo a ser armazenado: {calculo}")

    if len(planos) == len(regioes) == len(saude):
        for i in range(len(planos)):
            print(f"Plano {planos[i]}")
            print(f"Região: {regioes[i]}")
            print(f"Saúde(R$): {saude[i]}")
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
        saude_pattern_1 = re.compile(r"(.*anos)")
        saude_pattern_2 = re.compile(r"(\d\d a \d\d)")
        saude_pattern_3 = re.compile(r"(.*adiante)")

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

            elif saude_pattern_1.match(text[i]):
                saude_valores.append(text[i+1])

            elif saude_pattern_2.match(text[i]):
                saude_valores.append(text[i+1])

            elif saude_pattern_3.match(text[i]):
                saude_valores.append(text[i+1])  

            elif len(saude_valores) != 0 and len(saude_valores)%10 == 0:   
                if saude_valores not in saude:
                    saude.append(saude_valores.copy())
                    saude_valores.clear()
                    
        get_result(pdf, planos, regioes, saude)