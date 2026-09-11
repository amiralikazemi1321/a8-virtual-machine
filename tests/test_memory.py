from a8.memory import Memory


def test_memory_read_write():
    memory = Memory()

    memory.write(10, 42)

    assert memory.read(10) == 42


def test_memory_initial_value():
    memory = Memory()

    assert memory.read(0) == 0
    assert memory.read(255) == 0