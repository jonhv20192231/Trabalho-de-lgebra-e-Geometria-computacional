class Vector:
    def __init__(self, elements):
        
        self.elements = list(elements)
        self.dim = len(self.elements)

    def get(self, i):
       
        if 0 <= i < self.dim:
            return self.elements[i]
        else:
            raise IndexError(f"Índice {i} fora do alcance do vetor de dimensão {self.dim}.")

    def set(self, i, value):
        
        if 0 <= i < self.dim:
            self.elements[i] = value
        else:
            raise IndexError(f"Não é possível definir valor no índice {i}.")

    def __str__(self):
        
        return f"Vetor({self.dim}): {self.elements}"