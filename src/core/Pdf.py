import textract
import re
import os

class Pdf:
    def __init__(self, file = None):
        if file is None: 
            print("ERRO: Por favor, entre com um arquivo ou um diretório!")
            exit(-1)
        if os.path.isfile(file):
            self.__file = file
            self.__directory = None  
        if os.path.isdir(file):
            self.__directory = file  
            self.__file = None
        self.__calculo_pattern = re.compile(r"(Identiﬁque o cálculo a ser armazenado*)")
        self.__plano_pattern = re.compile(r"Plano: (.*)")
        self.__regiao_pattern = re.compile(r"Região: (.*)")
        self.__saude_pattern_1 = re.compile(r"(.*anos)")
        self.__saude_pattern_2 = re.compile(r"(\d\d a \d\d)")
        self.__saude_pattern_3 = re.compile(r"(.*adiante)")

    def get_directory(self):
        return self.__directory

    def get_file(self):
        return self.__file

    def get_pdfs(self):
        if self.get_directory():
            return [pdf for pdf in os.listdir(self.get_directory()) if pdf[-4:] =='.pdf']
        else:
            if self.get_file()[-4:] != '.pdf':
                print("ERRO: Por favor, passe um arquivo .pdf!")
                exit(-1)
            return [self.get_file()]

    def print_result(self, pdf, calculo, planos, regioes, saudes):
        print(f"PDF: {pdf}\n")
        
        print(f"Cálculo a ser armazenado: {calculo}")

        if len(planos) == len(regioes) == len(saudes):
            for i in range(len(planos)):
                print(f"Plano: {planos[i]}")
                print(f"Região: {regioes[i]}")
                print(f"Saúde(R$): {saudes[i]}")    
                print()
            print("="*100)
            print()
        else: 
            print("ERRO: Tamanho das listas dos dados são diferentes!")
            exit(-1)
    
    def get_result(self):

        for pdf in self.get_pdfs():
            if self.get_directory():
                text = textract.process(os.path.join(self.get_directory(),pdf))
            else:
                text = textract.process(self.get_file())
            text_splitted = text.decode("utf-8").split("\n")

            for i in text_splitted:
                if i == '': text_splitted.remove(i)

            planos = []
            regioes = []
            saudes = []
            saude_valores = []
            for i in range(len(text_splitted)):  
                if self.__calculo_pattern.match(text_splitted[i]):
                    calculo = text_splitted[i+1]

                plano = self.__plano_pattern.match(text_splitted[i])
                if plano:
                    planos.append(plano[1])
                regiao = self.__regiao_pattern.match(text_splitted[i])
                if regiao:
                    regioes.append(regiao[1])

                if self.__saude_pattern_1.match(text_splitted[i]):
                    saude_valores.append(text_splitted[i+1])

                if self.__saude_pattern_2.match(text_splitted[i]):
                    saude_valores.append(text_splitted[i+1])

                if self.__saude_pattern_3.match(text_splitted[i]):
                    saude_valores.append(text_splitted[i+1])  

                if len(saude_valores) != 0 and len(saude_valores)%10 == 0:   
                    if saude_valores not in saudes:
                        saudes.append(saude_valores.copy())
                        saude_valores.clear()
            try:
                if len(saudes) == 0: continue
                self.print_result(pdf, calculo, planos, regioes, saudes)
            except Exception:
                print("ERRO: Por favor, certifique-se que este .pdf contem o mesmo que os outros padrão!")
                exit(-1)