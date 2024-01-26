#RISC-V text for graph.c 
#author@lcsaszar01

#start of assembly code 


    SB s1, s2, imm     #call ammio acid store

    LB s3, rs1, imm      #call the ammino acid string

    SB rs1, rs2, imm     #x16 set a k-1 mer of 32 chars

    LB t0, rs1, imm      #load the 32char string

#For the prefixes

addi s4, s4, 0
FOR1: #Start of for using ammino acids
    beq s0, x0, EXIT
    add 
    jal x0, FOR1

FOR2: beq s0,  #stat of d


    jal x0, EXIT1

IF: BEQ   rs1, rs2, imm #if x in kmer_list equals,

    LW    rd, rs1, imm

    LW    rd, rs1, imm

    ADDI  rd, rs1, imm

    ADDI  t3, t3, 1  #increase counter_for_find 

    jal x0, FOR2

EXIT1:

IF0: BEQ x0, 

     BEQ x0, $zero
    
IF2: BLT $zero, #If the counter_for_find is greater in value than 0

EXIT:
