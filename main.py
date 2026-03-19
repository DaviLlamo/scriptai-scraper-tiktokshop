import tkinter as tk
from tkinter import filedialog, messagebox
import os

from scraper import pegar_videos, salvar_excel
from roteiros import analisar_excel
from pdf import gerar_pdf

# =========================
# Funções Scraper
# =========================
def trends():
    try:
        dados = pegar_videos("trending")
        caminho = salvar_excel(dados)
        messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{caminho}")
    except Exception as e:
        print(e)
        messagebox.showerror("Erro", "Erro ao pegar trends")


def buscar():
    termo = entrada.get()
    if not termo:
        messagebox.showwarning("Aviso", "Digite algo")
        return
    try:
        dados = pegar_videos(termo)
        caminho = salvar_excel(dados)
        messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{caminho}")
    except Exception as e:
        print(e)
        messagebox.showerror("Erro", "Erro na busca")


# =========================
# Funções IA + Roteiros
# =========================
def rodar_ia():
    try:
        caminho = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
        if not caminho:
            return

        resultados = analisar_excel(caminho)

        # Print no console
        print("\n===== RESULTADOS =====")
        for r in resultados:
            print("\n🎬", r["nome"])
            print(r["roteiros"])

        messagebox.showinfo("Sucesso", "Roteiros criados!")

    except Exception as e:
        print(e)
        messagebox.showerror("Erro", "Erro ao gerar roteiro")


# =========================
# Função Gerar PDF
# =========================
def rodar_ia_pdf():
    try:
        caminho = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
        if not caminho:
            return

        resultados = analisar_excel(caminho)

        # gera PDF
        pdf_path = gerar_pdf(resultados)

        messagebox.showinfo("Sucesso", f"PDF criado em:\n{pdf_path}")

    except Exception as e:
        print(e)
        messagebox.showerror("Erro", "Erro ao gerar PDF")


# =========================
# Interface Tkinter
# =========================
app = tk.Tk()
app.title("TikTok Bot 🔥")
app.geometry("300x175")

# Botão Trends
btn_trends = tk.Button(app, text="🔥 Trends do Dia", command=trends)
btn_trends.pack(pady=10)

# Campo busca
entrada = tk.Entry(app, width=30)
entrada.pack(pady=5)

btn_buscar = tk.Button(app, text="🔎 Buscar Palavra", command=buscar)
btn_buscar.pack(pady=10)


# Botão PDF
btn_pdf = tk.Button(app, text="📄 Gerar PDF", command=rodar_ia_pdf)
btn_pdf.pack(pady=10)

# Rodar app
app.mainloop()