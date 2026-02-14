# Specs
Cells are 1-bit units
Characters:
    0, 1,
    XRegMarker, YRegMarker, PCRegMarker, SPRegMarker
4-Bit CPU?
    - up to 16 instructions
Registers
    Program Counter (PC): Address if current instruction here (8 cells)
    Stack Pointer (SP): Current index of the stack (3 cells)
    X & Y: General purpose registers
    Accumulator (ACC): The register to do math
Stack:
    The stack pointer is 3 cells, meaning we can have 8 items on the stack
    Each item in the stack is 4 cells, so the stack is 32 cells
    We can have 4 addresses on the stack b/c each address takes up 2 cells on the stack

Let's try to utilize 100 cells or less (thats how many cell I plan on having on my turing machine)
How many states should/will I use ¯\_(ツ)_/¯

# Instruction set:
LDV - 0000 - A Register, determined from the Register Operand, is loaded with the Value operand
LDA - 0001 - A Register, determined from the Register Operand, is loaded with the value from the address operand
STR - 0010 - Writes the value of a register to the address at the Address operand

ADD - 0011 - The Accumulator register is set to the value of X plus Y; ACC = X; ACC = ACC + Y
SUB - 0100 - The Accumulator register is set to the value of X minus Y; ACC = X; ACC = ACC - Y
AND - 0101 - The Accumulator register is set to the value of X & Y
OR  - 0110 - The accumulator register is set to the value of X | Y
XOR - 0111 - The accumulator register is set to the value of X ^ Y

GOA - 1000 - Sets the PC to the Address operand
GOE - 1001 - Acts as a GOA if the accumulator is 0, else it does nothing like a NOP
GOR - 1010 - Sets the PC to the X and Y registers together. X is the upper 4 cells of the register and Y is the lower 4 cells; (X << 8) | Y
RET - 1011 - Reads 2 from the stack (decrementing the SP) and sets the PC to it. Reads in the format PPC creates, meaning reads the lower 4 cells first, then the upper. On the stack it looks like TTTT BBBB

PPC - 1100 - Pushes the PC to the stack with the top 4 cells being 1st, and the bottom 4 cells being 2nd, so the stack ends up like TTTT BBBB (T & B for "top" and "bottom")
PSH - 1101 - Pushes a copy of the X register into the stack and increments the stack pointer; X Register wrote into the current stack item, INC SP
POP - 1110 - Gets a value from the stack and puts it into the X register; DEC SP, Stack Item written into the X register

HLT - 1111 - Halts the program and exits gracefully

* LDV & LDA only copies from right to left, so you cannot move the X Register into the Y Register but you can copy from the Y Register into the X Register


# Opcode operands
- The Register Operand (R) tells us which register the instruction will read or write to. The register cell value means this:
    0 = Register X
    1 = Register Y
- The Value operand (V) is 4 cells and come after the opcode, and after the register cell if present.
- The Address operand (A) is 8 cells and come after the opcode, and after the register cell if present.

# How to unconditional branch and return?
Unconditional Branch:
    PPC             ; put the PC onto the stack
    GOA 00001111    ; Sets the PC to 00001111
Return:
    RET             ; Read back an address from the stack and set the PC to it


# Memory layout
The PC Register start marker is also the marker of the address space. Addresses are relative to that (and are positive). So an address of 0 would be the PC marker and an address of 28 is the first cell in the stack, an address of 60 (0b00111100) is one cell after the end of the stack, etc

PC              - PC register start marker                                                      --
0 0 0 0 0 0 0 0 - 8 cells for the PC register, we can have up to 255 instructions                |
SP              - SP register start marker                                                       |
0 0 0           - 3 cells for the SP register, this means a max of 8 values in the stack         | 28 cells for the registers
X               - X register start marker                                                        |
0 0 0 0         - 4 cells for the X register                                                     |
Y               - Y register start marker                                                        |
0 0 0 0         - 4 cells for the Y register                                                     |
ACC             - Accumulator register start marker                                              |
0 0 0 0         - 4 cells for the Y register                                                    --

0 0 0 0 0 0 0 0 - 8 cells for 2 stack items  --
0 0 0 0 0 0 0 0 - 8 cells for 2 stack items   | 32 cells in total for the entire stack
0 0 0 0 0 0 0 0 - 8 cells for 2 stack items   | 
0 0 0 0 0 0 0 0 - 8 cells for 2 stack items  --

# Fibonacci Sequence Program
"""
; Fibonacci Sequence
; 14 = 00001110 = X Register
; 19 = 00010011 = Y Register
; 24 = 00011000 = Accumulator Register

; all the registers and the stack goes from 0 to 59, so we start at the program at address 60
LDV 0 0000      ; load X with 0
LDV 1 0001      ; load Y with 1

; the ADD opcode is at address 73 
ADD             ; Accumulator now has X + Y
LDA 0 00010011  ; Load X register w/ the value from the Y register (0010011 = 19, which is the Y Register address)
LDA 1 00011000  ; Load Y register w/ the value from the Accumulator (0011000 = 24, which is the accumulator address)
GOA 01001110    ; Go to address 78, which is the ADD, so we can loop forever
"""

Compiled Fibonacci Sequence from the code above:
0000 0 0000 ; 0000 1 0001 ; 0011 ; 0001 0 00010011 ; 0001 1 00011000 ; 1000 01001110
-> 000000000000010001001100010000100110001100011000100001001110
