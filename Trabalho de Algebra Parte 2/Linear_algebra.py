from Matrix import Matrix
from Vector import Vector

class LinearAlgebra:
    
    def transpose(self, a):
       
        if isinstance(a, Vector):
          
            new_matrix = Matrix([[0] for _ in range(a.dim)])
            for i in range(a.dim):
                new_matrix.set(i, 0, a.get(i))
            return new_matrix
        
        if isinstance(a, Matrix):
           
            new_data = [[0 for _ in range(a.rows)] for _ in range(a.cols)]
            new_matrix = Matrix(new_data)
            for i in range(a.rows):
                for j in range(a.cols):
                    new_matrix.set(j, i, a.get(i, j))
            return new_matrix
        
        raise TypeError("O parâmetro deve ser Matrix ou Vector.")
    
    def times(self, a, b):
        
        if isinstance(a, (int, float)):
            if isinstance(b, Vector):
                res = Vector([0] * b.dim)
                for i in range(b.dim):
                    res.set(i, b.get(i) * a)
                return res
            
            if isinstance(b, Matrix):
                new_data = [[0 for _ in range(b.cols)] for _ in range(b.rows)]
                res = Matrix(new_data)
                for i in range(b.rows):
                    for j in range(b.cols):
                        res.set(i, j, b.get(i, j) * a)
                return res


        if isinstance(a, Matrix) and isinstance(b, Matrix):
            if a.cols != b.rows:
                raise ValueError("Dimensões incompatíveis: colunas de A devem ser iguais às linhas de B.")
            
            
            new_data = [[0 for _ in range(b.cols)] for _ in range(a.rows)]
            res = Matrix(new_data)

            for i in range(a.rows):         
                for j in range(b.cols):     
                    soma_produto = 0
                    for k in range(a.cols): 
                        soma_produto += a.get(i, k) * b.get(k, j)
                    res.set(i, j, soma_produto)
            return res

        raise TypeError("Operação 'times' não suportada para estes tipos ou ordem incorreta.")

    def sum(self, a, b):
        
        if type(a) != type(b):
            raise TypeError("Os objetos devem ser do mesmo tipo para soma.")

        if isinstance(a, Vector):
            if a.dim != b.dim:
                raise ValueError("Vetores devem ter o mesmo tamanho.")
            res = Vector([0] * a.dim)
            for i in range(a.dim):
                res.set(i, a.get(i) + b.get(i))
            return res

        if isinstance(a, Matrix):
            if a.rows != b.rows or a.cols != b.cols:
                raise ValueError("Matrizes devem ter as mesmas dimensões.")
            new_data = [[0 for _ in range(a.cols)] for _ in range(a.rows)]
            res = Matrix(new_data)
            for i in range(a.rows):
                for j in range(a.cols):
                    res.set(i, j, a.get(i, j) + b.get(i, j))
            return res

    def gauss(self, a):
       
        if not isinstance(a, Matrix):
            raise TypeError("O parâmetro deve ser uma Matrix.")

        
        m_copy_data = [row[:] for row in a.data]
        m = Matrix(m_copy_data)
        
        for i in range(min(m.rows, m.cols)):
            
            max_row = i
            for k in range(i + 1, m.rows):
                if abs(m.get(k, i)) > abs(m.get(max_row, i)):
                    max_row = k
            
            
            m.data[i], m.data[max_row] = m.data[max_row], m.data[i]

            if abs(m.get(i, i)) < 1e-12:
                continue

            
            for k in range(i + 1, m.rows):
                factor = m.get(k, i) / m.get(i, i)
                for j in range(i, m.cols):
                    novo_valor = m.get(k, j) - (factor * m.get(i, j))
                    m.set(k, j, novo_valor)
        return m

    def solve(self, a):
       
        augmented = self.gauss(a)
        n = augmented.rows
        x = [0 for _ in range(n)]

        
        for i in range(n - 1, -1, -1):
            if abs(augmented.get(i, i)) < 1e-12:
                continue
            
            soma = sum(augmented.get(i, j) * x[j] for j in range(i + 1, n))
            
            x[i] = (augmented.get(i, n) - soma) / augmented.get(i, i)

        return Vector(x) 