from . import memory
from . import cpu
from . import assembler


def run(source):
    machine_code = assembler.assemble_program(source)

    mem = memory.Memory()
    machine = cpu.CPU()
    machine.memory = mem

    for address, value in enumerate(machine_code):
        mem.write(address, value)

    while not machine.halted:
        machine.step()

    return machine


def run_file(path):
    with open(path, "r") as file:
        source = file.read()

    return run(source)


if __name__ == "__main__":
    run_file(input())