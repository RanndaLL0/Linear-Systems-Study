import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares.geradorDeMatrizes import exibir_valores_iniciais, gerar_matrizes

def eliminacao_gaussiana(a, b):

    #Converte as matrizes para ponto flutuante
    a = a.astype(float)
    b = b.astype(float)

    #n representa o numero de linhas da minha matriz
    n = a.shape[0]

    for i in range(n - 1):
      pivo = a[i][i]
      if pivo == 0:
        print("Não é possivel realizar o pivoteamento!")
        return
      for j in range(i + 1, n):
        #realiza as operações entre as linhas a fim de igualar a zero os valores abaixo do pivo

        m = a[j][i] / pivo
        a[j] = a[j] - m * a[i]
        b[j] = b[j] - m * b[i]

    #percorre as linhas de cima para baixo descobrindo o valor de cada variavel do sistemas
    x = np.zeros(n)
    for i in range(n - 1, - 1, -1):
        x[i] = (b[i] - np.dot(a[i, i+1:], x[i+1:])) / a[i, i]
    return a,x

A,B,_ = gerar_matrizes(5,10,5)

print(f"Sistema inicial\n\{A}")
print("--------------------------")
print(f"Vetor de resultados\n{B}")
print("--------------------------\n\n")

print("Resolução via numpy: \n")
print("--------------------------")
print(np.linalg.solve(A,B))
print("--------------------------\n\n")

a,b = eliminacao_gaussiana(A,B)

print(f"Sistema final\n{a}")
print("--------------------------")
print(f"Vetor de resultados\n{b}")
print("--------------------------")