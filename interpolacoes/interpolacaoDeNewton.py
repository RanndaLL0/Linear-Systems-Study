import numpy as np
import math
import os
import sys
from time import perf_counter
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#função sugerida no enunciado
def f_x(x):
  return (x , np.sin(2*math.pi*x) + 0.2 * np.cos(4*math.pi*x) + 0.1 * x);

#pontos (x,y) dado um conjunto de entrada
def gera_saidas(conjunto):
  x = np.array([])
  for i in range(len(conjunto)):
    x_valor, _ = f_x(conjunto[i])
    x = np.append(x,x_valor)

  y = np.array([])
  for i in range(len(conjunto)):
    _, y_valor = f_x(conjunto[i])
    y = np.append(y,y_valor)

  return x,y

def diferencas_divididas(x, y):
    n = len(x)
    #Os coeficientes são atualizados ao final de cada interação sobe a tabela
    #assim gerando no final uma nova matriz contendo os resultados
    coeficientes = [y.copy()]

    for j in range(1, n):
        nova_coluna = []
        #Este loop percorre as colunas não visitadas da matriz
        for i in range(n - j):
            #Calculamos separadamente as diferenças entre x e y 

            numerador = coeficientes[j - 1][i + 1] - coeficientes[j - 1][i]
            denominador = x[i + j] - x[i]
            nova_coluna.append(numerador / denominador)
        coeficientes.append(nova_coluna)

    return [coeficientes[i][0] for i in range(n)]

def interpolacao_de_newton(x,y,x_desejado):
  a = diferencas_divididas(x,y)
  y_0 = y[0]
  resultado = 0
  for i in range(len(a)):
    fator = a[i]
    produto_dos_termos = 1
    for j in range(i):
      produto_dos_termos *= (x_desejado - x[j])
    resultado += fator * produto_dos_termos
  return resultado

def exibe_resultados(x,y,x_interp):

  t1_inicio = perf_counter()
  resultado = interpolacao_de_newton(x,y,x_interp)
  t1_final = perf_counter()

  tempo_execucao = 0
  _,valor_exato = f_x(x_interp)
  erro_absoluto = math.fabs(valor_exato - resultado )

  print("\nValores selecionados de X")
  print(f"{x}")
  print("-------------------------")
  print("Valores selecionados de Y\n")
  print(f"{y}")
  print("-------------------------")
  print("Valor esperado\n")
  print(f"{valor_exato}")
  print("-------------------------")
  print("Resultado Final\n")
  print(resultado)
  print("\n")
  print("-------------------------")
  print("Erro Absoluto\n")
  print(erro_absoluto)
  print("\nErro Relativo\n")
  print((erro_absoluto / valor_exato)*100)
  print("-------------------------")
  print("\n tempo de execução:")
  print(t1_final - t1_inicio)

#A função linspace gera um conjunto de dados dentro de um intervalo especificado
conjunto_um = np.linspace(0,1,10)
conjunto_dois = np.linspace(0,1,20)
conjunto_tres = np.random.rand(15)
x_interp  = 0.25

_,y_resultado = f_x(x_interp)

print("-------------")
print(f"O valor esperado para a função é: {y_resultado}")
print("-------------\n\n")

x_1,y_1 = gera_saidas(conjunto_um)
print("----Primeiro conjunto de dados----\n\n")
exibe_resultados(x_1,y_1,x_interp)

x_2,y_2 = gera_saidas(conjunto_dois)
print("----Segundo conjunto de dados----\n\n")
exibe_resultados(x_2,y_2,x_interp)

x_3,y_3 = gera_saidas(conjunto_tres)
print("----Terceiro conjunto de dados----\n\n")
exibe_resultados(x_3,y_3,x_interp)