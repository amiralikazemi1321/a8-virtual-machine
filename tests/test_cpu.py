from a8.cpu import CPU


def test_mov():
    cpu = CPU()

    cpu.execute_mov(0x00, 42)

    assert cpu.R0 == 42


def test_add():
    cpu = CPU()

    cpu.R0 = 10
    cpu.R1 = 20

    cpu.execute_add(0x00, 0x01)

    assert cpu.R0 == 30


def test_sub():
    cpu = CPU()

    cpu.R0 = 30
    cpu.R1 = 10

    cpu.execute_sub(0x00, 0x01)

    assert cpu.R0 == 20


def test_load_store():
    cpu = CPU()

    cpu.R0 = 42
    cpu.execute_store(0x00, 100)

    cpu.R0 = 0
    cpu.execute_load(0x00, 100)

    assert cpu.R0 == 42


def test_jmp():
    cpu = CPU()

    cpu.execute_jmp(50)

    assert cpu.PC == 50


def test_cmp_equal():
    cpu = CPU()

    cpu.R0 = 10
    cpu.R1 = 10

    cpu.execute_cmp(0x00, 0x01)

    assert cpu.FLAGS == 1


def test_cmp_not_equal():
    cpu = CPU()

    cpu.R0 = 10
    cpu.R1 = 20

    cpu.execute_cmp(0x00, 0x01)

    assert cpu.FLAGS == 0


def test_jz():
    cpu = CPU()

    cpu.FLAGS = 1
    cpu.execute_jz(50)

    assert cpu.PC == 50


def test_out():
    cpu = CPU()

    cpu.R0 = 30

    cpu.execute_out(0x00)


def test_halt():
    cpu = CPU()

    cpu.memory.write(0, 0xFF)

    cpu.step()

    assert cpu.halted is True