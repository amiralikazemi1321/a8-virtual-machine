from . import instructions

SYNTAX = {
    "MOV": ["register", "value"],
    "ADD": ["register", "register"],
    "SUB": ["register", "register"],
    "LOAD": ["register", "address"],
    "STORE": ["register", "address"],
    "JMP": ["address"],
    "CMP": ["register", "register"],
    "JZ": ["address"],
    "OUT": ["register"],
    "HALT": []
}

line = "MOV R0, 10"
source = """
MOV R0, 10
MOV R1, 20
ADD R0, R1
HALT
"""


def tokenize(line):
    line = line.strip()

    l = []
    word = ""

    for i in line:
        if i == ' ':
            l.append(word)
            word = ""
        else:
            word += i

    l.append(word)

    for index, j in enumerate(l):
        if ',' in j:
            l[index] = j.replace(',', '')

    return l

def validate(tokens):
    instruction = tokens[0]

    if instruction not in SYNTAX:
        raise ValueError(f"Unknown instruction: {instruction}")

    expected = SYNTAX[instruction]
    operands = tokens[1:]

    if len(operands) != len(expected):
        raise ValueError(
            f"{instruction} expects {len(expected)} operand(s), "
            f"got {len(operands)}"
        )

    for operand, operand_type in zip(operands, expected):

        if operand_type == "register":
            if operand not in instructions.REGISTERS:
                raise ValueError(f"Unknown register: {operand}")

        elif operand_type in ("value", "address"):
            try:
                int(operand)
            except ValueError:
                raise ValueError(
                    f"Expected {operand_type}, got: {operand}"
                )

def assemble(tokens):
    instruction = tokens[0]
    operands = tokens[1:]

    opcode = instructions.INSTRUCTIONS[instruction]
    machine_code = [opcode]

    for operand, operand_type in zip(operands, SYNTAX[instruction]):
        if operand_type == "register":
            machine_code.append(instructions.REGISTERS[operand])
        else:
            machine_code.append(int(operand))

    return machine_code

def assemble_program(source):
    machine_code = []

    for line in source.splitlines():
        line = line.strip()

        if not line:
            continue

        tokens = tokenize(line)
        validate(tokens)

        code = assemble(tokens)
        machine_code.extend(code)

    return machine_code

machine_code = assemble_program(source)
