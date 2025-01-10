import tkinter as tk
from tkinter import messagebox
import json


# Função para centralizar a janela
def centralizar_janela(janela, largura=400, altura=300):
    janela.geometry(f"{largura}x{altura}+{int(janela.winfo_screenwidth()/2 - largura/2)}+{int(janela.winfo_screenheight()/2 - altura/2)}")


# ===========================
# QUESTÃO 1 - Soma da variável
# ===========================
def questao_1():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    messagebox.showinfo("Questão 1", f"O valor da variável SOMA é: {SOMA}")


# ===========================
# QUESTÃO 2 - Sequência de Fibonacci
# ===========================
def questao_2():
    def is_fibonacci(number):
        a, b = 0, 1
        while b <= number:
            if b == number:
                return True
            a, b = b, a + b
        return False

    def verificar_fibonacci():
        try:
            number = int(entry_fibonacci.get())
            if is_fibonacci(number):
                messagebox.showinfo("Questão 2", f"O número {number} pertence à sequência de Fibonacci.")
            else:
                messagebox.showinfo("Questão 2", f"O número {number} não pertence à sequência de Fibonacci.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    # Janela para entrada
    janela_fibonacci = tk.Toplevel()
    janela_fibonacci.title("Questão 2 - Fibonacci")
    centralizar_janela(janela_fibonacci, 400, 200)
    tk.Label(janela_fibonacci, text="Informe um número:", font=("Arial", 12)).pack(pady=10)
    entry_fibonacci = tk.Entry(janela_fibonacci, font=("Arial", 12), width=20)
    entry_fibonacci.pack(pady=10)
    tk.Button(janela_fibonacci, text="Verificar", command=verificar_fibonacci, bg="#007acc", fg="white", font=("Arial", 12)).pack(pady=10)


# ===========================
# QUESTÃO 3 - Faturamento diário
# ===========================
def questao_3():
    faturamento_json = '''
    [
        {"dia": 1, "valor": 1000},
        {"dia": 2, "valor": 0},
        {"dia": 3, "valor": 1500},
        {"dia": 4, "valor": 2000},
        {"dia": 5, "valor": 0}
    ]
    '''
    faturamento = json.loads(faturamento_json)
    valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    resultado = (
        f"Menor valor de faturamento: {menor_valor}\n"
        f"Maior valor de faturamento: {maior_valor}\n"
        f"Dias acima da média mensal: {dias_acima_media}"
    )

    messagebox.showinfo("Questão 3", resultado)


# ===========================
# QUESTÃO 4 - Percentual de representação
# ===========================
def questao_4():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    faturamento_total = sum(faturamento_estados.values())
    resultado = "Percentual de representação:\n"

    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        resultado += f"{estado}: {percentual:.2f}%\n"

    messagebox.showinfo("Questão 4", resultado)


# ===========================
# QUESTÃO 5 - Inversão de string
# ===========================
def questao_5():
    def inverte_string(string):
        invertida = ""
        for i in range(len(string) - 1, -1, -1):
            invertida += string[i]
        return invertida

    def inverter():
        string = entry_string.get()
        invertida = inverte_string(string)
        messagebox.showinfo("Questão 5", f"String invertida: {invertida}")

    # Janela para entrada
    janela_inversao = tk.Toplevel()
    janela_inversao.title("Questão 5 - Inversão de String")
    centralizar_janela(janela_inversao, 400, 200)
    tk.Label(janela_inversao, text="Informe uma string:", font=("Arial", 12)).pack(pady=10)
    entry_string = tk.Entry(janela_inversao, font=("Arial", 12), width=20)
    entry_string.pack(pady=10)
    tk.Button(janela_inversao, text="Inverter", command=inverter, bg="#007acc", fg="white", font=("Arial", 12)).pack(pady=10)


# ===========================
# INTERFACE PRINCIPAL
# ===========================
def main():
    janela = tk.Tk()
    janela.title("Desafio Técnico - Menu")
    centralizar_janela(janela, 500, 400)

    janela.configure(bg="#f4f4f4")

    tk.Label(
        janela, text="Selecione uma questão para executar:", font=("Arial", 16), bg="#f4f4f4"
    ).pack(pady=20)

    tk.Button(
        janela, text="Questão 1 - Soma da variável", command=questao_1, font=("Arial", 14), width=30, bg="#007acc", fg="white"
    ).pack(pady=10)
    tk.Button(
        janela, text="Questão 2 - Fibonacci", command=questao_2, font=("Arial", 14), width=30, bg="#007acc", fg="white"
    ).pack(pady=10)
    tk.Button(
        janela, text="Questão 3 - Faturamento diário", command=questao_3, font=("Arial", 14), width=30, bg="#007acc", fg="white"
    ).pack(pady=10)
    tk.Button(
        janela, text="Questão 4 - Percentual de representação", command=questao_4, font=("Arial", 14), width=30, bg="#007acc", fg="white"
    ).pack(pady=10)
    tk.Button(
        janela, text="Questão 5 - Inversão de string", command=questao_5, font=("Arial", 14), width=30, bg="#007acc", fg="white"
    ).pack(pady=10)
    tk.Button(
        janela, text="Sair", command=janela.destroy, font=("Arial", 14), width=30, bg="#e74c3c", fg="white"
    ).pack(pady=20)

    janela.mainloop()


if __name__ == "__main__":
    main()
