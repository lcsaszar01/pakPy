	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 14, 0	sdk_version 14, 4
	.globl	_createNodes                    ; -- Begin function createNodes
	.p2align	2
_createNodes:                           ; @createNodes
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #208
	.cfi_def_cfa_offset 208
	stp	x29, x30, [sp, #192]            ; 16-byte Folded Spill
	add	x29, sp, #192
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	stur	x8, [x29, #-8]
	str	x0, [sp, #48]
	str	x1, [sp, #40]
	str	x2, [sp, #32]
	strb	w3, [sp, #31]
	str	x4, [sp, #16]
	str	w5, [sp, #12]
	ldr	x8, [sp, #48]
	mov	x9, #58464
	movk	x9, #1, lsl #16
	ldr	w8, [x8, x9]
	subs	w8, w8, #1000
	cset	w8, ge
	tbnz	w8, #0, LBB0_2
	b	LBB0_1
LBB0_1:
	ldr	x1, [sp, #40]
	add	x0, sp, #60
	str	x0, [sp]                        ; 8-byte Folded Spill
	mov	x2, #100
	bl	___strcpy_chk
	ldr	x8, [sp]                        ; 8-byte Folded Reload
	add	x0, x8, #100
	ldr	x1, [sp, #32]
	mov	x2, #10
	bl	___strcpy_chk
	ldr	x1, [sp]                        ; 8-byte Folded Reload
	ldrb	w8, [sp, #31]
	strb	w8, [sp, #170]
	ldr	x8, [sp, #16]
	ldr	w8, [x8]
	str	w8, [sp, #172]
	ldr	x8, [sp, #16]
	ldr	w8, [x8, #4]
	str	w8, [sp, #176]
	ldr	w8, [sp, #12]
	str	w8, [sp, #180]
	ldr	x8, [sp, #48]
	ldr	x9, [sp, #48]
	mov	x10, #58464
	movk	x10, #1, lsl #16
	add	x11, x9, x10
	ldrsw	x9, [x11]
	mov	x10, x9
	add	w10, w10, #1
	str	w10, [x11]
	mov	x10, #124
	mul	x9, x9, x10
	add	x0, x8, x9
	mov	x2, #124
	bl	_memcpy
	b	LBB0_3
LBB0_2:
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB0_3
LBB0_3:
	ldur	x9, [x29, #-8]
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	subs	x8, x8, x9
	cset	w8, eq
	tbnz	w8, #0, LBB0_5
	b	LBB0_4
LBB0_4:
	bl	___stack_chk_fail
LBB0_5:
	ldp	x29, x30, [sp, #192]            ; 16-byte Folded Reload
	add	sp, sp, #208
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3, 0x0                          ; -- Begin function main
lCPI1_0:
	.quad	0x3f2c2e33eff19503              ; double 2.1499999999999999E-4
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-32]!           ; 16-byte Folded Spill
	.cfi_def_cfa_offset 32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w27, -24
	.cfi_offset w28, -32
	mov	w9, #3808
	movk	w9, #2, lsl #16
	adrp	x16, ___chkstk_darwin@GOTPAGE
	ldr	x16, [x16, ___chkstk_darwin@GOTPAGEOFF]
	blr	x16
	sub	sp, sp, #32, lsl #12            ; =131072
	sub	sp, sp, #3808
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	stur	x8, [x29, #-24]
	str	wzr, [sp, #124]
	str	w0, [sp, #120]
	str	x1, [sp, #112]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	adrp	x1, l_.str.3@PAGE
	add	x1, x1, l_.str.3@PAGEOFF
	bl	_fopen
	str	x0, [sp, #104]
	str	wzr, [sp, #100]
	b	LBB1_1
LBB1_1:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB1_3 Depth 2
	ldr	w8, [sp, #100]
	subs	w8, w8, #1000
	cset	w8, ge
	tbnz	w8, #0, LBB1_8
	b	LBB1_2
LBB1_2:                                 ;   in Loop: Header=BB1_1 Depth=1
	str	wzr, [sp, #96]
	b	LBB1_3
LBB1_3:                                 ;   Parent Loop BB1_1 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [sp, #96]
	subs	w8, w8, #100
	cset	w8, ge
	tbnz	w8, #0, LBB1_6
	b	LBB1_4
LBB1_4:                                 ;   in Loop: Header=BB1_3 Depth=2
	ldrsw	x8, [sp, #100]
	mov	x9, #100
	mul	x9, x8, x9
	add	x8, sp, #8, lsl #12             ; =32768
	add	x8, x8, #2104
	add	x8, x8, x9
	ldrsw	x9, [sp, #96]
	add	x0, x8, x9
	ldr	x2, [sp, #104]
	mov	w1, #1024
	bl	_fgets
	ldr	x0, [sp, #104]
	bl	_fclose
	b	LBB1_5
LBB1_5:                                 ;   in Loop: Header=BB1_3 Depth=2
	ldr	w8, [sp, #96]
	add	w8, w8, #1
	str	w8, [sp, #96]
	b	LBB1_3
LBB1_6:                                 ;   in Loop: Header=BB1_1 Depth=1
	b	LBB1_7
LBB1_7:                                 ;   in Loop: Header=BB1_1 Depth=1
	ldr	w8, [sp, #100]
	add	w8, w8, #1
	str	w8, [sp, #100]
	b	LBB1_1
LBB1_8:
	adrp	x0, l_.str.4@PAGE
	add	x0, x0, l_.str.4@PAGEOFF
	adrp	x1, l_.str.3@PAGE
	add	x1, x1, l_.str.3@PAGEOFF
	bl	_fopen
	str	x0, [sp, #88]
	ldr	x2, [sp, #88]
	add	x0, sp, #8, lsl #12             ; =32768
	add	x0, x0, #1080
	mov	w1, #1024
	bl	_fgets
	ldr	x0, [sp, #88]
	bl	_fclose
	adrp	x0, l_.str.5@PAGE
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	str	wzr, [sp, #84]
	str	wzr, [sp, #80]
	str	wzr, [sp, #76]
	str	wzr, [sp, #72]
	adrp	x8, l___const.main.alpha@PAGE
	add	x8, x8, l___const.main.alpha@PAGEOFF
	ldr	w8, [x8]
	str	w8, [sp, #68]
	str	wzr, [sp, #64]
	b	LBB1_9
LBB1_9:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB1_11 Depth 2
	ldr	w8, [sp, #64]
	ldr	w9, [sp, #84]
	subs	w8, w8, w9
	cset	w8, gt
	tbnz	w8, #0, LBB1_18
	b	LBB1_10
LBB1_10:                                ;   in Loop: Header=BB1_9 Depth=1
	ldr	w8, [sp, #72]
	add	w8, w8, #1
	str	w8, [sp, #72]
	add	x0, sp, #3, lsl #12             ; =12288
	add	x0, x0, #4052
	mov	w1, #0
	str	w1, [sp, #20]                   ; 4-byte Folded Spill
	mov	x2, #100
	str	x2, [sp, #24]                   ; 8-byte Folded Spill
	bl	_memset
	ldr	w1, [sp, #20]                   ; 4-byte Folded Reload
	ldr	x2, [sp, #24]                   ; 8-byte Folded Reload
	add	x0, sp, #3, lsl #12             ; =12288
	add	x0, x0, #3952
	bl	_memset
	ldrsw	x9, [sp, #64]
	add	x8, sp, #68
	str	x8, [sp, #32]                   ; 8-byte Folded Spill
	ldrsb	w10, [x8, x9]
	mov	x9, sp
                                        ; implicit-def: $x8
	mov	x8, x10
	str	x8, [x9]
	adrp	x0, l_.str.6@PAGE
	add	x0, x0, l_.str.6@PAGEOFF
	bl	_printf
	ldr	x8, [sp, #32]                   ; 8-byte Folded Reload
	ldrsw	x9, [sp, #64]
	add	x1, x8, x9
	add	x0, sp, #4, lsl #12             ; =16384
	add	x0, x0, #56
	str	x0, [sp, #40]                   ; 8-byte Folded Spill
	mov	x2, #1024
	bl	___strcat_chk
	ldr	x8, [sp, #40]                   ; 8-byte Folded Reload
	mov	x9, sp
	str	x8, [x9]
	adrp	x0, l_.str.7@PAGE
	add	x0, x0, l_.str.7@PAGEOFF
	bl	_printf
	str	wzr, [sp, #60]
	b	LBB1_11
LBB1_11:                                ;   Parent Loop BB1_9 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [sp, #60]
	subs	w8, w8, #4
	cset	w8, ge
	tbnz	w8, #0, LBB1_14
	b	LBB1_12
LBB1_12:                                ;   in Loop: Header=BB1_11 Depth=2
	mov	x9, sp
	adrp	x8, l_.str.8@PAGE
	add	x8, x8, l_.str.8@PAGEOFF
	str	x8, [x9]
	add	x0, sp, #3, lsl #12             ; =12288
	add	x0, x0, #3852
	bl	_printf
	add	x4, sp, #3, lsl #12             ; =12288
	add	x4, x4, #3840
	str	xzr, [sp, #16128]
	str	wzr, [sp, #56]
	ldrsw	x9, [sp, #60]
	add	x8, sp, #68
	ldrsb	w3, [x8, x9]
	ldr	w5, [sp, #56]
	mov	x0, #0
	add	x1, sp, #3, lsl #12             ; =12288
	add	x1, x1, #4052
	adrp	x2, l_.str.9@PAGE
	add	x2, x2, l_.str.9@PAGEOFF
	bl	_createNodes
	b	LBB1_13
LBB1_13:                                ;   in Loop: Header=BB1_11 Depth=2
	ldr	w8, [sp, #60]
	add	w8, w8, #1
	str	w8, [sp, #60]
	b	LBB1_11
LBB1_14:                                ;   in Loop: Header=BB1_9 Depth=1
	ldr	w8, [sp, #80]
	subs	w8, w8, #0
	cset	w8, le
	tbnz	w8, #0, LBB1_16
	b	LBB1_15
LBB1_15:                                ;   in Loop: Header=BB1_9 Depth=1
	ldr	s1, [sp, #80]
                                        ; implicit-def: $d0
	fmov	s0, s1
	sshll.2d	v0, v0, #0
                                        ; kill: def $d0 killed $d0 killed $q0
	scvtf	d0, d0
	adrp	x8, lCPI1_0@PAGE
	ldr	d1, [x8, lCPI1_0@PAGEOFF]
	fdiv	d0, d0, d1
	str	d0, [sp, #48]
	ldr	s1, [sp, #80]
                                        ; implicit-def: $d0
	fmov	s0, s1
	sshll.2d	v0, v0, #0
                                        ; kill: def $d0 killed $d0 killed $q0
	scvtf	d0, d0
	ldrsw	x10, [sp, #72]
	add	x8, sp, #4, lsl #12             ; =16384
	add	x8, x8, #1080
	mov	x9, x8
	add	x9, x9, x10, lsl #4
	str	d0, [x9, #8]
	ldr	d0, [sp, #48]
	ldrsw	x9, [sp, #72]
	lsl	x9, x9, #4
	str	d0, [x8, x9]
	b	LBB1_16
LBB1_16:                                ;   in Loop: Header=BB1_9 Depth=1
	b	LBB1_17
LBB1_17:                                ;   in Loop: Header=BB1_9 Depth=1
	ldr	w8, [sp, #64]
	add	w8, w8, #1
	str	w8, [sp, #64]
	b	LBB1_9
LBB1_18:
	ldur	x9, [x29, #-24]
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	subs	x8, x8, x9
	cset	w8, eq
	tbnz	w8, #0, LBB1_20
	b	LBB1_19
LBB1_19:
	bl	___stack_chk_fail
LBB1_20:
	mov	w0, #0
	add	sp, sp, #32, lsl #12            ; =131072
	add	sp, sp, #3808
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #32             ; 16-byte Folded Reload
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"Maximum number of nodes reached.\n"

l_.str.1:                               ; @.str.1
	.asciz	"setting up graph\n"

l_.str.2:                               ; @.str.2
	.asciz	"kmer_lst.txt"

l_.str.3:                               ; @.str.3
	.asciz	"r"

l_.str.4:                               ; @.str.4
	.asciz	"kmer_1.txt"

l_.str.5:                               ; @.str.5
	.asciz	"Done importing kmer files.\n"

	.section	__TEXT,__literal4,4byte_literals
l___const.main.alpha:                   ; @__const.main.alpha
	.ascii	"ATCG"

	.section	__TEXT,__cstring,cstring_literals
l_.str.6:                               ; @.str.6
	.asciz	"%c\n"

l_.str.7:                               ; @.str.7
	.asciz	"%s\n"

l_.str.8:                               ; @.str.8
	.asciz	"%s"

l_.str.9:                               ; @.str.9
	.asciz	"Suffix"

.subsections_via_symbols
