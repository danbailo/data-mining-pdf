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
            if text[i]=="anos":
                j = i
                while True:
                    if re.match(pattern=r".*(adiante?)",string=text[j]):
                        all_values = text[i+1:j+2].copy()

                        #VERIFICAR SE ESTA PEGANDO TODOS OS VALORES DA LINHA
                        print(all_values) #ok

                        #IDEIA 1: VERIFICAR UM CIFRAO QUE ESTA SOZINHO E UM NUMERO QUE ESTA SOZINHO E SOMAR ESSAS STRINGS E SUBSTITUIR NO LUGAR NO CIFRAO
                        #IDEIA 2: VERIFICAR OS PDFS PRA PEGAR SOMENTE O 1 TERMO DPS DAS IDADES
                        
                        #IDEIA 1
                        for i in range(len(all_values)):
                            try:
                                if re.match(pattern=r"(^R\$$)", string=all_values[i]):
                                    all_values[i] = all_values[i] + " " + (all_values[i+1])                        
                                    all_values.remove(all_values[i+1])
                            except Exception: break

                        # print(all_values) #ok

                        all_values_cipher = [value for value in all_values if re.match(pattern=r"(^R\$ ?.+\d)", string=value)]
                    
                        #print(all_values_cipher) #ok

                        joined_values = " ".join(all_values_cipher)
            
                        # print(joined_values) #tem um ' R$ ' aqui

                        values_splited = re.split(pattern=r"(R\$ \d+\,\d+)|(R\$ \d\.\d+\,\d+)", string=joined_values, flags=0)
                        # print(values_splited) #tem um ' R$ ' aqui
                        # print(values_splited)
                        all_health_values = [new_value for new_value in values_splited if new_value not in [None, '', ' ',' R$ ', 'R$']]
                        # print(all_health_values) # tem um R$ sozinho aqui

                        # print("len:",len(all_health_values))

                        health_values = []
                        try:
                            k = 0
                            while True:
                                # print(k,all_health_values[k])
                                health_values.append(all_health_values[k])
                                k += 7
                        except Exception:
                            # print("excecao")
                            if len(health_values) < 10:pass
                                # print("tamanho do health_values e menor q 10")
                                # health_values.append(all_health_values[-1])
                        


                        saude_valores.append(health_values)
                        break # para o primeiro laco
                    j += 1
        print_result(pdf, planos, regioes, saude_valores)