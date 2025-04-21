import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares.geradorDeMatrizes import exibir_valores_iniciais, gerar_matrizes

def gauss_seidel(A, b, x0, tol, max_iter):
    #realiza a soma das linhas para verificar se o pivo é o maior valor presente na mesma
    for i in range(A.shape[0]):
      soma_da_linha = 0
      pivo = 0
      for j in range(A[i].size):
        if i == j:
          pivo = np.abs(A[i,j])
        else:
          soma_da_linha += np.abs(A[i,j])
      if soma_da_linha > pivo:
        print("A matriz não é diagonal dominante❌")
        return
    print("A matriz é diagonal dominante!✔️\n")
    
    x = np.copy(x0)
    
    for iter in range(max_iter):
        x_old = np.copy(x)
        maior_erro = 0
        for i in range(A.shape[0]):
            #Aqui é calculado a aproximação das variaveis do sistema
            #Utilizando do seguinte apresentado na imagem 1.1

            soma = 0
            for j in range(A.shape[0]):
                if j != i:
                    soma += A[i,j] * x[j]
            #A atualização é realizada após a aproximação de qualquer variavel do meu sistema
            x[i] = (b[i] - soma) / A[i,i]
            erro = np.abs(x[i] - x_old[i])
            maior_erro = max(maior_erro, erro)
        
        print(f"📍iteração {iter + 1}, valores das variáveis:\n {x}")
        print(f"Maior erro nesta iteração: {maior_erro}")
        
        if maior_erro < tol:
            print(f"✅A convergência foi atingida! Maior erro de {maior_erro} em {iter + 1} iterações")
            return x
    
    print(f"❌A convergência não foi atingida! Maior erro de {maior_erro} em {max_iter} iterações")
    return x

matriz_a,vetor_de_resultados,vetor_de_palpites = gerar_matrizes(40,60,500)
exibir_valores_iniciais(matriz_a,vetor_de_resultados,vetor_de_palpites)

tol = 1e-6
iteracoes = 1000

print("Resultado via numpy: \n")
print(np.linalg.solve(matriz_a,vetor_de_resultados))
print("--------------------------\n")

resultado = gauss_seidel(matriz_a,vetor_de_resultados,vetor_de_palpites,tol,iteracoes)