import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares.geradorDeMatrizes import exibir_valores_iniciais, gerar_matrizes

def jacobi(A,b,x0,tol,max_iter):
  print("---Resolução pelo método de Jacobi---\n")

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

  x_copia = np.copy(x0)
  maior_erro = float("inf")

  for i in range(max_iter):

    for j in range(A.shape[0]):
      #Aqui é calculado a aproximação das variaveis do sistema
      #Utilizando do seguinte apresentado na imagem 1.1

      soma_dos_termos = sum((A[j][k] * x0[k] for k in range(A[j].size) if k != j))
      x_copia[j] = (b[j] - soma_dos_termos) / A[j,j]
      maior_erro = min(maior_erro, np.abs(x_copia[j] - x0[j]))

    print(f"📍iteração {i + 1},valores das variaveis:\n {x_copia}")
    
    if maior_erro < tol:
      #verifica se o erro maximo das variaveis é menor que o erro
      #esperado i.e se o método convergiu

      print(f"{x_copia}")
      print(f"✅A convergencia foi atingida! maior erro de {maior_erro} em {i + 1} iterações")
      return

    #Importante notar que a atualização dos valores das variaveis é realizada após
    #a aproximação de todas elas
    x0[:] = x_copia

  print(f"❌A convergencia não foi atingida! maior erro de {maior_erro} em {i} iterações")

matriz_a,vetor_de_resultados,vetor_de_palpites = gerar_matrizes(40,60,5)
exibir_valores_iniciais(matriz_a,vetor_de_resultados,vetor_de_palpites)

tol = 1e-6
iteracoes = 1000

print("Resultado via numpy: \n")
print(np.linalg.solve(matriz_a,vetor_de_resultados))
print("--------------------------\n")

resultado = jacobi(matriz_a,vetor_de_resultados,vetor_de_palpites,tol,iteracoes)