import customtkinter as ctk
import os
import subprocess
import time
from tkcalendar import Calendar
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
import pyautogui
import tkinter.messagebox as messagebox
from tkinter import Toplevel
import tkinter as tk
import re

DATE_REGEX = r"^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$"


# Configurações iniciais do customtkinter
ctk.set_appearance_mode("System")  # Modo de aparência do sistema (pode ser "Light" ou "Dark")
ctk.set_default_color_theme("blue")  # Tema de cores (pode ser "blue", "green", "dark-blue")

def gerar_texto_pdf(produto=None, unidade=None, validade1=None, validade2=None, validade3=None, validade4=None, fabricacao=None, abertura=None, ingredientes=None, refeicao=None, conservacao=None, manipulacao=None, layout=None):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 7)

    if layout == "Identificação de Produto":
        c.drawString(18.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(22.00 * mm, 50.00 * mm, "IDENTIFICAÇÃO DE PRODUTO")
        c.drawString(7.50 * mm, 44.50 * mm, f"PRODUTO: {produto}")
        c.drawString(7.50 * mm, 41.00 * mm, f"DATA DE VALIDADE: {validade1}")
        c.drawString(7.50 * mm, 37.00 * mm, f"DATA DE FABRICAÇÃO: {fabricacao}")
        c.drawString(7.50 * mm, 33.00 * mm, f"INGREDIENTES: {ingredientes}")
        c.drawString(20.00 * mm, 15.00 * mm, f"CONSUMO IMEDIATO")

    elif layout == "Refeição Acompanhante":
        c.drawString(20.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(22.00 * mm, 50.00 * mm, "REFEIÇÃO ACOMPANHANTE")
        c.drawString(7.50 * mm, 44.50 * mm, f"REFEIÇÃO: {refeicao}")
        c.drawString(7.50 * mm, 41.00 * mm, f"UNIDADE: {unidade}")
        c.drawString(7.50 * mm, 37.00 * mm, f"VALIDADE: {validade2}")
        c.drawString(20.00 * mm, 15.00 * mm, f"CONSUMO IMEDIATO")

    elif layout == "Produtos Abertos":
        c.drawString(20.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(22.00 * mm, 50.00 * mm, "PRODUTOS ABERTOS")
        c.drawString(7.50 * mm, 44.50 * mm, f"DATA DE ABERTURA: {abertura}")
        c.drawString(7.50 * mm, 41.00 * mm, f"DATA DE VALIDADE: {validade3}")
        c.drawString(7.50 * mm, 37.00 * mm, f"CONSERVAÇÃO: {conservacao}")

    elif layout == "Produtos Perecíveis":
        c.drawString(20.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(22.00 * mm, 50.00 * mm, "PRODUTOS PERECÍVEIS")
        c.drawString(7.50 * mm, 44.50 * mm, f"PRODUTO: {produto}")
        c.drawString(7.50 * mm, 41.00 * mm, f"DATA DE MANIPULAÇÃO: {manipulacao}")
        c.drawString(7.50 * mm, 37.00 * mm, f"DATA DE VALIDADE: {validade4}")

    c.save()
    buffer.seek(0)
    return buffer
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 7)

    if layout == "Identificação de Produto":
        c.drawString(18.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(20.00 * mm, 50.00 * mm, "IDENTIFICAÇÃO DE PRODUTO")
        c.drawString(7.50 * mm, 44.50 * mm, f"PRODUTO: {produto}")
        c.drawString(7.50 * mm, 41.00 * mm, f"DATA DE VALIDADE: {validade1}")
        c.drawString(7.50 * mm, 37.00 * mm, f"DATA DE FABRICAÇÃO: {fabricacao}")
        c.drawString(7.50 * mm, 33.00 * mm, f"INGREDIENTES: {ingredientes}")
        c.drawString(20.00 * mm, 15.00 * mm, f"CONSUMO IMEDIATO")

    elif layout == "Refeição Acompanhante":
        c.drawString(20.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(20.00 * mm, 50.00 * mm, "REFEIÇÃO ACOMPANHANTE")
        c.drawString(7.50 * mm, 44.50 * mm, f"REFEIÇÃO: {refeicao}")
        c.drawString(7.50 * mm, 41.00 * mm, f"UNIDADE: {unidade}")
        c.drawString(7.50 * mm, 37.00 * mm, f"VALIDADE: {validade2}")
        c.drawString(22.00 * mm, 15.00 * mm, f"CONSUMO IMEDIATO")

    elif layout == "Produtos Abertos":
        c.drawString(20.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(22.00 * mm, 50.00 * mm, "PRODUTOS ABERTOS")
        c.drawString(7.50 * mm, 44.50 * mm, f"DATA DE ABERTURA: {abertura}")
        c.drawString(7.50 * mm, 41.00 * mm, f"DATA DE VALIDADE: {validade3}")
        c.drawString(7.50 * mm, 37.00 * mm, f"CONSERVAÇÃO: {conservacao}")

    elif layout == "Produtos Perecíveis":
        c.drawString(20.00 * mm, 54.00 * mm, "SANTA CASA DA BAHIA - HSI")
        c.drawString(22.00 * mm, 50.00 * mm, "PRODUTOS PERECÍVEIS")
        c.drawString(7.50 * mm, 44.50 * mm, f"PRODUTO: {produto}")
        c.drawString(7.50 * mm, 41.00 * mm, f"DATA DE MANIPULAÇÃO: {manipulacao}")
        c.drawString(7.50 * mm, 37.00 * mm, f"DATA DE VALIDADE: {validade4}")
        c.drawString(7.50 * mm, 33.00 * mm, f"CONSERVAÇÃO: {conservacao}")

    c.save()
    buffer.seek(0)
    return buffer

def imprimir_etiqueta(produto, unidade, validade1, validade2, validade3, validade4, Fabricacao, abertura, ingredientes, refeicao, conservacao, manipulacao, layout):
    caminho_modelo = r"PYTHON/QuickTAG/Nutri_Model.pdf"
    
    pdf_reader = PdfReader(caminho_modelo)
    pdf_writer = PdfWriter()

    texto_pdf_buffer = gerar_texto_pdf(produto, unidade, validade1, validade2, validade3, validade4, Fabricacao, abertura, ingredientes, refeicao, conservacao, manipulacao, layout)
    texto_pdf_reader = PdfReader(texto_pdf_buffer)

    # Garanta que você está acessando a página correta
    page = pdf_reader.pages[0]
    page.merge_page(texto_pdf_reader.pages[0])  # Certifique-se de que ambas as páginas estão do mesmo tamanho

    pdf_writer.add_page(page)

    output_dir = r"PYTHON/QuickTAG/"
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
    layout = layout_var.get()

    # Inicializa as variáveis como None
    produto = None
    unidade = None
    validade1 = None
    validade2 = None
    validade3 = None
    validade4 = None
    fabricacao = None
    ingredientes = None
    abertura = None
    refeicao = None
    conservacao = None
    manipulacao = None

    try:
        if layout == "Identificação de Produto":
            produto = campo_produto.get()
            validade1 = campo_validade1.get()
            fabricacao = campo_fabricacao.get()
            ingredientes = campo_ingredientes.get()
            # Corrigindo a chamada
            pdf = gerar_texto_pdf(produto=produto, validade1=validade1, fabricacao=fabricacao, ingredientes=ingredientes, layout=layout)
        
        elif layout == "Refeição Acompanhante":
            refeicao = campo_refeicao.get()
            unidade = campo_unidade.get()
            validade2 = campo_validade2.get()
            pdf = gerar_texto_pdf(unidade=unidade, validade2=validade2, refeicao=refeicao, layout=layout)
        
        elif layout == "Produtos Abertos":
            abertura = campo_abertura.get()
            validade3 = campo_validade3.get()
            conservacao = campo_conservacao.get()
            pdf = gerar_texto_pdf(abertura=abertura, validade3=validade3, conservacao=conservacao, layout=layout)
        
        elif layout == "Produtos Perecíveis":
            produto = campo_produto.get()
            manipulacao = campo_manipulacao.get()
            validade4 = campo_validade4.get()
            conservacao = campo_conservacao.get()
            pdf = gerar_texto_pdf(produto=produto, validade4=validade4, conservacao=conservacao, manipulacao=manipulacao, layout=layout)

        # Verifica se pdf foi gerado antes de imprimir
        if pdf:
            # Chama a função para imprimir a etiqueta
            imprimir_etiqueta(produto, unidade, validade1, validade2, validade3, validade4, fabricacao, abertura, ingredientes, refeicao, conservacao, manipulacao, layout)
            messagebox.showinfo("Impressão", "Etiqueta gerada com sucesso.")
        else:
            messagebox.showwarning("Atenção", "Falha ao gerar o PDF.")

    except TypeError as te:
        messagebox.showerror("Erro de Tipo", f"Erro ao gerar etiqueta: {str(te)}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar etiqueta: {str(e)}")

def limpar_campos():
    # Função para limpar todos os campos de entrada
    for frame in layout_frames.values():
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkEntry):
                widget.delete(0, ctk.END)

def abrir_calendario(entry):
    def selecionar_data():
        entry.delete(0, ctk.END)
        entry.insert(0, cal.selection_get().strftime('%d/%m/%Y'))
        top.destroy()

    # Criação da janela modal para o calendário
    top = ctk.CTkToplevel(app)
    top.geometry("300x300")
    top.title("Selecione a Data")
    top.grab_set()

    # Frame para o calendário
    frame_calendario = ctk.CTkFrame(top)
    frame_calendario.pack(pady=10, padx=10, fill="both", expand=True)

    # Widget do calendário com nomes em português
    cal = Calendar(frame_calendario, selectmode="day", date_pattern="dd/mm/yyyy",
                   locale='pt_BR',  # Definindo o locale para português
                   showweeknumbers=False)
    cal.pack(pady=20)

    # Botão de seleção da data
    btn_confirmar = ctk.CTkButton(top, text="Selecionar Data", command=selecionar_data)
    btn_confirmar.pack(pady=10)

def limitar_texto(entry, limite):
    """ Limita o número de caracteres em um campo de entrada. """
    if len(entry.get()) > limite:
        entry.delete(limite, ctk.END)

def mostrar_ajuda():
    messagebox.showinfo("Ajuda", "Entre em contato no ramal 9800 para falar com o administrador do sistema.")

def mudar_layout(layout):
    # Esconde todos os frames de layout
    for frame in layout_frames.values():
        frame.pack_forget()

    # Mostra o frame correspondente ao layout selecionado
    layout_frames[layout].pack(pady=10)

# Configurações da janela principal
app = ctk.CTk() 
app.title("QUICKTAG")
app.geometry("700x400")
app.resizable(False, False)

# Criação do menu
menu_bar = tk.Menu(app)
menu_ajuda = tk.Menu(menu_bar, tearoff=0)
menu_ajuda.add_command(label="Ajuda", command=mostrar_ajuda)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)
app.config(menu=menu_bar)

# Labels e Entradas com customtkinter
label_style = {'anchor': 'w'}
entry_style = {'width': 400}

# Dropdown para selecionar layout
layout_var = tk.StringVar(value="Identificação de Produto")
layout_dropdown = ctk.CTkOptionMenu(app, variable=layout_var, values=["Identificação de Produto", "Refeição Acompanhante", "Produtos Abertos", "Produtos Perecíveis"], command=mudar_layout)
layout_dropdown.pack(pady=10)

# Frames para diferentes layouts
layout_frames = {}

# Frame para Identificação de Produto
frame_identificacao = ctk.CTkFrame(app)
layout_frames["Identificação de Produto"] = frame_identificacao
frame_identificacao.pack(pady=10)

ctk.CTkLabel(frame_identificacao, text="Produto:", **label_style).grid(row=0, column=0, padx=10, pady=10)
campo_produto = ctk.CTkEntry(frame_identificacao, **entry_style)
campo_produto.grid(row=0, column=1, padx=10, pady=10)
limitar_texto(campo_produto, 40)

ctk.CTkLabel(frame_identificacao, text="Data de Validade (DD/MM/AAAA):", **label_style).grid(row=1, column=0, padx=10, pady=10)
campo_validade1 = ctk.CTkEntry(frame_identificacao, **entry_style)
campo_validade1.grid(row=1, column=1, padx=10, pady=10)
btn_calendar = ctk.CTkButton(frame_identificacao, text="📅", width=40, command=lambda: abrir_calendario(campo_validade1))
btn_calendar.grid(row=1, column=2, padx=10, pady=10)
limitar_texto(campo_validade1, 10)

ctk.CTkLabel(frame_identificacao, text="Data de Fabricação (DD/MM/AAAA):", **label_style).grid(row=2, column=0, padx=10, pady=10)
campo_fabricacao = ctk.CTkEntry(frame_identificacao, **entry_style)
campo_fabricacao.grid(row=2, column=1, padx=10, pady=10)
btn_calendar = ctk.CTkButton(frame_identificacao, text="📅", width=40, command=lambda: abrir_calendario(campo_fabricacao))
btn_calendar.grid(row=2, column=2, padx=10, pady=10)
limitar_texto(campo_fabricacao, 10)

ctk.CTkLabel(frame_identificacao, text="Ingredientes:", **label_style).grid(row=3, column=0, padx=10, pady=10)
campo_ingredientes = ctk.CTkEntry(frame_identificacao, **entry_style)
campo_ingredientes.grid(row=3, column=1, padx=10, pady=10)
limitar_texto(campo_ingredientes, 40)

botao_aplicar = ctk.CTkButton(frame_identificacao, text="Gerar e Imprimir", command=aplicar_configuracoes)
botao_aplicar.grid(row=7, column=0, padx=10, pady=20)

botao_limpar = ctk.CTkButton(frame_identificacao, text="Limpar Campos", command=limpar_campos)
botao_limpar.grid(row=7, column=1, padx=10, pady=20)

# Frame para Refeição Acompanhante
frame_refeicao = ctk.CTkFrame(app)
layout_frames["Refeição Acompanhante"] = frame_refeicao
frame_refeicao.pack(pady=10)

ctk.CTkLabel(frame_refeicao, text="Refeição:", **label_style).grid(row=0, column=0, padx=10, pady=10)
campo_refeicao = ctk.CTkEntry(frame_refeicao, **entry_style)
campo_refeicao.grid(row=0, column=1, padx=10, pady=10)
limitar_texto(campo_refeicao, 40)

ctk.CTkLabel(frame_refeicao, text="Unidade:", **label_style).grid(row=1, column=0, padx=10, pady=10)
campo_unidade = ctk.CTkEntry(frame_refeicao, **entry_style)
campo_unidade.grid(row=1, column=1, padx=10, pady=10)
limitar_texto(campo_unidade, 40)

ctk.CTkLabel(frame_refeicao, text="Data de Validade (DD/MM/AAAA):", **label_style).grid(row=2, column=0, padx=10, pady=10)
campo_validade2 = ctk.CTkEntry(frame_refeicao, **entry_style)
campo_validade2.grid(row=2, column=1, padx=10, pady=10)
btn_calendar = ctk.CTkButton(frame_refeicao, text="📅", width=40, command=lambda: abrir_calendario(campo_validade2))
btn_calendar.grid(row=2, column=2, padx=10, pady=10)
limitar_texto(campo_validade2, 10)

botao_aplicar_refeicao = ctk.CTkButton(frame_refeicao, text="Gerar e Imprimir", command=aplicar_configuracoes)
botao_aplicar_refeicao.grid(row=7, column=0, padx=10, pady=20)

botao_limpar_refeicao = ctk.CTkButton(frame_refeicao, text="Limpar Campos", command=limpar_campos)
botao_limpar_refeicao.grid(row=7, column=1, padx=10, pady=20)

# Frame para Produtos Abertos
frame_abertos = ctk.CTkFrame(app)
layout_frames["Produtos Abertos"] = frame_abertos
frame_abertos.pack(pady=10)

ctk.CTkLabel(frame_abertos, text="Data de Abertura (DD/MM/AAAA):", **label_style).grid(row=0, column=0, padx=10, pady=10)
campo_abertura = ctk.CTkEntry(frame_abertos, **entry_style)
campo_abertura.grid(row=0, column=1, padx=10, pady=10)
btn_calendar = ctk.CTkButton(frame_abertos, text="📅", width=40, command=lambda: abrir_calendario(campo_abertura))
btn_calendar.grid(row=0, column=2, padx=10, pady=10)
limitar_texto(campo_abertura, 10)

ctk.CTkLabel(frame_abertos, text="Data de Validade (DD/MM/AAAA):", **label_style).grid(row=1, column=0, padx=10, pady=10)
campo_validade3 = ctk.CTkEntry(frame_abertos, **entry_style)
campo_validade3.grid(row=1, column=1, padx=10, pady=10)
btn_calendar = ctk.CTkButton(frame_abertos, text="📅", width=40, command=lambda: abrir_calendario(campo_validade3))
btn_calendar.grid(row=1, column=2, padx=10, pady=10)
limitar_texto(campo_validade3, 10)

ctk.CTkLabel(frame_abertos, text="Conservação:", **label_style).grid(row=2, column=0, padx=10, pady=10)
campo_conservacao = ctk.CTkEntry(frame_abertos, **entry_style)
campo_conservacao.grid(row=2, column=1, padx=10, pady=10)
limitar_texto(campo_conservacao, 40)

botao_aplicar_abertos = ctk.CTkButton(frame_abertos, text="Gerar e Imprimir", command=aplicar_configuracoes)
botao_aplicar_abertos.grid(row=7, column=0, padx=10, pady=20)

botao_limpar_abertos = ctk.CTkButton(frame_abertos, text="Limpar Campos", command=limpar_campos)
botao_limpar_abertos.grid(row=7, column=1, padx=10, pady=20)

# Frame para Produtos Perecíveis
frame_periciveis = ctk.CTkFrame(app)
layout_frames["Produtos Perecíveis"] = frame_periciveis
frame_periciveis.pack(pady=10)

ctk.CTkLabel(frame_periciveis, text="Produto:", **label_style).grid(row=0, column=0, padx=10, pady=10)
campo_produto_pericivel = ctk.CTkEntry(frame_periciveis, **entry_style)
campo_produto_pericivel.grid(row=0, column=1, padx=10, pady=10)
limitar_texto(campo_produto_pericivel, 40)

ctk.CTkLabel(frame_periciveis, text="Data de Manipulação:", **label_style).grid(row=1, column=0, padx=10, pady=10)
campo_manipulacao = ctk.CTkEntry(frame_periciveis, **entry_style)
campo_manipulacao.grid(row=1, column=1, padx=10, pady=10)
btn_calendar = ctk.CTkButton(frame_periciveis, text="📅", width=40, command=lambda: abrir_calendario(campo_manipulacao))
btn_calendar.grid(row=1, column=2, padx=10, pady=10)
limitar_texto(campo_manipulacao, 10)

ctk.CTkLabel(frame_periciveis, text="Data de Validade (DD/MM/AAAA):", **label_style).grid(row=2, column=0, padx=10, pady=10)
campo_validade4 = ctk.CTkEntry(frame_periciveis, **entry_style)
campo_validade4.grid(row=2, column=1, padx=10, pady=10)
btn_calendar = ctk.CTkButton(frame_periciveis, text="📅", width=40, command=lambda: abrir_calendario(campo_validade4))
btn_calendar.grid(row=2, column=2, padx=10, pady=10)
limitar_texto(campo_validade4, 10)

ctk.CTkLabel(frame_periciveis, text="Conservação:", **label_style).grid(row=3, column=0, padx=10, pady=10)
campo_conservacao_pericivel = ctk.CTkEntry(frame_periciveis, **entry_style)
campo_conservacao_pericivel.grid(row=3, column=1, padx=10, pady=10)
limitar_texto(campo_conservacao_pericivel, 40)

botao_aplicar_periciveis = ctk.CTkButton(frame_periciveis, text="Gerar e Imprimir", command=aplicar_configuracoes)
botao_aplicar_periciveis.grid(row=7, column=0, padx=10, pady=20)

botao_limpar_periciveis = ctk.CTkButton(frame_periciveis, text="Limpar Campos", command=limpar_campos)
botao_limpar_periciveis.grid(row=7, column=1, padx=10, pady=20)

layout_frames["Identificação de Produto"].pack(pady=10)

mudar_layout(layout_var.get())

# Executar a aplicação
app.mainloop()
