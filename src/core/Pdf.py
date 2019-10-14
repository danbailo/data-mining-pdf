import textract
import platform
import re
import os
from .Database import Database
import datetime

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
        self.__db = Database()
        self.__calculo_pattern = re.compile(r"(Identiﬁque o cálculo a ser armazenado*)")
        self.__plano_pattern = re.compile(r"Plano: (.*)")
        self.__regiao_pattern = re.compile(r"Região: (.*)")
        self.__saude_pattern_1 = re.compile(r"(.*anos)")
        self.__saude_pattern_2 = re.compile(r"(\d\d a \d\d)")
        self.__saude_pattern_3 = re.compile(r"(.*adiante)")
        self.__money_sign = re.compile(r"R\$")
        self.__comma = re.compile(r"\,")       
        self.__dot = re.compile(r" \d{1}(\.)")

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

    def insert_result(self, calculo, planos, regioes, saudes):
        for i in range(len(planos)):
            extracao_pdf = {
                "extrator": "Bradesco",
                "dt_extracao": datetime.datetime.now(),
                "campo_01": f"{calculo}",
                "campo_02": f"{planos[i]}",
                "campo_03": f"{regioes[i]}",
                "campo_04":"",
                "campo_05":"",
                "campo_06":"",
                "faixa_01": float(f' {saudes[i][0]}'),
                "faixa_02": float(f' {saudes[i][1]}'),
                "faixa_03": float(f' {saudes[i][2]}'),
                "faixa_04": float(f' {saudes[i][3]}'),
                "faixa_05": float(f' {saudes[i][4]}'),
                "faixa_06": float(f' {saudes[i][5]}'),
                "faixa_07": float(f' {saudes[i][6]}'),
                "faixa_08": float(f' {saudes[i][7]}'),
                "faixa_09": float(f' {saudes[i][8]}'),
                "faixa_10": float(f' {saudes[i][9]}'),
            }  
            self.__db.insert_into_extracao_pdf(extracao_pdf)
    
    def get_result(self):
        for pdf in self.get_pdfs():
            if self.get_directory():
                text = textract.process(os.path.join(self.get_directory(),pdf))
            else:
                text = textract.process(self.get_file())
                if platform.system() == "Windows": pdf = pdf.split(r"\\")[-1]
                else: pdf = pdf.split("/")[-1]
            text_splitted = text.decode("utf-8").split("\n")

            if platform.system() == "Windows":
                text_splitted = [re.sub(pattern=r"\r", repl="", string=t) for t in text_splitted]            

            for i in text_splitted:
                if i == '': text_splitted.remove(i)
            # text_splitted = [text_splitted.remove(i) for i in text_splitted if i =='']

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
                    comma = re.sub(self.__comma, ".", text_splitted[i+1])
                    money_sign = re.sub(self.__money_sign, "", comma)
                    if self.__dot.match(money_sign):
                        new_value = re.sub(r"\.", "", money_sign, count=1)
                    else: new_value = money_sign
                    saude_valores.append(new_value)

                if self.__saude_pattern_2.match(text_splitted[i]):
                    comma = re.sub(self.__comma, ".", text_splitted[i+1])
                    money_sign = re.sub(self.__money_sign, "", comma)
                    if self.__dot.match(money_sign):
                        new_value = re.sub(r"\.", "", money_sign, count=1)                    
                    else: new_value = money_sign
                    saude_valores.append(new_value)

                if self.__saude_pattern_3.match(text_splitted[i]):
                    comma = re.sub(self.__comma, ".", text_splitted[i+1])
                    money_sign = re.sub(self.__money_sign, "", comma)
                    if self.__dot.match(money_sign):
                        new_value = re.sub(r"\.", "", money_sign, count=1)
                    else: new_value = money_sign                    
                    saude_valores.append(new_value)

                if len(saude_valores) != 0 and len(saude_valores)%10 == 0:   
                    if saude_valores not in saudes:
                        saudes.append(saude_valores.copy())
                        saude_valores.clear()
            try:
                if len(saudes) == 0: continue
                self.insert_result(calculo, planos, regioes, saudes)                
                print(f'Os dados do PDF "{pdf}" foram inseridos no banco de dados com sucesso!')
              
            except Exception:
                print("ERRO: Por favor, certifique-se que este .pdf contem o mesmo que os outros padrão!")
                exit(-1)