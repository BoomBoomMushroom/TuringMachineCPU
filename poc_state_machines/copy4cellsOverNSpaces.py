from CustomClasses import State, statesArrayToJson
BLANK_CHARACTER = "_"
states = [
    State("LDVY_TurnIntoPrimes_4", "1", "1'", "R", "LDVY_TurnIntoPrimes_3"),
    State("LDVY_TurnIntoPrimes_4", "0", "0'", "R", "LDVY_TurnIntoPrimes_3"),
    State("LDVY_TurnIntoPrimes_3", "1", "1'", "R", "LDVY_TurnIntoPrimes_2"),
    State("LDVY_TurnIntoPrimes_3", "0", "0'", "R", "LDVY_TurnIntoPrimes_2"),
    State("LDVY_TurnIntoPrimes_2", "1", "1'", "R", "LDVY_TurnIntoPrimes_1"),
    State("LDVY_TurnIntoPrimes_2", "0", "0'", "R", "LDVY_TurnIntoPrimes_1"),
    State("LDVY_TurnIntoPrimes_1", "1", "1'", "R", "LDVY_Back4"),
    State("LDVY_TurnIntoPrimes_1", "0", "0'", "R", "LDVY_Back4"),
    State("LDVY_Back4", None, None, "L", "LDVY_Back3"),
    State("LDVY_Back3", None, None, "L", "LDVY_Back2"),
    State("LDVY_Back2", None, None, "L", "LDVY_Back1"),
    State("LDVY_Back1", None, None, "L", "LDVY_CopyToYReg"),
    State("LDVY_CopyToYReg", "1'", "1", "L", "LDVY_CopyToYReg1"),
    State("LDVY_CopyToYReg", "0'", "0", "L", "LDVY_CopyToYReg0"),
    State("LDVY_CopyToYReg", None, None, "R", "LDVY_CopyToYReg"),
    
    State("LDVY_CopyToYReg1", "Y", None, "R", "LDVY_WriteToYReg1"),
    State("LDVY_CopyToYReg1", "1'", None, "R", "LDVY_WriteToYReg1"),
    State("LDVY_CopyToYReg1", "0'", None, "R", "LDVY_WriteToYReg1"),
    State("LDVY_CopyToYReg1", None, None, "L", "LDVY_CopyToYReg1"),
    
    State("LDVY_CopyToYReg0", "Y", None, "R", "LDVY_WriteToYReg0"),
    State("LDVY_CopyToYReg0", "1'", None, "R", "LDVY_WriteToYReg0"),
    State("LDVY_CopyToYReg0", "0'", None, "R", "LDVY_WriteToYReg0"),
    State("LDVY_CopyToYReg0", None, None, "L", "LDVY_CopyToYReg0"),
    
    # If Y is all primes then we have fully written to the Y Register, if one of them aren't then we still have work to do
    State("LDVY_WriteToYReg1", None, "1'", "R", "LDVY_CheckIfYIsAllPrimesStart"),
    State("LDVY_WriteToYReg0", None, "0'", "R", "LDVY_CheckIfYIsAllPrimesStart"),
    
    State("LDVY_CheckIfYIsAllPrimesStart", None, None, "L", "LDVY_CheckIfYIsAllPrimesStart"),
    State("LDVY_CheckIfYIsAllPrimesStart", "Y", None, "R", "LDVY_CheckIfYIsAllPrimes_4"),
    
    State("LDVY_CheckIfYIsAllPrimes_4", "1'", None, "R", "LDVY_CheckIfYIsAllPrimes_3"),
    State("LDVY_CheckIfYIsAllPrimes_4", "0'", None, "R", "LDVY_CheckIfYIsAllPrimes_3"),
    State("LDVY_CheckIfYIsAllPrimes_4", None, None, "R", "LDVY_CopyToYReg"),
    
    State("LDVY_CheckIfYIsAllPrimes_3", "1'", None, "R", "LDVY_CheckIfYIsAllPrimes_2"),
    State("LDVY_CheckIfYIsAllPrimes_3", "0'", None, "R", "LDVY_CheckIfYIsAllPrimes_2"),
    State("LDVY_CheckIfYIsAllPrimes_3", None, None, "R", "LDVY_CopyToYReg"),
    
    State("LDVY_CheckIfYIsAllPrimes_2", "1'", None, "R", "LDVY_CheckIfYIsAllPrimes_1"),
    State("LDVY_CheckIfYIsAllPrimes_2", "0'", None, "R", "LDVY_CheckIfYIsAllPrimes_1"),
    State("LDVY_CheckIfYIsAllPrimes_2", None, None, "R", "LDVY_CopyToYReg"),
    
    # All of them are primes! Let's now make them normal
    State("LDVY_CheckIfYIsAllPrimes_1", "1'", None, "R", "LDVY_FixYRegPrimes"),
    State("LDVY_CheckIfYIsAllPrimes_1", "0'", None, "R", "LDVY_FixYRegPrimes"),
    State("LDVY_CheckIfYIsAllPrimes_1", None, None, "R", "LDVY_CopyToYReg"),
    
    State("LDVY_FixYRegPrimes", "1'", "1", "L", "LDVY_FixYRegPrimes"),
    State("LDVY_FixYRegPrimes", "0'", "0", "L", "LDVY_FixYRegPrimes"),
    State("LDVY_FixYRegPrimes", None, None, "L", "LDVY_FixYRegPrimes"),
    State("LDVY_FixYRegPrimes", "Y", None, "R", "PCNextInstruction"),
]


"""
def readInstructionGenerator(id=""):
    if len(id.split("_")[1]) >= 4: return []
    
    readZero = State(id, "0", "0", "R", id+"0")
    readOne = State(id, "1", "1", "R", id+"1")
    
    states = [
        str(readZero),
        str(readOne)
    ]
    states.extend(readInstructionGenerator(readZero.nextStateId))
    states.extend(readInstructionGenerator(readOne.nextStateId))
    return states
for item in readInstructionGenerator("CopyValue_"): print(item+",")

for i in range(0, 2**4):
    binary = bin(i).split("0b")[1].zfill(4)
    print(State(f"PCReadNextInstruction_{binary}", None, None, "L", ""))
"""

print(statesArrayToJson(states))
