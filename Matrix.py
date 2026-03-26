class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def get(self, row, col):
       
        return self.data[row][col]

    def set(self, row, col, value):
        
        self.data[row][col] = value

    def __str__(self):
       
        return "\n".join([str(row) for row in self.data])