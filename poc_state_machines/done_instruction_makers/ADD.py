from CustomClasses import State, statesArrayToJson

BLANK_CHARACTER = "_"
states = [
    # Add X and Y reg together and store the result in the accumulator
    
    State("Instruction_ADD", None, None, "L", "Instruction_ADD"),
    State("Instruction_ADD", "PC", "PC", "R", "ADD_GotoXReg"),

    State("ADD_GotoXReg", None, None, "R", "ADD_GotoXReg"),
    State("ADD_GotoXReg", "X", "X", "R", "ADD_XRegVal"),

    # Read the entire 4 register and store it's value in the state
    State("ADD_XRegVal", "0", "0", "R", "ADD_XRegVal_0"),
    State("ADD_XRegVal", "1", "1", "R", "ADD_XRegVal_1"),
    State("ADD_XRegVal_0", "0", "0", "R", "ADD_XRegVal_00"),
    State("ADD_XRegVal_0", "1", "1", "R", "ADD_XRegVal_01"),
    State("ADD_XRegVal_00", "0", "0", "R", "ADD_XRegVal_000"),
    State("ADD_XRegVal_00", "1", "1", "R", "ADD_XRegVal_001"),
    State("ADD_XRegVal_000", "0", "0", "R", "ADD_FindAcc_0000"),
    State("ADD_XRegVal_000", "1", "1", "R", "ADD_FindAcc_0001"),
    State("ADD_XRegVal_001", "0", "0", "R", "ADD_FindAcc_0010"),
    State("ADD_XRegVal_001", "1", "1", "R", "ADD_FindAcc_0011"),
    State("ADD_XRegVal_01", "0", "0", "R", "ADD_XRegVal_010"),
    State("ADD_XRegVal_01", "1", "1", "R", "ADD_XRegVal_011"),
    State("ADD_XRegVal_010", "0", "0", "R", "ADD_FindAcc_0100"),
    State("ADD_XRegVal_010", "1", "1", "R", "ADD_FindAcc_0101"),
    State("ADD_XRegVal_011", "0", "0", "R", "ADD_FindAcc_0110"),
    State("ADD_XRegVal_011", "1", "1", "R", "ADD_FindAcc_0111"),
    State("ADD_XRegVal_1", "0", "0", "R", "ADD_XRegVal_10"),
    State("ADD_XRegVal_1", "1", "1", "R", "ADD_XRegVal_11"),
    State("ADD_XRegVal_10", "0", "0", "R", "ADD_XRegVal_100"),
    State("ADD_XRegVal_10", "1", "1", "R", "ADD_XRegVal_101"),
    State("ADD_XRegVal_100", "0", "0", "R", "ADD_FindAcc_1000"),
    State("ADD_XRegVal_100", "1", "1", "R", "ADD_FindAcc_1001"),
    State("ADD_XRegVal_101", "0", "0", "R", "ADD_FindAcc_1010"),
    State("ADD_XRegVal_101", "1", "1", "R", "ADD_FindAcc_1011"),
    State("ADD_XRegVal_11", "0", "0", "R", "ADD_XRegVal_110"),
    State("ADD_XRegVal_11", "1", "1", "R", "ADD_XRegVal_111"),
    State("ADD_XRegVal_110", "0", "0", "R", "ADD_FindAcc_1100"),
    State("ADD_XRegVal_110", "1", "1", "R", "ADD_FindAcc_1101"),
    State("ADD_XRegVal_111", "0", "0", "R", "ADD_FindAcc_1110"),
    State("ADD_XRegVal_111", "1", "1", "R", "ADD_FindAcc_1111"),
    
    # Find the accumulator marker, and we can just go right until we find it since we left off after the X register (on the Y register marker in fact)
    State("ADD_FindAcc_0000", None, None, "R", "ADD_FindAcc_0000"),
    State("ADD_FindAcc_0000", "A", "A", "R", "ADD_WriteAcc_0000"),
    State("ADD_FindAcc_0001", None, None, "R", "ADD_FindAcc_0001"),
    State("ADD_FindAcc_0001", "A", "A", "R", "ADD_WriteAcc_0001"),
    State("ADD_FindAcc_0010", None, None, "R", "ADD_FindAcc_0010"),
    State("ADD_FindAcc_0010", "A", "A", "R", "ADD_WriteAcc_0010"),
    State("ADD_FindAcc_0011", None, None, "R", "ADD_FindAcc_0011"),
    State("ADD_FindAcc_0011", "A", "A", "R", "ADD_WriteAcc_0011"),
    State("ADD_FindAcc_0100", None, None, "R", "ADD_FindAcc_0100"),
    State("ADD_FindAcc_0100", "A", "A", "R", "ADD_WriteAcc_0100"),
    State("ADD_FindAcc_0101", None, None, "R", "ADD_FindAcc_0101"),
    State("ADD_FindAcc_0101", "A", "A", "R", "ADD_WriteAcc_0101"),
    State("ADD_FindAcc_0110", None, None, "R", "ADD_FindAcc_0110"),
    State("ADD_FindAcc_0110", "A", "A", "R", "ADD_WriteAcc_0110"),
    State("ADD_FindAcc_0111", None, None, "R", "ADD_FindAcc_0111"),
    State("ADD_FindAcc_0111", "A", "A", "R", "ADD_WriteAcc_0111"),
    State("ADD_FindAcc_1000", None, None, "R", "ADD_FindAcc_1000"),
    State("ADD_FindAcc_1000", "A", "A", "R", "ADD_WriteAcc_1000"),
    State("ADD_FindAcc_1001", None, None, "R", "ADD_FindAcc_1001"),
    State("ADD_FindAcc_1001", "A", "A", "R", "ADD_WriteAcc_1001"),
    State("ADD_FindAcc_1010", None, None, "R", "ADD_FindAcc_1010"),
    State("ADD_FindAcc_1010", "A", "A", "R", "ADD_WriteAcc_1010"),
    State("ADD_FindAcc_1011", None, None, "R", "ADD_FindAcc_1011"),
    State("ADD_FindAcc_1011", "A", "A", "R", "ADD_WriteAcc_1011"),
    State("ADD_FindAcc_1100", None, None, "R", "ADD_FindAcc_1100"),
    State("ADD_FindAcc_1100", "A", "A", "R", "ADD_WriteAcc_1100"),
    State("ADD_FindAcc_1101", None, None, "R", "ADD_FindAcc_1101"),
    State("ADD_FindAcc_1101", "A", "A", "R", "ADD_WriteAcc_1101"),
    State("ADD_FindAcc_1110", None, None, "R", "ADD_FindAcc_1110"),
    State("ADD_FindAcc_1110", "A", "A", "R", "ADD_WriteAcc_1110"),
    State("ADD_FindAcc_1111", None, None, "R", "ADD_FindAcc_1111"),
    State("ADD_FindAcc_1111", "A", "A", "R", "ADD_WriteAcc_1111"),
    
    # Write the binary digit into the accumulator
    State("ADD_WriteAcc_0000", None, "0", "R", "ADD_WriteAcc_000"),
    State("ADD_WriteAcc_000", None, "0", "R", "ADD_WriteAcc_00"),
    State("ADD_WriteAcc_00", None, "0", "R", "ADD_WriteAcc_0"),
    State("ADD_WriteAcc_0", None, "0", "R", "ADD_GotoYReg"),
    State("ADD_WriteAcc_0001", None, "0", "R", "ADD_WriteAcc_001"),
    State("ADD_WriteAcc_001", None, "0", "R", "ADD_WriteAcc_01"),
    State("ADD_WriteAcc_01", None, "0", "R", "ADD_WriteAcc_1"),
    State("ADD_WriteAcc_1", None, "1", "R", "ADD_GotoYReg"),
    State("ADD_WriteAcc_0010", None, "0", "R", "ADD_WriteAcc_010"),
    State("ADD_WriteAcc_010", None, "0", "R", "ADD_WriteAcc_10"),
    State("ADD_WriteAcc_10", None, "1", "R", "ADD_WriteAcc_0"),
    State("ADD_WriteAcc_0011", None, "0", "R", "ADD_WriteAcc_011"),
    State("ADD_WriteAcc_011", None, "0", "R", "ADD_WriteAcc_11"),
    State("ADD_WriteAcc_11", None, "1", "R", "ADD_WriteAcc_1"),
    State("ADD_WriteAcc_0100", None, "0", "R", "ADD_WriteAcc_100"),
    State("ADD_WriteAcc_100", None, "1", "R", "ADD_WriteAcc_00"),
    State("ADD_WriteAcc_0101", None, "0", "R", "ADD_WriteAcc_101"),
    State("ADD_WriteAcc_101", None, "1", "R", "ADD_WriteAcc_01"),
    State("ADD_WriteAcc_0110", None, "0", "R", "ADD_WriteAcc_110"),
    State("ADD_WriteAcc_110", None, "1", "R", "ADD_WriteAcc_10"),
    State("ADD_WriteAcc_0111", None, "0", "R", "ADD_WriteAcc_111"),
    State("ADD_WriteAcc_111", None, "1", "R", "ADD_WriteAcc_11"),
    State("ADD_WriteAcc_1000", None, "1", "R", "ADD_WriteAcc_000"),
    State("ADD_WriteAcc_1001", None, "1", "R", "ADD_WriteAcc_001"),
    State("ADD_WriteAcc_1010", None, "1", "R", "ADD_WriteAcc_010"),
    State("ADD_WriteAcc_1011", None, "1", "R", "ADD_WriteAcc_011"),
    State("ADD_WriteAcc_1100", None, "1", "R", "ADD_WriteAcc_100"),
    State("ADD_WriteAcc_1101", None, "1", "R", "ADD_WriteAcc_101"),
    State("ADD_WriteAcc_1110", None, "1", "R", "ADD_WriteAcc_110"),
    State("ADD_WriteAcc_1111", None, "1", "R", "ADD_WriteAcc_111"),
    
    # Goto the Y register, we are 100% to the right of it (meaning we go left now) since we have just written to the accumulator
    State("ADD_GotoYReg", None, None, "L", "ADD_GotoYReg"),
    State("ADD_GotoYReg", "Y", "Y", "R", "ADD_YRegVal"),
    
    # Read the entire 4 register and store it's value in the state
    State("ADD_YRegVal", "0", "0", "R", "ADD_YRegVal_0"),
    State("ADD_YRegVal", "1", "1", "R", "ADD_YRegVal_1"),
    State("ADD_YRegVal_0", "0", "0", "R", "ADD_YRegVal_00"),
    State("ADD_YRegVal_0", "1", "1", "R", "ADD_YRegVal_01"),
    State("ADD_YRegVal_00", "0", "0", "R", "ADD_YRegVal_000"),
    State("ADD_YRegVal_00", "1", "1", "R", "ADD_YRegVal_001"),
    State("ADD_YRegVal_000", "0", "0", "R", "ADD_Finish"),
    State("ADD_YRegVal_000", "1", "1", "R", "ADD_Inc_0001_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_001", "0", "0", "R", "ADD_Inc_0010_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_001", "1", "1", "R", "ADD_Inc_0011_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_01", "0", "0", "R", "ADD_YRegVal_010"),
    State("ADD_YRegVal_01", "1", "1", "R", "ADD_YRegVal_011"),
    State("ADD_YRegVal_010", "0", "0", "R", "ADD_Inc_0100_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_010", "1", "1", "R", "ADD_Inc_0101_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_011", "0", "0", "R", "ADD_Inc_0110_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_011", "1", "1", "R", "ADD_Inc_0111_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_1", "0", "0", "R", "ADD_YRegVal_10"),
    State("ADD_YRegVal_1", "1", "1", "R", "ADD_YRegVal_11"),
    State("ADD_YRegVal_10", "0", "0", "R", "ADD_YRegVal_100"),
    State("ADD_YRegVal_10", "1", "1", "R", "ADD_YRegVal_101"),
    State("ADD_YRegVal_100", "0", "0", "R", "ADD_Inc_1000_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_100", "1", "1", "R", "ADD_Inc_1001_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_101", "0", "0", "R", "ADD_Inc_1010_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_101", "1", "1", "R", "ADD_Inc_1011_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_11", "0", "0", "R", "ADD_YRegVal_110"),
    State("ADD_YRegVal_11", "1", "1", "R", "ADD_YRegVal_111"),
    State("ADD_YRegVal_110", "0", "0", "R", "ADD_Inc_1100_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_110", "1", "1", "R", "ADD_Inc_1101_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_111", "0", "0", "R", "ADD_Inc_1110_GotoAcc"), # make these add the value we extracted to the accumulator register!
    State("ADD_YRegVal_111", "1", "1", "R", "ADD_Inc_1111_GotoAcc"), # make these add the value we extracted to the accumulator register!
    
    # All the increments we need
    State("ADD_Inc_0001_GotoAcc", None, None, "L", "ADD_Inc_0001_GotoAcc"),
    State("ADD_Inc_0001_GotoAcc", "A", "A", "R", "ADD_Inc_0001_GoRight3Times"),
    State("ADD_Inc_0001_GoRight3Times", None, None, "R", "ADD_Inc_0001_GoRight2Times"),
    State("ADD_Inc_0001_GoRight2Times", None, None, "R", "ADD_Inc_0001_GoRight1Times"),
    State("ADD_Inc_0001_GoRight1Times", None, None, "R", "ADD_Inc_0001"),
    State("ADD_Inc_0001", "A", "A", "R", "ADD_Finish"),
    State("ADD_Inc_0001", "0", "1", "L", "ADD_Finish"),
    State("ADD_Inc_0001", "1", "0", "L", "ADD_Inc_0001"),
    State("ADD_Inc_0010_GotoAcc", None, None, "L", "ADD_Inc_0010_GotoAcc"),
    State("ADD_Inc_0010_GotoAcc", "A", "A", "R", "ADD_Inc_0010_GoRight3Times"),
    State("ADD_Inc_0010_GoRight3Times", None, None, "R", "ADD_Inc_0010_GoRight2Times"),
    State("ADD_Inc_0010_GoRight2Times", None, None, "R", "ADD_Inc_0010_GoRight1Times"),
    State("ADD_Inc_0010_GoRight1Times", None, None, "R", "ADD_Inc_0010"),
    State("ADD_Inc_0010", "A", "A", "R", "ADD_Inc_0001_GotoAcc"),
    State("ADD_Inc_0010", "0", "1", "L", "ADD_Inc_0001_GotoAcc"),
    State("ADD_Inc_0010", "1", "0", "L", "ADD_Inc_0010"),
    State("ADD_Inc_0011_GotoAcc", None, None, "L", "ADD_Inc_0011_GotoAcc"),
    State("ADD_Inc_0011_GotoAcc", "A", "A", "R", "ADD_Inc_0011_GoRight3Times"),
    State("ADD_Inc_0011_GoRight3Times", None, None, "R", "ADD_Inc_0011_GoRight2Times"),
    State("ADD_Inc_0011_GoRight2Times", None, None, "R", "ADD_Inc_0011_GoRight1Times"),
    State("ADD_Inc_0011_GoRight1Times", None, None, "R", "ADD_Inc_0011"),
    State("ADD_Inc_0011", "A", "A", "R", "ADD_Inc_0010_GotoAcc"),
    State("ADD_Inc_0011", "0", "1", "L", "ADD_Inc_0010_GotoAcc"),
    State("ADD_Inc_0011", "1", "0", "L", "ADD_Inc_0011"),
    State("ADD_Inc_0100_GotoAcc", None, None, "L", "ADD_Inc_0100_GotoAcc"),
    State("ADD_Inc_0100_GotoAcc", "A", "A", "R", "ADD_Inc_0100_GoRight3Times"),
    State("ADD_Inc_0100_GoRight3Times", None, None, "R", "ADD_Inc_0100_GoRight2Times"),
    State("ADD_Inc_0100_GoRight2Times", None, None, "R", "ADD_Inc_0100_GoRight1Times"),
    State("ADD_Inc_0100_GoRight1Times", None, None, "R", "ADD_Inc_0100"),
    State("ADD_Inc_0100", "A", "A", "R", "ADD_Inc_0011_GotoAcc"),
    State("ADD_Inc_0100", "0", "1", "L", "ADD_Inc_0011_GotoAcc"),
    State("ADD_Inc_0100", "1", "0", "L", "ADD_Inc_0100"),
    State("ADD_Inc_0101_GotoAcc", None, None, "L", "ADD_Inc_0101_GotoAcc"),
    State("ADD_Inc_0101_GotoAcc", "A", "A", "R", "ADD_Inc_0101_GoRight3Times"),
    State("ADD_Inc_0101_GoRight3Times", None, None, "R", "ADD_Inc_0101_GoRight2Times"),
    State("ADD_Inc_0101_GoRight2Times", None, None, "R", "ADD_Inc_0101_GoRight1Times"),
    State("ADD_Inc_0101_GoRight1Times", None, None, "R", "ADD_Inc_0101"),
    State("ADD_Inc_0101", "A", "A", "R", "ADD_Inc_0100_GotoAcc"),
    State("ADD_Inc_0101", "0", "1", "L", "ADD_Inc_0100_GotoAcc"),
    State("ADD_Inc_0101", "1", "0", "L", "ADD_Inc_0101"),
    State("ADD_Inc_0110_GotoAcc", None, None, "L", "ADD_Inc_0110_GotoAcc"),
    State("ADD_Inc_0110_GotoAcc", "A", "A", "R", "ADD_Inc_0110_GoRight3Times"),
    State("ADD_Inc_0110_GoRight3Times", None, None, "R", "ADD_Inc_0110_GoRight2Times"),
    State("ADD_Inc_0110_GoRight2Times", None, None, "R", "ADD_Inc_0110_GoRight1Times"),
    State("ADD_Inc_0110_GoRight1Times", None, None, "R", "ADD_Inc_0110"),
    State("ADD_Inc_0110", "A", "A", "R", "ADD_Inc_0101_GotoAcc"),
    State("ADD_Inc_0110", "0", "1", "L", "ADD_Inc_0101_GotoAcc"),
    State("ADD_Inc_0110", "1", "0", "L", "ADD_Inc_0110"),
    State("ADD_Inc_0111_GotoAcc", None, None, "L", "ADD_Inc_0111_GotoAcc"),
    State("ADD_Inc_0111_GotoAcc", "A", "A", "R", "ADD_Inc_0111_GoRight3Times"),
    State("ADD_Inc_0111_GoRight3Times", None, None, "R", "ADD_Inc_0111_GoRight2Times"),
    State("ADD_Inc_0111_GoRight2Times", None, None, "R", "ADD_Inc_0111_GoRight1Times"),
    State("ADD_Inc_0111_GoRight1Times", None, None, "R", "ADD_Inc_0111"),
    State("ADD_Inc_0111", "A", "A", "R", "ADD_Inc_0110_GotoAcc"),
    State("ADD_Inc_0111", "0", "1", "L", "ADD_Inc_0110_GotoAcc"),
    State("ADD_Inc_0111", "1", "0", "L", "ADD_Inc_0111"),
    State("ADD_Inc_1000_GotoAcc", None, None, "L", "ADD_Inc_1000_GotoAcc"),
    State("ADD_Inc_1000_GotoAcc", "A", "A", "R", "ADD_Inc_1000_GoRight3Times"),
    State("ADD_Inc_1000_GoRight3Times", None, None, "R", "ADD_Inc_1000_GoRight2Times"),
    State("ADD_Inc_1000_GoRight2Times", None, None, "R", "ADD_Inc_1000_GoRight1Times"),
    State("ADD_Inc_1000_GoRight1Times", None, None, "R", "ADD_Inc_1000"),
    State("ADD_Inc_1000", "A", "A", "R", "ADD_Inc_0111_GotoAcc"),
    State("ADD_Inc_1000", "0", "1", "L", "ADD_Inc_0111_GotoAcc"),
    State("ADD_Inc_1000", "1", "0", "L", "ADD_Inc_1000"),
    State("ADD_Inc_1001_GotoAcc", None, None, "L", "ADD_Inc_1001_GotoAcc"),
    State("ADD_Inc_1001_GotoAcc", "A", "A", "R", "ADD_Inc_1001_GoRight3Times"),
    State("ADD_Inc_1001_GoRight3Times", None, None, "R", "ADD_Inc_1001_GoRight2Times"),
    State("ADD_Inc_1001_GoRight2Times", None, None, "R", "ADD_Inc_1001_GoRight1Times"),
    State("ADD_Inc_1001_GoRight1Times", None, None, "R", "ADD_Inc_1001"),
    State("ADD_Inc_1001", "A", "A", "R", "ADD_Inc_1000_GotoAcc"),
    State("ADD_Inc_1001", "0", "1", "L", "ADD_Inc_1000_GotoAcc"),
    State("ADD_Inc_1001", "1", "0", "L", "ADD_Inc_1001"),
    State("ADD_Inc_1010_GotoAcc", None, None, "L", "ADD_Inc_1010_GotoAcc"),
    State("ADD_Inc_1010_GotoAcc", "A", "A", "R", "ADD_Inc_1010_GoRight3Times"),
    State("ADD_Inc_1010_GoRight3Times", None, None, "R", "ADD_Inc_1010_GoRight2Times"),
    State("ADD_Inc_1010_GoRight2Times", None, None, "R", "ADD_Inc_1010_GoRight1Times"),
    State("ADD_Inc_1010_GoRight1Times", None, None, "R", "ADD_Inc_1010"),
    State("ADD_Inc_1010", "A", "A", "R", "ADD_Inc_1001_GotoAcc"),
    State("ADD_Inc_1010", "0", "1", "L", "ADD_Inc_1001_GotoAcc"),
    State("ADD_Inc_1010", "1", "0", "L", "ADD_Inc_1010"),
    State("ADD_Inc_1011_GotoAcc", None, None, "L", "ADD_Inc_1011_GotoAcc"),
    State("ADD_Inc_1011_GotoAcc", "A", "A", "R", "ADD_Inc_1011_GoRight3Times"),
    State("ADD_Inc_1011_GoRight3Times", None, None, "R", "ADD_Inc_1011_GoRight2Times"),
    State("ADD_Inc_1011_GoRight2Times", None, None, "R", "ADD_Inc_1011_GoRight1Times"),
    State("ADD_Inc_1011_GoRight1Times", None, None, "R", "ADD_Inc_1011"),
    State("ADD_Inc_1011", "A", "A", "R", "ADD_Inc_1010_GotoAcc"),
    State("ADD_Inc_1011", "0", "1", "L", "ADD_Inc_1010_GotoAcc"),
    State("ADD_Inc_1011", "1", "0", "L", "ADD_Inc_1011"),
    State("ADD_Inc_1100_GotoAcc", None, None, "L", "ADD_Inc_1100_GotoAcc"),
    State("ADD_Inc_1100_GotoAcc", "A", "A", "R", "ADD_Inc_1100_GoRight3Times"),
    State("ADD_Inc_1100_GoRight3Times", None, None, "R", "ADD_Inc_1100_GoRight2Times"),
    State("ADD_Inc_1100_GoRight2Times", None, None, "R", "ADD_Inc_1100_GoRight1Times"),
    State("ADD_Inc_1100_GoRight1Times", None, None, "R", "ADD_Inc_1100"),
    State("ADD_Inc_1100", "A", "A", "R", "ADD_Inc_1011_GotoAcc"),
    State("ADD_Inc_1100", "0", "1", "L", "ADD_Inc_1011_GotoAcc"),
    State("ADD_Inc_1100", "1", "0", "L", "ADD_Inc_1100"),
    State("ADD_Inc_1101_GotoAcc", None, None, "L", "ADD_Inc_1101_GotoAcc"),
    State("ADD_Inc_1101_GotoAcc", "A", "A", "R", "ADD_Inc_1101_GoRight3Times"),
    State("ADD_Inc_1101_GoRight3Times", None, None, "R", "ADD_Inc_1101_GoRight2Times"),
    State("ADD_Inc_1101_GoRight2Times", None, None, "R", "ADD_Inc_1101_GoRight1Times"),
    State("ADD_Inc_1101_GoRight1Times", None, None, "R", "ADD_Inc_1101"),
    State("ADD_Inc_1101", "A", "A", "R", "ADD_Inc_1100_GotoAcc"),
    State("ADD_Inc_1101", "0", "1", "L", "ADD_Inc_1100_GotoAcc"),
    State("ADD_Inc_1101", "1", "0", "L", "ADD_Inc_1101"),
    State("ADD_Inc_1110_GotoAcc", None, None, "L", "ADD_Inc_1110_GotoAcc"),
    State("ADD_Inc_1110_GotoAcc", "A", "A", "R", "ADD_Inc_1110_GoRight3Times"),
    State("ADD_Inc_1110_GoRight3Times", None, None, "R", "ADD_Inc_1110_GoRight2Times"),
    State("ADD_Inc_1110_GoRight2Times", None, None, "R", "ADD_Inc_1110_GoRight1Times"),
    State("ADD_Inc_1110_GoRight1Times", None, None, "R", "ADD_Inc_1110"),
    State("ADD_Inc_1110", "A", "A", "R", "ADD_Inc_1101_GotoAcc"),
    State("ADD_Inc_1110", "0", "1", "L", "ADD_Inc_1101_GotoAcc"),
    State("ADD_Inc_1110", "1", "0", "L", "ADD_Inc_1110"),
    State("ADD_Inc_1111_GotoAcc", None, None, "L", "ADD_Inc_1111_GotoAcc"),
    State("ADD_Inc_1111_GotoAcc", "A", "A", "R", "ADD_Inc_1111_GoRight3Times"),
    State("ADD_Inc_1111_GoRight3Times", None, None, "R", "ADD_Inc_1111_GoRight2Times"),
    State("ADD_Inc_1111_GoRight2Times", None, None, "R", "ADD_Inc_1111_GoRight1Times"),
    State("ADD_Inc_1111_GoRight1Times", None, None, "R", "ADD_Inc_1111"),
    State("ADD_Inc_1111", "A", "A", "R", "ADD_Inc_1110_GotoAcc"),
    State("ADD_Inc_1111", "0", "1", "L", "ADD_Inc_1110_GotoAcc"),
    State("ADD_Inc_1111", "1", "0", "L", "ADD_Inc_1111"),
    
    State("ADD_Finish", None, None, "L", "IncPCBy_4"), # Increment PC by 4 since it's 4 bits for the opcode and we took no operands
]

outStates = []

def createStates(name="", binary=""):
    currentStateName = name + binary
    
    binaryAsInt = int(binary, 2)
    binaryMinusOne = bin(binaryAsInt - 1)[2:].zfill(4)
    if binaryAsInt - 1 < 0: binaryMinusOne = "0000" # just make it zero so i'll fix it later
    
    # States to increment the accumulator register
    
    hitAccGoRight = State(currentStateName + "_GotoAcc", "A", "A", "R", currentStateName + "_GoRight3Times") # puts us on the MSB of the accumulator
    moveLeftToAcc = State(currentStateName + "_GotoAcc", None, None, "L", currentStateName + "_GotoAcc")

    goRight3 = State(currentStateName + "_GoRight3Times", None, None, "R", currentStateName + "_GoRight2Times")
    goRight2 = State(currentStateName + "_GoRight2Times", None, None, "R", currentStateName + "_GoRight1Times")
    goRight1 = State(currentStateName + "_GoRight1Times", None, None, "R", currentStateName)
    
    accumulatorOverflowFailsafe = State(currentStateName, "A", "A", "R", name + binaryMinusOne) # if we hit the accumulator start character then we end the increment as we overflowed
    readZeroNextInc = State(currentStateName, "0", "1", "L", name + binaryMinusOne + "_GotoAcc") # if read a zero, write a one and move on to the next increment
    readOneKeepGoing = State(currentStateName, "1", "0", "L", currentStateName) # if read a one, write a zero and keep going until we hit a zero or the accumulator register start character
    outStates.extend([moveLeftToAcc, hitAccGoRight, goRight3, goRight2, goRight1, accumulatorOverflowFailsafe, readZeroNextInc, readOneKeepGoing])
    
    # Create more states after the first digit is removed
    #createStates(name, binaryFirstDigitRemoved)

for i in range(0, 2**4):
    binaryNum = bin(i)[2:].zfill(4)
    #print(binaryNum)
    createStates("ADD_Inc_", binaryNum)

#createStates("ADD_FindAcc_", "")
#print(len(outStates))
#print(statesArrayToJson(outStates, isJson=False))

with open("./poc_state_machines/instruction_states/add.turing", "w") as f:
    lines = ["[\n"]
    lines.extend(["\t"+s.__str__(isJson=True)+",\n" for s in states])
    lines[-1] = lines[-1][:-2] + "\n"
    lines.append("]")

    f.writelines(lines)
    print(f"Wrote {len(lines)} lines!")
