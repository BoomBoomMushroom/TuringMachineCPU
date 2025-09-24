# Here is going to create all the states needed to make the CPU function
#   the compiler will just turn the assembly into machine code, then it will put it into the initMemory and combine it w/ the CPU functionality

from CustomClasses import State, statesArrayToJson

BLANK_CHARACTER = "_"

IncPCByN = 13
stateNamePrefix = f"IncPCBy_{IncPCByN}"

states = [
    State(f"{stateNamePrefix}", "PC", None, "R", f"{stateNamePrefix}_GotoPCEndR7"),
    State(f"{stateNamePrefix}", None, None, "L", f"{stateNamePrefix}"),
    State(f"{stateNamePrefix}_GotoPCEndR7", None, None, "R", f"{stateNamePrefix}_GotoPCEndR6"),
    State(f"{stateNamePrefix}_GotoPCEndR6", None, None, "R", f"{stateNamePrefix}_GotoPCEndR5"),
    State(f"{stateNamePrefix}_GotoPCEndR5", None, None, "R", f"{stateNamePrefix}_GotoPCEndR4"),
    State(f"{stateNamePrefix}_GotoPCEndR4", None, None, "R", f"{stateNamePrefix}_GotoPCEndR3"),
    State(f"{stateNamePrefix}_GotoPCEndR3", None, None, "R", f"{stateNamePrefix}_GotoPCEndR2"),
    State(f"{stateNamePrefix}_GotoPCEndR2", None, None, "R", f"{stateNamePrefix}_GotoPCEndR1"),
    State(f"{stateNamePrefix}_GotoPCEndR1", None, None, "R", f"{stateNamePrefix}_AddBit0Carry0"),
]

def generateAddStates(N):
    bits=8
    createdAddStates = []

    # Convert N to binary string, LSB first
    Nbits = list(bin(N)[2:].zfill(bits))[::-1]

    for bit in range(bits):
        for carry in (0, 1):
            stateName = f"{stateNamePrefix}_AddBit{bit}Carry{carry}"
            Nbit = int(Nbits[bit])

            for tapeBit in (0, 1):
                total = tapeBit + Nbit + carry
                writeBit = total % 2
                nextCarry = total // 2
                # Determine next state
                if bit == bits - 1:
                    # Final bit: if carry remains, create new state for extension
                    nextState = f"{stateNamePrefix}_AddBit{bits}Carry{nextCarry}" if nextCarry else "PCNextInstruction"
                else:
                    nextState = f"{stateNamePrefix}_AddBit{bit + 1}Carry{nextCarry}"

                # Append state as a Turing Machine transition
                createdAddStates.append(State(stateName, tapeBit, writeBit, "L", nextState))

    return createdAddStates

states.extend(generateAddStates(IncPCByN))

#print(statesArrayToJson(states, isJson=True))
print(statesArrayToJson(states, isJson=False))
