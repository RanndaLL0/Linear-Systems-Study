import numpy as np

#Este arquivo contem algumas funções importantes e fundamentais
#para o funcionamento dos métodos implementados 

#Esta função gera matrizes aleatórias seguindo uma escala fornecida
#tanto dos valores presentes em A, quando nos valores presentes em B.
#A mesma também recebe as dimensões que a matriz deve possuir
def gerar_matrizes(intervalo,intervalo_dos_resultados,n):
  A = np.random.randint(intervalo, size=(n,n))

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      valor_multiplicado = np.pow(np.random.randint(1,intervalo),2)
      A[i,j] = valor_multiplicado


  #Este loop impede de que as matrizes geradas não sejam diagonalmente dominantes
  for i in range(A.shape[0]):
    soma_dos_elementos = np.sum(A[i])
    soma_dos_elementos -= A[i,i]
    A[i,i] = soma_dos_elementos + 1

  B = np.random.randint(intervalo_dos_resultados, size=(n))

  for i in range(B.size):
    B[i] += 1
    valor_multiplicado = np.pow(np.random.randint(1,intervalo_dos_resultados),2)
    B[i] = valor_multiplicado

  x0 = np.zeros(n,dtype = float)
  return A,B,x0

#esta função auxilia na exibição dos valores gerados inicialmente
def exibir_valores_iniciais(matriz_a, vetor_de_resultados, vetor_de_palpites):
  print(f"\nSistema inicial🔣\n{matriz_a}\n")
  print("--------------------------")
  print(f"Vetor de resultados🔣\n{vetor_de_resultados}")
  print("--------------------------")
  print(f"Vetor de palpites🔣\n{vetor_de_palpites}")
  print("--------------------------\n")