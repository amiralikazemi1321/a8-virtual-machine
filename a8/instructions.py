INSTRUCTIONS = {
    "MOV": 0x01,
    "ADD": 0x02,
    "SUB": 0x03,
    "LOAD": 0x04,
    "STORE": 0x05,
    "JMP": 0x06,
    "CMP": 0x07,
    "JZ": 0x08,
    "OUT": 0x09,
    "HALT": 0xFF
}

OPCODES = {
    0x01: "MOV",
    0x02: "ADD",
    0x03: "SUB",
    0x04: "LOAD",
    0x05: "STORE",
    0x06: "JMP",
    0x07: "CMP",
    0x08: "JZ",
    0x09: "OUT",
    0xFF: "HALT"
}

REGISTERS = {
    "R0": 0x00,
    "R1": 0x01,
    "R2": 0x02,
    "R3": 0x03
}

REGISTER_NAMES = {
    0x00: "R0",
    0x01: "R1",
    0x02: "R2",
    0x03: "R3"
}

def decode(n):
    return OPCODES[n]