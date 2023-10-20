# Código para gerar um arquivo PDF de uma página, a partir de um arquivo TXT.
# O comando será realizado recursivamente em todos os arquivos TXT da pasta atual e subpastas
# Será utilizada a biblioteca FPDF - https://pyfpdf.readthedocs.io/

import os
from fpdf import FPDF

root = os.path.dirname(os.path.realpath(__file__)) # utilizará o diretório atual como raiz da pesquisa de TXT
font_size = 12
pageMargin = 0 # mm
px_to_mm = 0.2645833 # fator de conversão de px para mm - está relacionado também com o PPI desejado
widthHeightRatio = 1.4145 # proporção entre largura e altura
font = "Courier" # Courier é uma fonte monoespaçada, evitando problemas com o tamanho da página

for path, subdirs, files in os.walk(root):
    for name in files:
        fileExtension = name[-3:]
        if fileExtension.lower() == "txt":
            inputFile = os.path.join(path, name)
            destFile = os.path.join(path, name[0 : -4]+'.pdf')
            
            # Calcular a maior linha (em caracteres) do arquivo, que ditará o tamanho da página
            maxLineSize = 0
            f = open(inputFile, "r")
            for x in f:
                if len(x) > maxLineSize:
                    maxLineSize = len(x)
            
            # Calcular a largura da página em decorrência do tamanho da maior linha,
            # evitando que o texto fique cortado.
            # A altura da página é proporcional à largura.
            # Caso a largura e altura sejam menores que o tamanho padrão da folha A4,
            # adotar o tamanho do A4 para o arquivo atual.
            pageWidth = round(maxLineSize * font_size * px_to_mm)
            pageHeight = round(pageWidth * widthHeightRatio)
            if pageWidth < 210 or pageHeight < 297:
                pageWidth = 210
                pageHeight = 297
            
            # Criar o PDF
            pdf = FPDF('P', 'mm', [pageWidth + pageMargin, pageHeight + pageMargin])
            pdf.add_page()
            pdf.set_font(font, size = font_size)
            f = open(inputFile, "r")
            for x in f:
                # Replace para um caracter constante no TXT que não estava convertendo corretamente
                # provavelmente por erro de codificação no arquivo original.
                # 
                linha = x.replace('Ã‡', 'Ç')
                
                # Exportar para o PDF
                pdf.cell(200, 10, txt = linha, ln = 1)
            
            # gerar o arquivo PDF
            pdf.output(destFile)