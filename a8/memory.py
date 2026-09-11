class Memory:
    def __init__(self):
        self.memory = bytearray(256)

    def read(self, n):
        return self.memory[n]

    def write(self, a, b):
        self.memory[a] = b


