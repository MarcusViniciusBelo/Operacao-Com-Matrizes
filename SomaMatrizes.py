'''
Created on 20 de dez. de 2025

@author: Marcus Vinicius Belo Matos de Aguiar
'''

import numpy

# Função para adicionar duas matrizes
def SomaMatrizes(A,B, m, n):
    C = numpy.zeros((m,n))                      # Criação da matriz C para receber o resultado, de mesmas dimensões que A e B. Ela é inicialmente preenchida com zeros apenas
    for i in range (m):                         # Loop interno para as linhas
        for j in range(n):                      # Loop externo para as colunas
            C[i][j] = A[i][j] + B[i][j]         # Soma elemento a elemento
    
    return C                                    # Retorna a matriz resultante da soma de A e B      

# Inicio do programa para teste
print("Programa para Adicionar duas Matrizes de Dimensões iguais!")

try:                                            # Try sendo usado para controlar se A e B possuem a mesma dimensão
    m1 = int(input("Digite o número de linhas da primeira matriz A:"))              # Recebe a primeira dimensão (linhas) da matriz A
    n1 = int(input("Digite o número de colunas da primeira matriz A:"))             # Recebe a segunda dimensão (colunas) da matriz A
    print("\nDigite os elementos da matriz A:")                                     
    A = numpy.zeros((m1, n1))                                                       # Inicializa a matriz A com zeros (0)
    for i in range(m1):                                                             # Loop externo (para as linhas)
        for j in range(n1):                                                         # Loop interno (para as colunas)
            A[i][j] = float(input(f"A[{i}][{j}] = "))                               # Recebe os elementos da matriz A, um a um
        
    m2 = int(input("Digite o número de linhas da segunda matriz B:"))               # Recebe a primeira dimensão (linhas) da matriz B
    n2 = int(input("Digite o número de colunas da segunda matriz B:"))              # Recebe a segunda dimensão (colunas) da matriz B
    print("\nDigite os elementos da matriz B:")
    B = numpy.zeros((m2, n2))                                                       # Inicializa a matriz B com zeros (0)
    for i in range(m2):                                                             # Loop externo (para as linhas)
        for j in range(n2):                                                         # Loop interno (para as colunas)
            B[i][j] = float(input(f"B[{i}][{j}] = "))                               # Recebe os elementos da matriz B, um a um
        
    if (m1 != m2) or (n1 != n2):                                                    # Testa se as dimensões de A e B são diferentes
        raise ValueError(f"Dimensões incompatíveis: {m1}x{n1} vs {m2}x{n2}")        # Caso sejam diferentes, instaura o erro 
      
    C = SomaMatrizes(A,B,m1,n1)                                                     # Chama a função para somar as duas matrizes, caso possuam mesma dimensão
    print("A soma das matrizes é C:")                                               # Mostra o resultado
    print(C)
    
except ValueError as erro:                                                          # Retorna o erro caso as dimensões sejam diferentes
    print(f"Erro Encontrado!\n{erro}")