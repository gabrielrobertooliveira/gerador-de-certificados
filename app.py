# Importando as bibliotecas
import pandas as pd
from fpdf import FPDF

# Salvando a tabela em uma variável
dadosAlunos = pd.read_csv("alunos.csv")

# Dados do certificado
titulo = 'CERTIFICADO DE PARTICIPAÇÃO'
subtitulo = 'Este certificado comprova que'
texto2 = 'concluiu o curso gratuito de GERADOR DE CERTIFICADOS PYTHON'
texto3 = 'aplicado ente 10/02/2025 e 14/02/2025, com carga horária de 24 horas.'

for nome in dadosAlunos['nomecompleto']:
    pdf = FPDF(orientation='L')
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=18)
    pdf.image("Certificado-modelo.png", x=0, y=0)
    pdf.set_text_color(33, 24, 136)
 
    pdf.text(95, 100, titulo)
    pdf.text(75, 145, subtitulo)
    pdf.text(169, 145, nome)
    pdf.text(45, 155, texto2)
    pdf.text(45, 165, texto3)

    pdf.output(f'certificados/Certificado_{nome}.pdf')