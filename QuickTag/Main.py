import ctypes
import sys
import customtkinter as ctk
import os
import subprocess
import time
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
import pyautogui
import tkinter.messagebox as messagebox
import tkinter as tk
from datetime import datetime  # Importa a biblioteca para validação de datas

# Configurações iniciais do customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def validar_data(data_str):
    """ Valida se a string está no formato de data DD/MM/AAAA. """
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def verificar_datas_validas():
    validade = campo_validade.get()
    fabricacao = campo_fabricacao.get()

    if not validar_data(validade):
        messagebox.showwarning("Erro", "Data de Validade inválida. Por favor, use o formato DD/MM/AAAA.")
        return False

    if not validar_data(fabricacao):
        messagebox.showwarning("Erro", "Data de Fabricação inválida. Por favor, use o formato DD/MM/AAAA.")
        return False

    return True

def gerar_texto_pdf(produto, marca, validade, fabricacao, ingrediente):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    c.setFont("Helvetica-Bold", 7)

    c.drawString(18.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
    c.drawString(18.00 * mm, 50.00 * mm, "IDENTIFICAÇÃO DE PRODUTO")
    c.drawString(7.50 * mm, 44.50 * mm, f"PRODUTO: {produto}")
    c.drawString(7.50 * mm, 41.00 * mm, f"MARCA: {marca}")
    c.drawString(7.50 * mm, 37.00 * mm, f"DATA DE VALIDADE: {validade}")
    c.drawString(7.50 * mm, 33.00 * mm, f"DATA DE FABRICAÇÃO: {fabricacao}")
    c.drawString(7.50 * mm, 29.00 * mm, f"INGREDIENTES: {ingrediente}")

    c.save()
    buffer.seek(0)

    return buffer

def imprimir_etiqueta(produto, marca, validade, fabricacao, ingrediente):
    caminho_modelo = r"C:\Program Files (x86)\QUICKTAG\Model\Nutri_Model.pdf"

    pdf_reader = PdfReader(caminho_modelo)
    pdf_writer = PdfWriter()

    texto_pdf_buffer = gerar_texto_pdf(produto, marca, validade, fabricacao, ingrediente)
    texto_pdf_reader = PdfReader(texto_pdf_buffer)

    page = pdf_reader.pages[0]
    page.merge_page(texto_pdf_reader.pages[0])
    pdf_writer.add_page(page)

    output_dir = r"C:\Program Files (x86)\QUICKTAG\Temp"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_pdf_path = os.path.join(output_dir, "Etiqueta_Nutrição.pdf")
    
    with open(output_pdf_path, "wb") as output_file:
        pdf_writer.write(output_file)

    if os.path.exists(output_pdf_path):
        print(f"PDF gerado em: {output_pdf_path}")
    else:
        print("Erro ao gerar PDF.")

    try:
        process = subprocess.Popen([output_pdf_path], shell=True)

        time.sleep(1)

        app.iconify()
        
        pyautogui.hotkey('ctrl', 'p')
        print("Gerenciador de impressão aberto.")
    except Exception as e:
        print(f"Erro ao abrir o PDF ou gerenciador de impressão: {str(e)}")

def aplicar_configuracoes():
    produto = campo_produto.get()
    marca = campo_marca.get()
    validade = campo_validade.get()
    fabricacao = campo_fabricacao.get()
    ingrediente = campo_ingrediente.get()

    if not produto or not validade or not fabricacao:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos obrigatórios.")
        return

    if not verificar_datas_validas():
        return

    try:
        imprimir_etiqueta(produto, marca, validade, fabricacao, ingrediente)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar etiqueta: {str(e)}")

def limpar_campos():
    campo_produto.delete(0, ctk.END)
    campo_marca.delete(0, ctk.END)
    campo_validade.delete(0, ctk.END)
    campo_fabricacao.delete(0, ctk.END)
    campo_ingrediente.delete(0, ctk.END)

def formatar_data(event):
    value = event.widget.get()
    if len(value) == 2 or len(value) == 5:
        event.widget.insert(ctk.END, '/')
        event.widget.icursor(ctk.END)

def limitar_texto(entry, limite):
    def callback(event):
        if len(entry.get()) > limite:
            entry.delete(limite, tk.END)
    entry.bind('<KeyRelease>', callback)

def mostrar_ajuda():
    messagebox.showinfo("Ajuda", "Entre em contato no ramal 9800 para falar com o administrador do sistema.")

# Configurações da janela principal
app = ctk.CTk()
app.title("QUICKTAG")
app.geometry("700x300")
app.resizable(False, False)

# Criação do menu
menu_bar = tk.Menu(app)

# Menu "Ajuda"
menu_ajuda = tk.Menu(menu_bar, tearoff=0)
menu_ajuda.add_command(label="Ajuda", command=mostrar_ajuda)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

app.config(menu=menu_bar)

# Labels e Entradas com customtkinter
label_style = {'anchor': 'w'}
entry_style = {'width': 400}

ctk.CTkLabel(app, text="PRODUTO:", **label_style).grid(row=0, column=0, padx=10, pady=10)
campo_produto = ctk.CTkEntry(app, **entry_style)
campo_produto.grid(row=0, column=1, padx=10, pady=10)
limitar_texto(campo_produto, 40)

ctk.CTkLabel(app, text="MARCA:", **label_style).grid(row=1, column=0, padx=10, pady=10)
campo_marca = ctk.CTkEntry(app, **entry_style)
campo_marca.grid(row=1, column=1, padx=10, pady=10)
limitar_texto(campo_marca, 40)

ctk.CTkLabel(app, text="DATA DE VALIDADE (DD/MM/AAAA):", **label_style).grid(row=2, column=0, padx=10, pady=10)
campo_validade = ctk.CTkEntry(app, **entry_style)
campo_validade.grid(row=2, column=1, padx=10, pady=10)
campo_validade.bind("<KeyRelease>", formatar_data)
limitar_texto(campo_validade, 10)

ctk.CTkLabel(app, text="DATA DE FABRICAÇÃO (DD/MM/AAAA):", **label_style).grid(row=3, column=0, padx=10, pady=10)
campo_fabricacao = ctk.CTkEntry(app, **entry_style)
campo_fabricacao.grid(row=3, column=1, padx=10, pady=10)
campo_fabricacao.bind("<KeyRelease>", formatar_data)
limitar_texto(campo_fabricacao, 10)

ctk.CTkLabel(app, text="INGREDIENTES:", **label_style).grid(row=4, column=0, padx=10, pady=10)
campo_ingrediente = ctk.CTkEntry(app, **entry_style)
campo_ingrediente.grid(row=4, column=1, padx=10, pady=10)
limitar_texto(campo_ingrediente, 40)

botao_aplicar = ctk.CTkButton(app, text="Gerar e Imprimir", command=aplicar_configuracoes)
botao_aplicar.grid(row=7, column=0, padx=10, pady=10)

botao_limpar = ctk.CTkButton(app, text="Limpar", command=limpar_campos)
botao_limpar.grid(row=7, column=1, padx=10, pady=10)

app.mainloop()
