	.file	"graph.c"
	.option pic
	.attribute arch, "rv64i2p1_m2p0_a2p1_f2p2_d2p2_c2p0_zicsr2p0_zifencei2p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.section	.rodata
	.align	3
.LC0:
	.string	"setting up graph"
	.align	3
.LC1:
	.string	"r"
	.align	3
.LC2:
	.string	"kmer_lst.txt"
	.align	3
.LC3:
	.string	"Done importing kmer files."
	.align	3
.LC4:
	.string	"%c\n"
	.align	3
.LC5:
	.string	"%s"
	.align	3
.LC6:
	.string	"Suffix"
	.text
	.align	1
	.globl	main
	.type	main, @function
main:
.LFB6:
	.cfi_startproc
	addi	sp,sp,-32
	.cfi_def_cfa_offset 32
	sd	ra,24(sp)
	sd	s0,16(sp)
	sd	s1,8(sp)
	.cfi_offset 1, -8
	.cfi_offset 8, -16
	.cfi_offset 9, -24
	addi	s0,sp,32
	.cfi_def_cfa 8, 0
	li	t0,-241664
	addi	t0,t0,1984
	add	sp,sp,t0
	mv	a4,a0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sd	a1,1984(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	a4,1996(a5)
	la	a5,__stack_chk_guard
	ld	a4, 0(a5)
	sd	a4, -40(s0)
	li	a4, 0
	lla	a0,.LC0
	call	puts@plt
	li	a5,-237568
	addi	a5,a5,-32
	add	s1,a5,s0
	lla	a1,.LC1
	lla	a0,.LC2
	call	fopen@plt
	mv	a5,a0
	sd	a5,-2048(s1)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2004(a5)
	j	.L2
.L5:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2008(a5)
	j	.L3
.L4:
	li	a5,-237568
	addi	a5,a5,-2024
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a3,2008(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a2,2004(a5)
	li	a5,100
	mul	a5,a2,a5
	add	a5,a3,a5
	add	a4,a4,a5
	li	a5,-237568
	addi	a5,a5,-32
	add	a5,a5,s0
	ld	a2,-2048(a5)
	li	a1,8192
	mv	a0,a4
	call	fgets@plt
	li	a5,-237568
	addi	a5,a5,-32
	add	a5,a5,s0
	ld	a0,-2048(a5)
	call	fclose@plt
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,-241664
	addi	a4,a4,-32
	add	a4,a4,s0
	lw	a4,2008(a4)
	addiw	a4,a4,1
	sw	a4,2008(a5)
.L3:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2008(a5)
	sext.w	a4,a5
	li	a5,99
	ble	a4,a5,.L4
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,-241664
	addi	a4,a4,-32
	add	a4,a4,s0
	lw	a4,2004(a4)
	addiw	a4,a4,1
	sw	a4,2004(a5)
.L2:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2004(a5)
	sext.w	a4,a5
	li	a5,999
	ble	a4,a5,.L5
	lla	a0,.LC3
	call	puts@plt
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2032(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2036(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2040(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2012(a5)
	li	a5,-8192
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,1195593728
	addi	a4,a4,1089
	sw	a4,-328(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2016(a5)
	j	.L6
.L14:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,-241664
	addi	a4,a4,-32
	add	a4,a4,s0
	lw	a4,2012(a4)
	addiw	a4,a4,1
	sw	a4,2012(a5)
	li	a5,-8192
	addi	a5,a5,-32
	add	a5,a5,s0
	sd	zero,-320(a5)
	sd	zero,-312(a5)
	sd	zero,-304(a5)
	sd	zero,-296(a5)
	sd	zero,-288(a5)
	sd	zero,-280(a5)
	sd	zero,-272(a5)
	sd	zero,-264(a5)
	sd	zero,-256(a5)
	sd	zero,-248(a5)
	sd	zero,-240(a5)
	sd	zero,-232(a5)
	sw	zero,-224(a5)
	li	a5,-8192
	addi	a5,a5,-32
	add	a5,a5,s0
	sd	zero,-216(a5)
	sd	zero,-208(a5)
	sd	zero,-200(a5)
	sd	zero,-192(a5)
	sd	zero,-184(a5)
	sd	zero,-176(a5)
	sd	zero,-168(a5)
	sd	zero,-160(a5)
	sd	zero,-152(a5)
	sd	zero,-144(a5)
	sd	zero,-136(a5)
	sd	zero,-128(a5)
	sw	zero,-120(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2020(a5)
	j	.L7
.L12:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2024(a5)
	j	.L8
.L11:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2028(a5)
	j	.L9
.L10:
	li	a5,-8192
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2020(a5)
	add	a5,a4,a5
	lbu	a5,-328(a5)
	sext.w	a5,a5
	mv	a1,a5
	lla	a0,.LC4
	call	printf@plt
	li	a5,-237568
	addi	a5,a5,-2024
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a3,2028(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a2,2024(a5)
	li	a5,100
	mul	a5,a2,a5
	add	a5,a3,a5
	add	a3,a4,a5
	li	a5,-8192
	addi	a5,a5,-328
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2020(a5)
	add	a5,a4,a5
	mv	a1,a5
	mv	a0,a3
	call	strcat@plt
	li	a5,-8192
	addi	a5,a5,-8
	addi	a5,a5,-32
	add	a5,a5,s0
	mv	a0,a5
	call	puts@plt
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,-241664
	addi	a4,a4,-32
	add	a4,a4,s0
	lw	a4,2028(a4)
	addiw	a4,a4,1
	sw	a4,2028(a5)
.L9:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2028(a5)
	sext.w	a4,a5
	li	a5,100
	ble	a4,a5,.L10
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,-241664
	addi	a4,a4,-32
	add	a4,a4,s0
	lw	a4,2024(a4)
	addiw	a4,a4,1
	sw	a4,2024(a5)
.L8:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2024(a5)
	sext.w	a4,a5
	li	a5,1000
	ble	a4,a5,.L11
	li	a5,-8192
	addi	a5,a5,-112
	addi	a5,a5,-32
	add	a5,a5,s0
	lla	a1,.LC5
	mv	a0,a5
	call	printf@plt
	li	a5,-237568
	addi	a5,a5,-32
	add	a5,a5,s0
	sd	zero,-2032(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	sw	zero,2044(a5)
	li	a5,-8192
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2020(a5)
	add	a5,a4,a5
	lbu	a3,-328(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a2,2044(a5)
	li	a5,-237568
	addi	a5,a5,-2032
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-8192
	addi	a5,a5,-320
	addi	a5,a5,-32
	add	a1,a5,s0
	mv	a5,a2
	lla	a2,.LC6
	li	a0,0
	call	createNodes
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,-241664
	addi	a4,a4,-32
	add	a4,a4,s0
	lw	a4,2020(a4)
	addiw	a4,a4,1
	sw	a4,2020(a5)
.L7:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2020(a5)
	sext.w	a4,a5
	li	a5,3
	ble	a4,a5,.L12
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2036(a5)
	sext.w	a5,a5
	ble	a5,zero,.L13
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2036(a5)
	fcvt.d.w	fa4,a5
	li	a5,-237568
	addi	a5,a5,-32
	add	a5,a5,s0
	lla	a4,.LC7
	fld	fa5,0(a4)
	fdiv.d	fa5,fa4,fa5
	fsd	fa5,-2040(a5)
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2036(a5)
	fcvt.d.w	fa5,a5
	li	a5,-139264
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2012(a5)
	slli	a5,a5,4
	add	a5,a4,a5
	fsd	fa5,-320(a5)
	li	a5,-139264
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a5,2012(a5)
	slli	a5,a5,4
	add	a5,a4,a5
	li	a4,-237568
	addi	a4,a4,-32
	add	a4,a4,s0
	fld	fa5,-2040(a4)
	fsd	fa5,-328(a5)
.L13:
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	li	a4,-241664
	addi	a4,a4,-32
	add	a4,a4,s0
	lw	a4,2016(a4)
	addiw	a4,a4,1
	sw	a4,2016(a5)
.L6:
	li	a5,-241664
	addi	a5,a5,-32
	add	a4,a5,s0
	li	a5,-241664
	addi	a5,a5,-32
	add	a5,a5,s0
	lw	a4,2016(a4)
	lw	a5,2032(a5)
	sext.w	a4,a4
	sext.w	a5,a5
	ble	a4,a5,.L14
	li	a5,0
	mv	a4,a5
	la	a5,__stack_chk_guard
	ld	a3, -40(s0)
	ld	a5, 0(a5)
	xor	a5, a3, a5
	li	a3, 0
	beq	a5,zero,.L16
	call	__stack_chk_fail@plt
.L16:
	mv	a0,a4
	li	t0,241664
	addi	t0,t0,-1984
	add	sp,sp,t0
	.cfi_def_cfa 2, 32
	ld	ra,24(sp)
	.cfi_restore 1
	ld	s0,16(sp)
	.cfi_restore 8
	ld	s1,8(sp)
	.cfi_restore 9
	addi	sp,sp,32
	.cfi_def_cfa_offset 0
	jr	ra
	.cfi_endproc
.LFE6:
	.size	main, .-main
	.section	.rodata
	.align	3
.LC8:
	.string	"Maximum number of nodes reached."
	.text
	.align	1
	.globl	createNodes
	.type	createNodes, @function
createNodes:
.LFB7:
	.cfi_startproc
	addi	sp,sp,-208
	.cfi_def_cfa_offset 208
	sd	ra,200(sp)
	sd	s0,192(sp)
	.cfi_offset 1, -8
	.cfi_offset 8, -16
	addi	s0,sp,208
	.cfi_def_cfa 8, 0
	sd	a0,-168(s0)
	sd	a1,-176(s0)
	sd	a2,-184(s0)
	sd	a4,-200(s0)
	mv	a4,a5
	mv	a5,a3
	sb	a5,-185(s0)
	mv	a5,a4
	sw	a5,-192(s0)
	la	a5,__stack_chk_guard
	ld	a4, 0(a5)
	sd	a4, -24(s0)
	li	a4, 0
	ld	a4,-168(s0)
	li	a5,122880
	add	a5,a4,a5
	lw	a5,1120(a5)
	mv	a4,a5
	li	a5,999
	bgt	a4,a5,.L18
	addi	a5,s0,-152
	ld	a1,-176(s0)
	mv	a0,a5
	call	strcpy@plt
	addi	a5,s0,-152
	addi	a5,a5,100
	ld	a1,-184(s0)
	mv	a0,a5
	call	strcpy@plt
	lbu	a5,-185(s0)
	sb	a5,-42(s0)
	ld	a5,-200(s0)
	lw	a5,0(a5)
	sw	a5,-40(s0)
	ld	a5,-200(s0)
	lw	a5,4(a5)
	sw	a5,-36(s0)
	lw	a5,-192(s0)
	sw	a5,-32(s0)
	ld	a4,-168(s0)
	li	a5,122880
	add	a5,a4,a5
	lw	a4,1120(a5)
	addiw	a5,a4,1
	sext.w	a3,a5
	ld	a2,-168(s0)
	li	a5,122880
	add	a5,a2,a5
	sw	a3,1120(a5)
	ld	a3,-168(s0)
	mv	a5,a4
	slli	a5,a5,5
	sub	a5,a5,a4
	slli	a5,a5,2
	add	a5,a3,a5
	mv	a3,a5
	addi	a5,s0,-152
	li	a4,124
	mv	a2,a4
	mv	a1,a5
	mv	a0,a3
	call	memcpy@plt
	j	.L21
.L18:
	lla	a0,.LC8
	call	puts@plt
.L21:
	nop
	la	a5,__stack_chk_guard
	ld	a4, -24(s0)
	ld	a5, 0(a5)
	xor	a5, a4, a5
	li	a4, 0
	beq	a5,zero,.L20
	call	__stack_chk_fail@plt
.L20:
	ld	ra,200(sp)
	.cfi_restore 1
	ld	s0,192(sp)
	.cfi_restore 8
	.cfi_def_cfa 2, 208
	addi	sp,sp,208
	.cfi_def_cfa_offset 0
	jr	ra
	.cfi_endproc
.LFE7:
	.size	createNodes, .-createNodes
	.section	.rodata
	.align	3
.LC7:
	.word	-269380349
	.word	1059860019
	.ident	"GCC: (Ubuntu 13.2.0-4ubuntu3) 13.2.0"
	.section	.note.GNU-stack,"",@progbits
