#!/usr/bin/env python3

def resolve_sys(sys):
    if sys == 0x01:
        return 'read_code'
    if sys == 0x02:
        return 'exit'
    if sys == 0x04:
        return 'write'
    if sys == 0x08:
        return 'read_memory'
    if sys == 0x10:
        return 'sleep'
    if sys == 0x20:
        return 'open'

def resolve_flag(flag):
    ret = ''
    if flag == 0x00:
        ret += '*'
    if flag & 0x01:
        ret += 'G'
    if flag & 0x02:
        ret += 'E'
    if flag & 0x04:
        ret += 'N'
    if flag & 0x08:
        ret += 'Z'
    if flag & 0x10:
        ret += 'L'
    
    return ret

def resolve_register(reg_num):
    if reg_num == 0x01:
        return "d"
    elif reg_num == 0x02:
        return "s"
    elif reg_num == 0x04:
        return "i"
    elif reg_num == 0x08:
        return "b"
    elif reg_num == 0x10:
        return "c"
    elif reg_num == 0x20:
        return "a"
    elif reg_num == 0x40:
        return "f"


f = open('vmcode.txt', 'r')
lst = f.readline().strip().split()
code = [lst[i:i + 3] for i in range(0, len(lst), 3)]

for i in range(len(code)):
    op = int(code[i][0], 16)
    arg1 = int(code[i][1], 16)
    arg2 = int(code[i][2], 16)
    print(hex(i + 1) + ":", end=' ')

    if op == 0x01:
        print('IMM', resolve_register(arg1), '=', hex(arg2))
    elif op == 0x02:
        print('ADD', resolve_register(arg1), resolve_register(arg2))
    elif op == 0x04:
        ret1 = resolve_register(arg1)
        ret2 = resolve_register(arg2)
        print('STK', ret1, ret2)
        if ret1:
            print('      ... popping', ret1)
        if ret2:
            print('      ... pushing', ret2)
    elif op == 0x08:
        print('SYS', resolve_sys(arg1), resolve_register(arg2))
    elif op == 0x10:
        print('JMP', resolve_flag(arg1), resolve_register(arg2))
    elif op == 0x20:
        print('CMP', resolve_register(arg1), resolve_register(arg2))
    elif op == 0x40:
        print('STM *' + resolve_register(arg1), '=', resolve_register(arg2))
    else:
        print('LDM', resolve_register(arg1), '= *' + resolve_register(arg2))
