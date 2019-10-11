import textract
import re
import os

def get_pdfs(directory):
    return os.listdir(directory)

directory = "pdfs"

for pdf in get_pdfs(directory):
    os.path.join(directory,pdf)

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

                for i in range(len(all_values)):
                    try:
                        if re.match(pattern=r"(^R\$$)", string=all_values[i]):
                            all_values[i] = all_values[i] + " " + (all_values[i+1])                        
                            all_values.remove(all_values[i+1])
                    except Exception: break

                all_values_cipher = [value for value in all_values if re.match(pattern=r"(^R\$ ?.+\d)", string=value)]
            
                joined_values = " ".join(all_values_cipher)
       
                values_splited = re.split(pattern=r"(R\$ \d+\,\d+)|(R\$ \d\.\d+\,\d+)", string=joined_values, flags=0)
                all_health_values = [new_value for new_value in values_splited if new_value not in [None, '', ' ']]

                health_values = []
                try:
                    for k in range(0,len(all_health_values),7): 
                        health_values.append(all_health_values[k])
                except Exception: pass
                
                saude_valores.append(health_values)
                break # para o primeiro laco
            j += 1

print(calculo)

print(planos[0])    
print(regioes[0])    
print(saude_valores[0])

print()

print(planos[1])    
print(regioes[1])    
print(saude_valores[1])   