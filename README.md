# A8vm

A8 is an 8-bit virtual computer and assembler written in Python.

The project implements a small virtual CPU, memory, instruction set,
assembler, and emulator.

## Features

- 8-bit CPU
- 4 general-purpose registers
- 256 bytes of memory
- Program Counter (PC)
- Stack Pointer (SP)
- FLAGS register
- Custom A8 Assembly language
- Assembler
- CPU emulator
- Conditional and unconditional jumps
- Memory load/store operations
- Program output with `OUT`
- Automated tests with pytest

## Architecture

A8 consists of several main components:

```text
A8 Assembly
     |
     v
  Assembler
     |
     v
 Machine Code
     |
     v
   Memory
     |
     v
    CPU
     |
     v
  Program Output
CPU

The CPU contains four general-purpose registers:

R0
R1
R2
R3

It also contains:

PC
SP
FLAGS

All general-purpose registers store 8-bit values.

Memory

A8 provides 256 bytes of memory.

Valid memory addresses are:

0 - 255

Each memory location stores one byte.

Instruction Set
Instruction	Opcode	Operands	Description
MOV	0x01	register, value	Move a value into a register
ADD	0x02	register, register	Add two registers
SUB	0x03	register, register	Subtract one register from another
LOAD	0x04	register, address	Load a value from memory
STORE	0x05	register, address	Store a register value in memory
JMP	0x06	address	Jump to an address
CMP	0x07	register, register	Compare two registers
JZ	0x08	address	Jump if the comparison flag is set
OUT	0x09	register	Print a register value
HALT	0xFF	none	Stop execution
Example Program
MOV R0, 10
MOV R1, 20
ADD R0, R1
OUT R0
HALT

Running this program produces:

30
Running A8

From the project root:

python -m a8.emulator

The emulator will ask for the path to an A8 program:

programs/hello.a8

project tree:

a8/
├── a8
│   ├── assembler.py
│   ├── cpu.py
│   ├── emulator.py
│   ├── __init__.py
│   ├── instructions.py
│   └── memory.py
├── docs
│   └── architecture.md
├── programs
│   └── hello.a8
├── pyproject.toml
└── README.md

4 directories, 10 files
License

A8 is released under the MIT License.
