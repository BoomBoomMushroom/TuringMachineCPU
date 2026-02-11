from CustomClasses import State, statesArrayToJson
BLANK_CHARACTER = "_"
states = [
    # Add X and Y reg together and store the result in the accumulator
    
    State("ADD_FindPC", None, None, "L", "ADD_FindPC"),
    State("ADD_FindPC", "PC", "PC", "R", "ADD_GotoXReg"),

    State("ADD_GotoXReg", None, None, "R", "ADD_GotoXReg"),
    State("ADD_GotoXReg", "X", "X", "R", "ADD_XRegVal"),

    State("ADD_XRegVal", "0", "0", "R", "ADD_XRegVal0"),
    State("ADD_XRegVal", "1", "1", "R", "ADD_XRegVal1"),

    State("ADD_XRegVal0", "0", "0", "R", "ADD_XRegVal00"),
    State("ADD_XRegVal0", "1", "1", "R", "ADD_XRegVal01"),
    State("ADD_XRegVal1", "0", "0", "R", "ADD_XRegVal10"),
    State("ADD_XRegVal1", "1", "1", "R", "ADD_XRegVal11"),

    State("ADD_XRegVal00", None, None, "R", ""),
    State("ADD_XRegVal10", None, None, "R", ""),
    State("ADD_XRegVal01", None, None, "R", ""),
    State("ADD_XRegVal11", None, None, "R", ""),
]


with open("./poc_state_machines/instruction_states/add.turing", "w") as f:
    lines = ["[\n"]
    lines.extend(["\t"+s.__str__(isJson=True)+",\n" for s in states])
    lines[-1] = lines[-1][:-2] + "\n"
    lines.append("]")

    f.writelines(lines)
