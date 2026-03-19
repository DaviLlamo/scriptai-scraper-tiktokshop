from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def gerar_pdf(resultados):
    estilos = getSampleStyleSheet()

    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    if not os.path.exists(downloads):
        downloads = os.path.join(os.path.expanduser("~"), "Download")

    nome_arquivo = f"relatorio_tiktok_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    caminho = os.path.join(downloads, nome_arquivo)

    doc = SimpleDocTemplate(caminho)
    conteudo = []

    # título
    conteudo.append(Paragraph("Relatório de Vídeos Virais - TikTok Shop", estilos['Title']))
    conteudo.append(Spacer(1, 20))

    for item in resultados:
        video = item["nome"]
        link = item["link"]
        roteiros = item["roteiros"]

        conteudo.append(Paragraph(f"<b>Vídeo:</b> {video}", estilos['Heading2']))
        conteudo.append(Paragraph(f"<b>Link:</b> {link}", estilos['Normal']))
        conteudo.append(Spacer(1, 10))

        conteudo.append(Paragraph("<b>Roteiros:</b>", estilos['Heading3']))
        conteudo.append(Paragraph(roteiros.replace("\n", "<br/>"), estilos['Normal']))
        conteudo.append(Spacer(1, 25))

    doc.build(conteudo)
    print(f"📄 PDF gerado em: {caminho}")
    return caminho