'''
Created on 20 de dez. de 2025

@author: Marcus Vinicius Belo Matos de Aguiar
'''

import numpy

# Função para adicionar duas matrizes
def SomaMatrizes(A,B, m, n):
    C = numpy.zeros((m,n))                        # Criação da matriz C para receber o resultado, de mesmas dimensões que A e B. Ela é inicialmente preenchida com zeros apenas
    for i in range (m):                         # Loop interno para as linhas
        for j in range(n):                      # Loop externo para as colunas
            C[i][j] = A[i][j] + B[i][j]         # Soma elemento a elemento
    
    return C

print("Programa para Adicionar duas Matrizes de Dimensões iguais!")

try:
    m1 = int(input("Digite o número de linhas da primeira matriz A:"))
    n1 = int(input("Digite o número de colunas da primeira matriz A:"))
    print("\nDigite os elementos da matriz A:")
    A = numpy.zeros((m1, n1))
    for i in range(m1):
        for j in range(n1):
            A[i][j] = float(input(f"A[{i}][{j}] = "))
        
    m2 = int(input("Digite o número de linhas da segunda matriz B:"))
    n2 = int(input("Digite o número de colunas da segunda matriz B:"))
    print("\nDigite os elementos da matriz B:")
    B = numpy.zeros((m2, n2))
    for i in range(m2):
        for j in range(n2):
            B[i][j] = float(input(f"B[{i}][{j}] = "))
        
    if (m1 != m2) or (n1 != n2):
        raise ValueError(f"Dimensões incompatíveis: {m1}x{n1} vs {m2}x{n2}")
      
    C = SomaMatrizes(A,B,m1,n1)
    print("A soma das matrizes é C:")
    print(C)
    
except ValueError as erro:
    print(f"Erro Encontrado!\n{erro}")