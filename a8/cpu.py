from . import memory
from . import instructions

class CPU:
    def __init__(self):
        self.R0 = 0
        self.R1 = 0
        self.R2 = 0
        self.R3 = 0
        self.PC = 0
        self.SP = 255
        self.FLAGS = 0
        self.halted = False
        self.memory = memory.Memory()

    def fetch(self):
        opcode = self.memory.read(self.PC)
        self.PC += 1
        return opcode

    def execute_mov(self, register, value):
        if register == 0x00:
            self.R0 = value
        elif register == 0x01:
            self.R1 = value
        elif register == 0x02:
            self.R2 = value
        elif register == 0x03:
            self.R3 = value

    def execute_add(self, register, source):
        if register == 0x00:
            if source == 0x00:
                self.R0 = self.R0 + self.R0
            elif source == 0x01:
                self.R0 = self.R0 + self.R1
            elif source == 0x02:
                self.R0 = self.R0 + self.R2
            elif source == 0x03:
                self.R0 = self.R0 + self.R3

        elif register == 0x01:
            if source == 0x00:
                self.R1 = self.R1 + self.R0
            elif source == 0x01:
                self.R1 = self.R1 + self.R1
            elif source == 0x02:
                self.R1 = self.R1 + self.R2
            elif source == 0x03:
                self.R1 = self.R1 + self.R3

        elif register == 0x02:
            if source == 0x00:
                self.R2 = self.R2 + self.R0
            elif source == 0x01:
                self.R2 = self.R2 + self.R1
            elif source == 0x02:
                self.R2 = self.R2 + self.R2
            elif source == 0x03:
                self.R2 = self.R2 + self.R3

        elif register == 0x03:
            if source == 0x00:
                self.R3 = self.R3 + self.R0
            elif source == 0x01:
                self.R3 = self.R3 + self.R1
            elif source == 0x02:
                self.R3 = self.R3 + self.R2
            elif source == 0x03:
                self.R3 = self.R3 + self.R3

    def execute_sub(self, register, source):
        if register == 0x00:
            if source == 0x00:
                self.R0 = self.R0 - self.R0
            elif source == 0x01:
                self.R0 = self.R0 - self.R1
            elif source == 0x02:
                self.R0 = self.R0 - self.R2
            elif source == 0x03:
                self.R0 = self.R0 - self.R3

        elif register == 0x01:
            if source == 0x00:
                self.R1 = self.R1 - self.R0
            elif source == 0x01:
                self.R1 = self.R1 - self.R1
            elif source == 0x02:
                self.R1 = self.R1 - self.R2
            elif source == 0x03:
                self.R1 = self.R1 - self.R3

        elif register == 0x02:
            if source == 0x00:
                self.R2 = self.R2 - self.R0
            elif source == 0x01:
                self.R2 = self.R2 - self.R1
            elif source == 0x02:
                self.R2 = self.R2 - self.R2
            elif source == 0x03:
                self.R2 = self.R2 - self.R3

        elif register == 0x03:
            if source == 0x00:
                self.R3 = self.R3 - self.R0
            elif source == 0x01:
                self.R3 = self.R3 - self.R1
            elif source == 0x02:
                self.R3 = self.R3 - self.R2
            elif source == 0x03:
                self.R3 = self.R3 - self.R3

    def execute_load(self, register, address):
        value = self.memory.read(address)

        if register == 0x00:
            self.R0 = value
        elif register == 0x01:
            self.R1 = value
        elif register == 0x02:
            self.R2 = value
        elif register == 0x03:
            self.R3 = value

    def execute_store(self, register, address):
        if register == 0x00:
            value = self.R0
        elif register == 0x01:
            value = self.R1
        elif register == 0x02:
            value = self.R2
        elif register == 0x03:
            value = self.R3

        self.memory.write(address, value)

    def execute_jmp(self, address):
        self.PC = address

    def execute_cmp(self, register, source):
        if register == 0x00:
            if source == 0x00:
                if self.R0 == self.R0:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x01:
                if self.R0 == self.R1:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x02:
                if self.R0 == self.R2:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x03:
                if self.R0 == self.R3:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0

        elif register == 0x01:
            if source == 0x00:
                if self.R1 == self.R0:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x01:
                if self.R1 == self.R1:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x02:
                if self.R1 == self.R2:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x03:
                if self.R1 == self.R3:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0

        elif register == 0x02:
            if source == 0x00:
                if self.R2 == self.R0:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x01:
                if self.R2 == self.R1:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x02:
                if self.R2 == self.R2:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x03:
                if self.R2 == self.R3:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0

        elif register == 0x03:
            if source == 0x00:
                if self.R3 == self.R0:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x01:
                if self.R3 == self.R1:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x02:
                if self.R3 == self.R2:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0
            elif source == 0x03:
                if self.R3 == self.R3:
                    self.FLAGS = 1
                else:
                    self.FLAGS = 0

    def execute_jz(self, address):
        if self.FLAGS == 1:
            self.PC = address

    def execute_out(self, register):
        if register == 0x00:
            print(self.R0)
        elif register == 0x01:
            print(self.R1)
        elif register == 0x02:
            print(self.R2)
        elif register == 0x03:
            print(self.R3)
        
    def step(self):
        o = self.fetch()
        r = instructions.decode(o)

        if r == "MOV":
            register = self.fetch()
            value = self.fetch()
            self.execute_mov(register, value)

        elif r == "ADD":
            register = self.fetch()
            source = self.fetch()
            self.execute_add(register, source)

        elif r == "SUB":
            register = self.fetch()
            source = self.fetch()
            self.execute_sub(register, source)

        elif r == "OUT":
            register = self.fetch()
            self.execute_out(register)

        elif r == "HALT":
            self.halted = True

        elif r == "LOAD":
            register = self.fetch()
            address = self.fetch()
            self.execute_load(register, address)

        elif r == "STORE":
            register = self.fetch()
            address = self.fetch()
            self.execute_store(register, address)

        elif r == "JMP":
            address = self.fetch()
            self.execute_jmp(address)

        elif r == "CMP":
            register = self.fetch()
            source = self.fetch()
            self.execute_cmp(register, source)

        elif r == "JZ":
            address = self.fetch()
            self.execute_jz(address)

        
