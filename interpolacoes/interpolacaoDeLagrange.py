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

def lagrange(x,y,x_interp):
  n = len(x)
  resultado = 0
  for i in range(n):

    #definimos numerador e denominador inicialmente como um para evitar
    #problemas de atualização dos valores, já que um é o elemento neutro da multiplicação
    lx_numerador = 1
    lx_denominador = 1
    for j in range(n):
      if i != j:
        #Calculamos as diferenças das variaveis seguindo o raciocinio
        #descrito em imagem_1.2
        lx_numerador *= (x_interp - x[j])
        lx_denominador *= (x[i] - x[j])
    
    #Realiza o produtório
    resultado += y[i] * (lx_numerador/lx_denominador)
  return resultado

#Função auxiliar que exibe os dados das iterações
def exibe_resultados(x,y,x_interp):

  start = perf_counter()
  resultado = lagrange(x,y,x_interp)
  end = perf_counter()

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
  print("\nTempo de execução:")
  print(end-start)


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