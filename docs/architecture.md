# A8 Architecture

## Overview

A8 is an 8-bit virtual computer implemented in Python.

It consists of:

- An 8-bit CPU
- 256 bytes of memory
- Four general-purpose registers
- Special registers
- An instruction set
- An assembler
- An emulator

A8 programs are written in A8 Assembly and assembled into machine code before execution.

## CPU

The CPU has four general-purpose registers:

- R0
- R1
- R2
- R3

Each register stores an 8-bit value.

The CPU also contains:

- PC — Program Counter
- SP — Stack Pointer
- FLAGS — CPU flags

### Program Counter

PC stores the address of the next instruction to fetch.

After fetching an instruction or operand, PC is incremented.

Jump instructions can modify PC directly.

### Stack Pointer

SP represents the current stack position.

The initial value of SP is 255.

### FLAGS

FLAGS stores the result of comparison operations.

Currently:

- `1` means equal
- `0` means not equal

`JZ` uses this flag to decide whether to jump.

## Memory

A8 has 256 bytes of memory.

Valid addresses are:

```text
0 - 255

Each memory location stores one 8-bit value.

Memory is initially filled with zeroes.

Instruction Set
Instruction	Opcode	Operands	Description
MOV	0x01	register, value	Store a value in a register
ADD	0x02	register, register	Add two registers
SUB	0x03	register, register	Subtract one register from another
LOAD	0x04	register, address	Load a value from memory
STORE	0x05	register, address	Store a register value in memory
JMP	0x06	address	Jump to an address
CMP	0x07	register, register	Compare two registers
JZ	0x08	address	Jump if FLAGS is set
OUT	0x09	register	Print a register value
HALT	0xFF	none	Stop execution
Registers

Register identifiers are encoded as:

Register	Value
R0	0x00
R1	0x01
R2	0x02
R3	0x03
Machine Code

For example:

MOV R0, 10
MOV R1, 20
ADD R0, R1
OUT R0
HALT

is assembled into:

01 00 0A
01 01 14
02 00 01
09 00
FF

The CPU fetches these bytes from memory and executes them sequentially.

Execution Cycle

The CPU follows a simple fetch-decode-execute cycle:

Fetch an opcode from memory using PC.
Increment PC.
Decode the opcode.
Fetch required operands.
Execute the instruction.
Repeat until HALT.

Conceptually:

Memory
   |
   v
 Fetch
   |
   v
 Decode
   |
   v
 Execute
   |
   v
 Update CPU state
   |
   +------> Fetch
Assembler

The assembler converts A8 Assembly source code into machine code.

For example:

MOV R0, 10

becomes:

[0x01, 0x00, 0x0A]

The assembler validates:

Instruction names
Operand count
Register names
Numeric operands
Emulator

The emulator:

Reads an A8 program.
Assembles it into machine code.
Loads the machine code into memory.
Creates a CPU.
Executes instructions until HALT.

A program can produce output through the OUT instruction.

Project Structure
a8/
├── README.md
├── pyproject.toml
├── docs/
│   └── architecture.md
├── a8/
│   ├── __init__.py
│   ├── cpu.py
│   ├── memory.py
│   ├── instructions.py
│   ├── assembler.py
│   └── emulator.py
├── programs/
│   └── hello.a8
└── tests/
    ├── test_cpu.py
    ├── test_memory.py
    └── test_instructions.py