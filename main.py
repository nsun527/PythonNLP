# from typing import List, Tuple, Dict
from os import system
from jamo import h2j, j2hcj

system('cls')
input_str: str = "안녕"
umso: str = h2j(input_str)
encoded: bytes = umso.encode('UTF-8')
print(encoded)

# 소릿값이 없는 'ㅇ' 삭제
replaced = encoded.replace(b'\xE1\x84\x8B', b'')

finished: str = j2hcj(replaced.decode('UTF-8'))
for ch in finished:
    print(f'{ch}, ')