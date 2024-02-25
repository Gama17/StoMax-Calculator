#main.py
import calculator
import customtkinter as tk

def calculate(dividendYeld):
    averageDiv = calculator.averageDiv(numPayments, *payments)
    dividendYeld = float(dividendYeld)
    calculator.maxPrice(dividendYeld,averageDiv)

def insertValues():
    global numPayments
    numPayments = int(entrada1.get())
    for i in range(numPayments):
        entrada2 = tk.CTkEntry(master=frame, placeholder_text="Valor do dividendo:")      #Cria uma pequena janela para inserir o valor do Dividendo por Cota
        entrada2.pack(pady=12, padx=10)     #Define a posição da caixa de inserção do valor do Dividendo por Cota
        entries.append(entrada2)
    for entry in entries:
        payments.append(float(entry.get()))
    
def onCalculateClick():
    dividendYeld = entrada3.get()
    calculate(dividendYeld)

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

window = tk.CTk()                                                                       #Cria a janela "window"
window.geometry("800x500")                                                              #Define as dimensões padrão da janela
window.title("StoMax Calculator")                                                       #Define o título da janela
label = tk.CTkLabel(window, text="Welcome to StoMax Calculator!", font=('Arial', 18))   #Cria um texto de Boas vindas                                   
label.pack(padx=20, pady=20)                                                            #Define a posição do texto de Boas vindas

frame = tk.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entries = []
payments = []

entrada1 = tk.CTkEntry(master=frame, placeholder_text="Número de Pagamentos:")    #Cria uma pequena janela para inserir o número de pagamentos
entrada1.pack(pady=12, padx=10)                                                   #Define a posição da caixa de inserção do número de pagamentos

botao1 = tk.CTkButton(master=frame, text="Próximo", command=insertValues)
botao1.pack(pady=12, padx=10)

entrada3 = tk.CTkEntry(master=frame, placeholder_text="Dividend Yeld:")           #Cria uma pequena janela para inserir a taxa pretendida(Dividend Yeld)
entrada3.pack(pady=12, padx=10)   #Define a posição da caixa de inserção da taxa pretendida

botao2 = tk.CTkButton(master=frame, text="Calcular", command=onCalculateClick)
botao2.pack(pady=12, padx=10)

window.mainloop()