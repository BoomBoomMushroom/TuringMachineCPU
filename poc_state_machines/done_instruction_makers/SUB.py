from CustomClasses import State, statesArrayToJson

BLANK_CHARACTER = "_"
states = [
    # Add X and Y reg together and store the result in the accumulator
    
    State("Instruction_SUB", None, None, "L", "Instruction_SUB"),
    State("Instruction_SUB", "PC", "PC", "R", "SUB_GotoXReg"),

    State("SUB_GotoXReg", None, None, "R", "SUB_GotoXReg"),
    State("SUB_GotoXReg", "X", "X", "R", "SUB_XRegVal"),

    # Read the entire 4 register and store it's value in the state
    State("SUB_XRegVal", "0", "0", "R", "SUB_XRegVal_0"),
    State("SUB_XRegVal", "1", "1", "R", "SUB_XRegVal_1"),
    State("SUB_XRegVal_0", "0", "0", "R", "SUB_XRegVal_00"),
    State("SUB_XRegVal_0", "1", "1", "R", "SUB_XRegVal_01"),
    State("SUB_XRegVal_00", "0", "0", "R", "SUB_XRegVal_000"),
    State("SUB_XRegVal_00", "1", "1", "R", "SUB_XRegVal_001"),
    State("SUB_XRegVal_000", "0", "0", "R", "SUB_FindAcc_0000"),
    State("SUB_XRegVal_000", "1", "1", "R", "SUB_FindAcc_0001"),
    State("SUB_XRegVal_001", "0", "0", "R", "SUB_FindAcc_0010"),
    State("SUB_XRegVal_001", "1", "1", "R", "SUB_FindAcc_0011"),
    State("SUB_XRegVal_01", "0", "0", "R", "SUB_XRegVal_010"),
    State("SUB_XRegVal_01", "1", "1", "R", "SUB_XRegVal_011"),
    State("SUB_XRegVal_010", "0", "0", "R", "SUB_FindAcc_0100"),
    State("SUB_XRegVal_010", "1", "1", "R", "SUB_FindAcc_0101"),
    State("SUB_XRegVal_011", "0", "0", "R", "SUB_FindAcc_0110"),
    State("SUB_XRegVal_011", "1", "1", "R", "SUB_FindAcc_0111"),
    State("SUB_XRegVal_1", "0", "0", "R", "SUB_XRegVal_10"),
    State("SUB_XRegVal_1", "1", "1", "R", "SUB_XRegVal_11"),
    State("SUB_XRegVal_10", "0", "0", "R", "SUB_XRegVal_100"),
    State("SUB_XRegVal_10", "1", "1", "R", "SUB_XRegVal_101"),
    State("SUB_XRegVal_100", "0", "0", "R", "SUB_FindAcc_1000"),
    State("SUB_XRegVal_100", "1", "1", "R", "SUB_FindAcc_1001"),
    State("SUB_XRegVal_101", "0", "0", "R", "SUB_FindAcc_1010"),
    State("SUB_XRegVal_101", "1", "1", "R", "SUB_FindAcc_1011"),
    State("SUB_XRegVal_11", "0", "0", "R", "SUB_XRegVal_110"),
    State("SUB_XRegVal_11", "1", "1", "R", "SUB_XRegVal_111"),
    State("SUB_XRegVal_110", "0", "0", "R", "SUB_FindAcc_1100"),
    State("SUB_XRegVal_110", "1", "1", "R", "SUB_FindAcc_1101"),
    State("SUB_XRegVal_111", "0", "0", "R", "SUB_FindAcc_1110"),
    State("SUB_XRegVal_111", "1", "1", "R", "SUB_FindAcc_1111"),
    
    # Find the accumulator marker, and we can just go right until we find it since we left off after the X register (on the Y register marker in fact)
    State("SUB_FindAcc_0000", None, None, "R", "SUB_FindAcc_0000"),
    State("SUB_FindAcc_0000", "A", "A", "R", "SUB_WriteAcc_0000"),
    State("SUB_FindAcc_0001", None, None, "R", "SUB_FindAcc_0001"),
    State("SUB_FindAcc_0001", "A", "A", "R", "SUB_WriteAcc_0001"),
    State("SUB_FindAcc_0010", None, None, "R", "SUB_FindAcc_0010"),
    State("SUB_FindAcc_0010", "A", "A", "R", "SUB_WriteAcc_0010"),
    State("SUB_FindAcc_0011", None, None, "R", "SUB_FindAcc_0011"),
    State("SUB_FindAcc_0011", "A", "A", "R", "SUB_WriteAcc_0011"),
    State("SUB_FindAcc_0100", None, None, "R", "SUB_FindAcc_0100"),
    State("SUB_FindAcc_0100", "A", "A", "R", "SUB_WriteAcc_0100"),
    State("SUB_FindAcc_0101", None, None, "R", "SUB_FindAcc_0101"),
    State("SUB_FindAcc_0101", "A", "A", "R", "SUB_WriteAcc_0101"),
    State("SUB_FindAcc_0110", None, None, "R", "SUB_FindAcc_0110"),
    State("SUB_FindAcc_0110", "A", "A", "R", "SUB_WriteAcc_0110"),
    State("SUB_FindAcc_0111", None, None, "R", "SUB_FindAcc_0111"),
    State("SUB_FindAcc_0111", "A", "A", "R", "SUB_WriteAcc_0111"),
    State("SUB_FindAcc_1000", None, None, "R", "SUB_FindAcc_1000"),
    State("SUB_FindAcc_1000", "A", "A", "R", "SUB_WriteAcc_1000"),
    State("SUB_FindAcc_1001", None, None, "R", "SUB_FindAcc_1001"),
    State("SUB_FindAcc_1001", "A", "A", "R", "SUB_WriteAcc_1001"),
    State("SUB_FindAcc_1010", None, None, "R", "SUB_FindAcc_1010"),
    State("SUB_FindAcc_1010", "A", "A", "R", "SUB_WriteAcc_1010"),
    State("SUB_FindAcc_1011", None, None, "R", "SUB_FindAcc_1011"),
    State("SUB_FindAcc_1011", "A", "A", "R", "SUB_WriteAcc_1011"),
    State("SUB_FindAcc_1100", None, None, "R", "SUB_FindAcc_1100"),
    State("SUB_FindAcc_1100", "A", "A", "R", "SUB_WriteAcc_1100"),
    State("SUB_FindAcc_1101", None, None, "R", "SUB_FindAcc_1101"),
    State("SUB_FindAcc_1101", "A", "A", "R", "SUB_WriteAcc_1101"),
    State("SUB_FindAcc_1110", None, None, "R", "SUB_FindAcc_1110"),
    State("SUB_FindAcc_1110", "A", "A", "R", "SUB_WriteAcc_1110"),
    State("SUB_FindAcc_1111", None, None, "R", "SUB_FindAcc_1111"),
    State("SUB_FindAcc_1111", "A", "A", "R", "SUB_WriteAcc_1111"),
    
    # Write the binary digit into the accumulator
    State("SUB_WriteAcc_0000", None, "0", "R", "SUB_WriteAcc_000"),
    State("SUB_WriteAcc_000", None, "0", "R", "SUB_WriteAcc_00"),
    State("SUB_WriteAcc_00", None, "0", "R", "SUB_WriteAcc_0"),
    State("SUB_WriteAcc_0", None, "0", "R", "SUB_GotoYReg"),
    State("SUB_WriteAcc_0001", None, "0", "R", "SUB_WriteAcc_001"),
    State("SUB_WriteAcc_001", None, "0", "R", "SUB_WriteAcc_01"),
    State("SUB_WriteAcc_01", None, "0", "R", "SUB_WriteAcc_1"),
    State("SUB_WriteAcc_1", None, "1", "R", "SUB_GotoYReg"),
    State("SUB_WriteAcc_0010", None, "0", "R", "SUB_WriteAcc_010"),
    State("SUB_WriteAcc_010", None, "0", "R", "SUB_WriteAcc_10"),
    State("SUB_WriteAcc_10", None, "1", "R", "SUB_WriteAcc_0"),
    State("SUB_WriteAcc_0011", None, "0", "R", "SUB_WriteAcc_011"),
    State("SUB_WriteAcc_011", None, "0", "R", "SUB_WriteAcc_11"),
    State("SUB_WriteAcc_11", None, "1", "R", "SUB_WriteAcc_1"),
    State("SUB_WriteAcc_0100", None, "0", "R", "SUB_WriteAcc_100"),
    State("SUB_WriteAcc_100", None, "1", "R", "SUB_WriteAcc_00"),
    State("SUB_WriteAcc_0101", None, "0", "R", "SUB_WriteAcc_101"),
    State("SUB_WriteAcc_101", None, "1", "R", "SUB_WriteAcc_01"),
    State("SUB_WriteAcc_0110", None, "0", "R", "SUB_WriteAcc_110"),
    State("SUB_WriteAcc_110", None, "1", "R", "SUB_WriteAcc_10"),
    State("SUB_WriteAcc_0111", None, "0", "R", "SUB_WriteAcc_111"),
    State("SUB_WriteAcc_111", None, "1", "R", "SUB_WriteAcc_11"),
    State("SUB_WriteAcc_1000", None, "1", "R", "SUB_WriteAcc_000"),
    State("SUB_WriteAcc_1001", None, "1", "R", "SUB_WriteAcc_001"),
    State("SUB_WriteAcc_1010", None, "1", "R", "SUB_WriteAcc_010"),
    State("SUB_WriteAcc_1011", None, "1", "R", "SUB_WriteAcc_011"),
    State("SUB_WriteAcc_1100", None, "1", "R", "SUB_WriteAcc_100"),
    State("SUB_WriteAcc_1101", None, "1", "R", "SUB_WriteAcc_101"),
    State("SUB_WriteAcc_1110", None, "1", "R", "SUB_WriteAcc_110"),
    State("SUB_WriteAcc_1111", None, "1", "R", "SUB_WriteAcc_111"),
    
    # Goto the Y register, we are 100% to the right of it (meaning we go left now) since we have just written to the accumulator
    State("SUB_GotoYReg", None, None, "L", "SUB_GotoYReg"),
    State("SUB_GotoYReg", "Y", "Y", "R", "SUB_YRegVal"),
    
    # Read the entire 4 register and store it's value in the state
    # Since we just need to add the two's complement and we're going to increment the PC by 4 like ADD, we can just call add states on it's two's complement
    State("SUB_YRegVal", "0", "0", "R", "SUB_YRegVal_0"),
    State("SUB_YRegVal", "1", "1", "R", "SUB_YRegVal_1"),
    State("SUB_YRegVal_0", "0", "0", "R", "SUB_YRegVal_00"),
    State("SUB_YRegVal_0", "1", "1", "R", "SUB_YRegVal_01"),
    State("SUB_YRegVal_00", "0", "0", "R", "SUB_YRegVal_000"),
    State("SUB_YRegVal_00", "1", "1", "R", "SUB_YRegVal_001"),
    State("SUB_YRegVal_000", "0", "0", "R", "ADD_Finish"), # goto the ADD finish since we don't have our own finish b/c 
    State("SUB_YRegVal_000", "1", "1", "R", "ADD_Inc_1111_GotoAcc"), # 0001 -> 2's complement -> 1111
    State("SUB_YRegVal_001", "0", "0", "R", "ADD_Inc_1110_GotoAcc"), # 0010 -> 2's complement -> 1110
    State("SUB_YRegVal_001", "1", "1", "R", "ADD_Inc_1101_GotoAcc"), # 0011 -> 2's complement -> 1101
    State("SUB_YRegVal_01", "0", "0", "R", "SUB_YRegVal_010"),
    State("SUB_YRegVal_01", "1", "1", "R", "SUB_YRegVal_011"),
    State("SUB_YRegVal_010", "0", "0", "R", "ADD_Inc_1100_GotoAcc"), # 0100 -> 2's complement -> 1100
    State("SUB_YRegVal_010", "1", "1", "R", "ADD_Inc_1011_GotoAcc"), # 0101 -> 2's complement -> 1011
    State("SUB_YRegVal_011", "0", "0", "R", "ADD_Inc_1010_GotoAcc"), # 0110 -> 2's complement -> 1010
    State("SUB_YRegVal_011", "1", "1", "R", "ADD_Inc_1001_GotoAcc"), # 0111 -> 2's complement -> 1001
    State("SUB_YRegVal_1", "0", "0", "R", "SUB_YRegVal_10"),
    State("SUB_YRegVal_1", "1", "1", "R", "SUB_YRegVal_11"),
    State("SUB_YRegVal_10", "0", "0", "R", "SUB_YRegVal_100"),
    State("SUB_YRegVal_10", "1", "1", "R", "SUB_YRegVal_101"),
    State("SUB_YRegVal_100", "0", "0", "R", "ADD_Inc_1000_GotoAcc"), # 1000 -> 2's complement -> 1000
    State("SUB_YRegVal_100", "1", "1", "R", "ADD_Inc_0111_GotoAcc"), # 1001 -> 2's complement -> 0111
    State("SUB_YRegVal_101", "0", "0", "R", "ADD_Inc_0110_GotoAcc"), # 1010 -> 2's complement -> 0110
    State("SUB_YRegVal_101", "1", "1", "R", "ADD_Inc_0101_GotoAcc"), # 1011 -> 2's complement -> 0101
    State("SUB_YRegVal_11", "0", "0", "R", "SUB_YRegVal_110"),
    State("SUB_YRegVal_11", "1", "1", "R", "SUB_YRegVal_111"),
    State("SUB_YRegVal_110", "0", "0", "R", "ADD_Inc_0100_GotoAcc"), # 1100 -> 2's complement -> 0100
    State("SUB_YRegVal_110", "1", "1", "R", "ADD_Inc_0011_GotoAcc"), # 1101 -> 2's complement -> 0011
    State("SUB_YRegVal_111", "0", "0", "R", "ADD_Inc_0010_GotoAcc"), # 1110 -> 2's complement -> 0010
    State("SUB_YRegVal_111", "1", "1", "R", "ADD_Inc_0001_GotoAcc"), # 1111 -> 2's complement -> 0001
]


with open("./poc_state_machines/instruction_states/sub.turing", "w") as f:
    lines = ["[\n"]
    lines.extend(["\t"+s.__str__(isJson=True)+",\n" for s in states])
    lines[-1] = lines[-1][:-2] + "\n"
    lines.append("]")

    f.writelines(lines)
    print(f"Wrote {len(lines)} lines!")
