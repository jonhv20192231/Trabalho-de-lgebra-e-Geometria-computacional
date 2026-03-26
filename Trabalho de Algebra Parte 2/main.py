from Matrix import Matrix
from Vector import Vector
from Linear_algebra import LinearAlgebra

def main():
    
    la = LinearAlgebra()

    
    print("=" * 40)
    print("      SISTEMA DE ÁLGEBRA LINEAR".center(40))
    print("=" * 40)

    
    dados_sistema = [
        [2, 1, 10],
        [1, 3, 15]
    ]
    
    matriz_original = Matrix(dados_sistema)

    

    print("\n[PASSO 1] MATRIZ ORIGINAL (AUMENTADA):")
    print(matriz_original)
    print("-" * 30)

    
    print("\n[EXTRA] TESTANDO MÉTODO 'TIMES' (Dobrando o sistema):")
    matriz_dobrada = la.times(2, matriz_original)
    print(matriz_dobrada)
    print("-" * 30)

    
    print("\n[EXTRA] TESTANDO MÉTODO 'TRANSPOSE' (Gira a matriz):")
    matriz_transposta = la.transpose(matriz_original)
    print(matriz_transposta)
    print("-" * 30)

    
    print("\n[PASSO 2] MATRIZ ESCALONADA (MÉTODO DE GAUSS):")
    matriz_escalonada = la.gauss(matriz_original)
    print(matriz_escalonada)
    print("-" * 30)

    
    print("\n[PASSO 3] RESULTADO FINAL (VALORES DE X e Y):")
    resultado_final = la.solve(matriz_original)
    print(resultado_final)
    
    print("\n" + "=" * 40)
    print("       EXECUÇÃO FINALIZADA".center(40))
    print("=" * 40)

if __name__ == "__main__":
    main()