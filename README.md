# Mineração de dados - PDF's

## Descrição
Este projeto consiste em coletar alguns dados especificados pelo cliente de determinados arquivos `.pdfs`.

---
## Requisitos

* `Python 3`
* `pip (Gerenciador de pacotes do Python)`

---
## Dependências

Para instalar as dependências, execute os comandos abaixo num terminal/prompt de comando:

* Linux
  * `python3 -m pip install -r requirements.txt --user`

* Windows
  * `python -m pip install -r requirements.txt --user`

---
## Como usar

Para executar o programa, abra um terminal/prompt de comando aberto, e como parâmetro de execução do mesmo, é preciso passar o caminho da pasta ou do arquivo `.pdf`:
* `cd src/`
    * Linux
    * **Helper**
    * `python3 main.py -h`
    * **Executa o programa lendo um ou mais pdf que esteja dentro da pasta, exemplo:**
    * `python3 main.py -f ../pdfs/`
    * **Executa o programa lendo diretamente determinado pdf, exemplo:**
    * `python3 main.py -f ../pdfs/exemplo_extrarcao_pdf.pdf`

    * Windows
    * **Helper**
    * `python main.py -h`
    * **Executa o programa lendo um ou mais pdf que esteja dentro da pasta, exemplo:**
    * `python main.py -f "..\\pdfs\\"`
    * **Executa o programa lendo diretamente determinado pdf, exemplo:**
    * `python main.py -f "..\\pdfs\\exemplo_extrarcao_pdf.pdf"`

Caso uma pasta que contenha mais de um tipo de arquivo seja passada como parâmetro, o programa só irá pegar os arquivos que são `.pdfs`.

---