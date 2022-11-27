section .rodata
msg: db "Wanna pwn me ?", 10
len: equ $ - msg

flag: db "flag.txt", 0

section .text
global _start

win:
	push rbp
	mov rbp, rsp 
	sub rsp, 40

	; fopen("flag.txt", "r")
	mov rdi, $flag
	xor rsi, rsi
	xor rdx, rdx 
	push 2
	pop rax
	syscall

	; read(fd, &stack, 40)
	xchg rax, rdi 
	mov rsi, rsp
	mov rdx, 40
	xor rax, rax 
	syscall 

	; write what's on the stack
	mov rdi, 1 
	mov rax, rdi 
	syscall	

	add rsp, 40
	pop rbp
	ret 

print:
	push rbp,
	mov rbp, rsp
	; write Wanna pwn me 
	xor rdi, rdi 
	inc rdi 
	mov rsi, $msg
	mov rdx, $len 
	xor rax, rax
	inc rax 
	syscall 
	
	pop rbp
	ret

answer:
	push rbp
	mov rbp, rsp
	sub rsp, 0x10
	
	xor rdi, rdi ; stdin 
	mov rsi, rsp ; *buf
	mov rdx, 0x100 ; count
	
	xor rax, rax 
	syscall	
	
	add rsp, 0x10
	pop rbp 
	ret

exit:
	mov rax, 60
	mov rdi, 0 
	syscall

_start:
	push rbp
	mov rbp, rsp
	call print
	call answer
	call exit 
	pop rbp 
	ret
