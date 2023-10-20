# txt-to-pdf
> Conversor de TXT para PDF recursivo em Python

## 🏁 Objetivo
Realizar a conversão de arquivos TXT em PDF, de forma recursiva a partir do diretório de execução do código.


## 💻 Pré-requisitos
Python 3 (https://www.python.org/downloads/)
FPDF (https://pyfpdf.readthedocs.io/)

Windows 
```
py -m pip install fpdf
```

Linux
```
python3 -m pip install fpdf
```

Caso esteja utilizando um proxy, adicionar:
```
--proxy=htpp://USUARIO:SENHA@URL_PROXY:PORTA
```

## 🚀 Funcionamento 
Ao executar o código, todos os arquivos TXT da pasta atual e das subpastas serão convertidos em PDF.

> Os arquivos receberão o mesmo nome do arquivo original, alterando somente a extensão.


## 💬 Informações
> Documentação da biblioteca FPDF: https://pyfpdf.readthedocs.io/

