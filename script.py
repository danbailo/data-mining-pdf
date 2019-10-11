import textract
import re
from functools import reduce

text = textract.process("exemplo_extrarcao_pdf.pdf")
# text = textract.process("opcional + 1 titu. 4 a 29 nacional hosp_1.pdf")

text = text.decode("utf-8").split("\n")

calculo_pattern = re.compile(r"(Identiﬁque o cálculo a ser armazenado*)")
plano_pattern = re.compile(r"Plano: (.*)")
regiao_pattern = re.compile(r"Região: (.*)")
cifrao_pattern = re.compile(r"(R\$$)")
adiante_pattern = re.compile(r"(adiante)")
valor_pattern = re.compile(r"R\$.*")


for i in text:
    if i == '': text.remove(i)
# print(text)
# for i in text:
#     if cifrao_pattern.match(i): text.remove(i)
# for i in text:
#     if adiante_pattern.match(i): text.remove(i)       


# exit()

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
    if text[i]=="anos":
        j = i
        while True:
            if re.match(pattern=r".*(adiante?)",string=text[j]):
                all_values = text[i+1:j+2].copy()

                print(all_values)

                exit()

                all_values_cipher = [value for value in all_values if re.match(pattern=r"(^R\$ ?.+\d)", string=value)]
            
                joined_values = " ".join(all_values_cipher)

                for number in joined_values.split():
                    if re.match(pattern=r"(\d+\,\d+)|(\d\.\d+\,\d+)", string=number):
                        print(number)

                exit()
                # test = [cipher.split() for cipher in all_values_cipher]

                # print([t[1] for t in test])

                break # para o primeiro laco
            j += 1

# print(calculo)

# print(temp)

# print(planos[0])    
# print(regioes[0])    
# print(saude_valores[0])

# print()

# print(planos[1])    
# print(regioes[1])    
# print(saude_valores[1])   