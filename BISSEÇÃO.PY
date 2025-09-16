import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    """
    Define a função f(x) a ser analisada.
    Altere a expressão 'return' para usar uma função diferente.
    Exemplo: x**3 - x - 2
    """
    return x**3 - x - 2

def metodo_bissecao(f, a, b, tol):
    """
    Implementação do Método da Bisseção para encontrar a raiz de uma função.

    Argumentos:
    f (function): A função para a qual a raiz está sendo procurada.
    a (float): O início do intervalo.
    b (float): O fim do intervalo.
    tol (float): A tolerância para o critério de parada.

    Retorna:
    (float, list): A raiz aproximada e uma lista de dicionários com os dados de cada iteração.
    """
    # [cite_start]Passo 2: Verificar se f(a) e f(b) têm sinais opostos. [cite: 8]
    if f(a) * f(b) >= 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos.")
        return None, []

    iteracoes_dados = []
    x_anterior = a # Inicializa x_anterior para o cálculo da primeira tolerância
    n = 0

    while True:
        n += 1
        # [cite_start]Passo 3: Obtenha o ponto médio do intervalo. [cite: 9]
        x_n = (a + b) / 2

        # Armazena os dados da iteração atual para a tabela.
        iteracoes_dados.append({
            'n': n,
            'a_n': a,
            'b_n': b,
            'x_n': x_n,
            'f(x_n)': f(x_n)
        })

        # [cite_start]Passo 4: Verifica se o ponto médio é a raiz exata. [cite: 11]
        if f(x_n) == 0:
            print(f"A raiz exata foi encontrada: {x_n}")
            break

        # [cite_start]Passo 7: Verifica o critério de parada pela tolerância. [cite: 16, 17]
        # Este critério é verificado aqui, após o cálculo de x_n, como é comum em implementações.
        if abs(x_n - x_anterior) < tol:
            break

        # Passo 5: Atualiza o intervalo para a próxima iteração.
        if f(a) * f(x_n) < 0: # A raiz está no intervalo [a, x_n]
            b = x_n
        else: # A raiz está no intervalo [x_n, b]
            a = x_n

        x_anterior = x_n

    # [cite_start]A última x_n calculada é a nossa raiz aproximada.
    raiz_aproximada = iteracoes_dados[-1]['x_n']
    return raiz_aproximada, iteracoes_dados

# --- Início da Execução do Programa ---
if __name__ == "__main__":
    # [cite_start]Passo 1: Entrar com a função, o intervalo [a, b] e a tolerância. [cite: 7]
    a = 1.0
    b = 2.0
    tolerancia = 1e-6 # Exemplo: 10^-6

    # Chama o método da bisseção
    raiz, dados = metodo_bissecao(f, a, b, tolerancia)

    if raiz is not None:
        # [cite_start]Obs a) Agrupar os dados em uma tabela. [cite: 22]
        tabela = pd.DataFrame(dados)
        pd.set_option('display.float_format', '{:.8f}'.format) # Formata a exibição dos floats
        print("--- Tabela de Iterações ---")
        print(tabela)

        print(f"\nConclusão:")
        print(f"A raiz aproximada é x = {raiz:.8f} com uma tolerância de {tolerancia}")

        # [cite_start]Obs b) Plotar o gráfico da função. [cite: 30]
        x = np.linspace(a - 0.5, b + 0.5, 400)
        y = f(x)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f'f(x) = x³ - x - 2', color='blue')

        # Exibe a raiz aproximada
        plt.plot(raiz, f(raiz), 'ro', label=f'Raiz Aproximada ({raiz:.4f}, {f(raiz):.4f})')

        # Exibe as iterações
        pontos_x_iter = [d['x_n'] for d in dados]
        pontos_y_iter = [f(d['x_n']) for d in dados]
        plt.plot(pontos_x_iter, pontos_y_iter, 'g.', markersize=5, label='Iterações (x_n)')

        # Configurações do gráfico
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.title('Método da Bisseção')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.show()