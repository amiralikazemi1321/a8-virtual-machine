from a8 import instructions


def test_instruction_opcodes():
    assert instructions.INSTRUCTIONS["MOV"] == 0x01
    assert instructions.INSTRUCTIONS["ADD"] == 0x02
    assert instructions.INSTRUCTIONS["SUB"] == 0x03
    assert instructions.INSTRUCTIONS["LOAD"] == 0x04
    assert instructions.INSTRUCTIONS["STORE"] == 0x05
    assert instructions.INSTRUCTIONS["JMP"] == 0x06
    assert instructions.INSTRUCTIONS["CMP"] == 0x07
    assert instructions.INSTRUCTIONS["JZ"] == 0x08
    assert instructions.INSTRUCTIONS["OUT"] == 0x09
    assert instructions.INSTRUCTIONS["HALT"] == 0xFF


def test_decode():
    assert instructions.decode(0x01) == "MOV"
    assert instructions.decode(0x09) == "OUT"
    assert instructions.decode(0xFF) == "HALT"