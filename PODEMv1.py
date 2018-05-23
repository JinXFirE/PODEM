import os
import sys
import re

def and_gate(inp1, inp2):
    if (inp1 == 0 or inp1 == 1) and (inp2 == 0 or inp2 == 1):
        inp3 = inp1 * inp2
    if inp1 == 0:
        if (inp2 == 'D') or (inp2 == 'Dbar') or (inp2 == 'x'):
            inp3 = 0
    if inp1 == 1:
        if (inp2 == 'D') or (inp2 == 'Dbar') or (inp2 == 'x'):
            inp3 = inp2
    if inp1 == 'D':
        if inp2 == 0:
            inp3 = 0
        if inp2 == 1:
            inp3 = 'D'
        if inp2 == 'D':
            inp3 = 'D'
        if inp2 == 'Dbar':
            inp3 = 0
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'Dbar':
        if inp2 == 0:
            inp3 = 0
        if inp2 == 1:
            inp3 = 'Dbar'
        if inp2 == 'D':
            inp3 = 0
        if inp2 == 'Dbar':
            inp3 = 'Dbar'
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'x':
        if inp2 == 0:
            inp3 = 0
        if inp2 == 1:
            inp3 = 'x'
        if inp2 == 'D':
            inp3 = 'x'
        if inp2 == 'Dbar':
            inp3 = 'x'
        if inp2 == 'x':
            inp3 = 'x'
    return inp3

def not_gate(inp1):
    if inp1 == 1:
        inp2 = 0
    if inp1 == 0:
        inp2 = 1
    if inp1 == 'D':
        inp2 = 'Dbar'
    if inp1 == 'Dbar':
        inp2 = 'D'
    if inp1 == 'x':
        inp2 = inp1
    return inp2


def nor_gate(inp1, inp2):
    if (inp1 == 0 or inp1 == 1) and (inp2 == 0 or inp2 == 1):
        if inp1 == 1:
            inp1 = True
        else:
            inp1 = False
        if inp2 == 1:
            inp2 = True
        else:
            inp2 = False

        inp3 = (not inp1) and (not inp2)

        if inp3 == True:
            inp3 = 1
        else:
            inp3 = 0
    if inp1 == 0:
        if inp2 == 'D':
            inp3 = 'Dbar'
        if inp2 == 'Dbar':
            inp3 = 'D'
        if inp2 == 'x':
            inp3 = inp2
    if inp1 == 1:
        if (inp2 == 'D') or (inp2 == 'Dbar') or (inp2 == 'x'):
            inp3 = 0
    if inp1 == 'D':
        if inp2 == 0:
            inp3 = 'Dbar'
        if inp2 == 1:
            inp3 = 0
        if inp2 == 'D':
            inp3 = 'Dbar'
        if inp2 == 'Dbar':
            inp3 = 0
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'Dbar':
        if inp2 == 0:
            inp3 = 'D'
        if inp2 == 1:
            inp3 = 0
        if inp2 == 'D':
            inp3 = 0
        if inp2 == 'Dbar':
            inp3 = 'D'
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'x':
        if inp2 == 0:
            inp3 = 'x'
        if inp2 == 1:
            inp3 = 0
        if inp2 == 'D':
            inp3 = 'x'
        if inp2 == 'Dbar':
            inp3 = 'x'
        if inp2 == 'x':
            inp3 = 'x'
    return inp3


def nand_gate(inp1, inp2):
    if (inp1 == 0 or inp1 == 1) and (inp2 == 0 or inp2 == 1):
        if inp1 == 1:
            inp1 = True
        else:
            inp1 = False
        if inp2 == 1:
            inp2 = True
        else:
            inp2 = False

        inp3 = (not inp1) or (not inp2)

        if inp3 == True:
            inp3 = 1
        else:
            inp3 = 0
    if inp1 == 1:
        if inp2 == 'D':
            inp3 = 'Dbar'
        if inp2 == 'Dbar':
            inp3 = 'D'
        if inp2 == 'x':
            inp3 = inp2
    if inp1 == 0:
        if (inp2 == 'D') or (inp2 == 'Dbar') or (inp2 == 'x'):
            inp3 = 1

    if inp1 == 'D':
        if inp2 == 0:
            inp3 = 1
        if inp2 == 1:
            inp3 = 'Dbar'
        if inp2 == 'D':
            inp3 = 'Dbar'
        if inp2 == 'Dbar':
            inp3 = 1
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'Dbar':
        if inp2 == 0:
            inp3 = 1
        if inp2 == 1:
            inp3 = 'D'
        if inp2 == 'D':
            inp3 = 1
        if inp2 == 'Dbar':
            inp3 = 'D'
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'x':
        if inp2 == 0:
            inp3 = 1
        if inp2 == 1:
            inp3 = 'x'
        if inp2 == 'D':
            inp3 = 'x'
        if inp2 == 'Dbar':
            inp3 = 'x'
        if inp2 == 'x':
            inp3 = 'x'
    return inp3


def or_gate(inp1, inp2):
    if (inp1 == 0 or inp1 == 1) and (inp2 == 0 or inp2 == 1):
        if inp1 == 1:
            inp1 = True
        else:
            inp1 = False
        if inp2 == 1:
            inp2 = True
        else:
            inp2 = False

        inp3 = inp1 or inp2

        if inp3 == True:
            inp3 = 1
        else:
            inp3 = 0
    if inp1 == 1:
        if (inp2 == 'D') or (inp2 == 'Dbar') or (inp2 == 'x'):
            inp3 = 1
    if inp1 == 0:
        if (inp2 == 'D') or (inp2 == 'Dbar') or (inp2 == 'x'):
            inp3 = inp2
    if inp1 == 'D':
        if inp2 == 0:
            inp3 = 'D'
        if inp2 == 1:
            inp3 = 1
        if inp2 == 'D':
            inp3 = 'D'
        if inp2 == 'Dbar':
            inp3 = 1
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'Dbar':
        if inp2 == 0:
            inp3 = 'Dbar'
        if inp2 == 1:
            inp3 = 1
        if inp2 == 'D':
            inp3 = 1
        if inp2 == 'Dbar':
            inp3 = 'Dbar'
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'x':
        if inp2 == 0:
            inp3 = 'x'
        if inp2 == 1:
            inp3 = 1
        if inp2 == 'D':
            inp3 = 'x'
        if inp2 == 'Dbar':
            inp3 = 'x'
        if inp2 == 'x':
            inp3 = 'x'
    return inp3

def xor_gate(inp1, inp2):
    if (inp1 == 0 or inp1 == 1) and (inp2 == 0 or inp2 == 1):
        if inp1 == 1:
            inp1 = True
        else:
            inp1 = False
        if inp2 == 1:
            inp2 = True
        else:
            inp2 = False

        inp3 =((not inp1) and inp2) or (inp1 and (not inp2))

        if inp3 == True:
            inp3 = 1
        else:
            inp3 = 0
    if inp1 == 'D':
        if inp2 == 0:
            inp3 = 'D'
        if inp2 == 1:
            inp3 = 'Dbar'
        if inp2 == 'D':
            inp3 = 0
        if inp2 == 'Dbar':
            inp3 = 1
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'Dbar':
        if inp2 == 0:
            inp3 = 'Dbar'
        if inp2 == 1:
            inp3 = 'D'
        if inp2 == 'D':
            inp3 = 1
        if inp2 == 'Dbar':
            inp3 = 0
        if inp2 == 'x':
            inp3 = 'x'
    if inp1 == 'x':
        if inp2 == 0:
            inp3 = 'x'
        if inp2 == 1:
            inp3 = 'x'
        if inp2 == 'D':
            inp3 = 'x'
        if inp2 == 'Dbar':
            inp3 = 'x'
        if inp2 == 'x':
            inp3 = 'x'
    return inp3

def eval_logic():  # 5 valued Imply Function
    loop = 0
    if input_list_ip1.__contains__(target_pin):
        if Tot_pins[target_pin - 1] == 0 and val_stuck_at == 1:
            Tot_pins[target_pin - 1] = 'Dbar'
        if Tot_pins[target_pin - 1] == 1 and val_stuck_at == 0:
            Tot_pins[target_pin - 1] = 'D'

    for loop1 in range(20):
        loop += 1

        var_and_count = len(and_list)
        var_or_count = len(or_list)
        var_xor_count = len(xor_list)
        var_nor_count = len(nor_list)
        var_inv_count = len(inv_list)
        var_nand_count = len(nand_list)
        var_buf_count = len(buf_list)

        i1 = 0
        while not var_and_count == 0:

            and_opr = and_gate(Tot_pins[and_list[i1][0] - 1], Tot_pins[and_list[i1][1] - 1])
            Tot_pins[and_list[i1][2] - 1] = and_opr
            # print(and_list[i1][0]-1)
            # print(and_list[i1][1]-1)
            if and_list[i1][2] == target_pin:
                if Tot_pins[and_list[i1][2]-1] == 0 and val_stuck_at == 1:
                    Tot_pins[and_list[i1][2]-1] = 'Dbar'
                if Tot_pins[and_list[i1][2]-1] == 1 and val_stuck_at == 0:
                    Tot_pins[and_list[i1][2]-1] = 'D'
            i1 += 1
            var_and_count -= 1

        i2 = 0
        while not var_or_count == 0:
            or_opr = or_gate(Tot_pins[or_list[i2][0] - 1], Tot_pins[or_list[i2][1] - 1])
            Tot_pins[or_list[i2][2] - 1] = or_opr
            if or_list[i2][2] == target_pin:

                if Tot_pins[or_list[i2][2]-1] == 0 and val_stuck_at == 1:
                    Tot_pins[or_list[i2][2]-1] = 'Dbar'
                if Tot_pins[or_list[i2][2]-1] == 1 and val_stuck_at == 0:
                    Tot_pins[or_list[i2][2]-1] = 'D'
            i2 += 1
            var_or_count -= 1

        i3 = 0
        while not var_nor_count == 0:
            nor_opr = nor_gate(Tot_pins[nor_list[i3][0] - 1], Tot_pins[nor_list[i3][1] - 1])
            Tot_pins[nor_list[i3][2] - 1] = nor_opr
            if nor_list[i3][2] == target_pin:
                if Tot_pins[nor_list[i3][2]-1] == 0 and val_stuck_at == 1:
                    Tot_pins[nor_list[i3][2]-1] = 'Dbar'
                if Tot_pins[nor_list[i3][2]-1] == 1 and val_stuck_at == 0:
                    Tot_pins[nor_list[i3][2]-1] = 'D'
            i3 += 1
            var_nor_count -= 1

        i4 = 0
        while not var_xor_count == 0:
            xor_opr = xor_gate(Tot_pins[xor_list[i4][0] - 1], Tot_pins[xor_list[i4][1] - 1])
            Tot_pins[xor_list[i4][2] - 1] = xor_opr
            if xor_list[i4][2] == target_pin:
                if Tot_pins[xor_list[i4][2]-1] == 0 and val_stuck_at == 1:
                    Tot_pins[xor_list[i4][2]-1] = 'Dbar'
                if Tot_pins[xor_list[i4][2]-1] == 1 and val_stuck_at == 0:
                    Tot_pins[xor_list[i4][2]-1] = 'D'
            i4 += 1
            var_xor_count -= 1

        i5 = 0
        while not var_nand_count == 0:

            nand_opr = nand_gate(Tot_pins[nand_list[i5][0] - 1], Tot_pins[nand_list[i5][1] - 1])
            Tot_pins[nand_list[i5][2] - 1] = nand_opr
            if nand_list[i5][2] == target_pin:
                if Tot_pins[nand_list[i5][2]-1] == 0 and val_stuck_at == 1:
                    Tot_pins[nand_list[i5][2]-1] = 'Dbar'
                if Tot_pins[nand_list[i5][2]-1] == 1 and val_stuck_at == 0:
                    Tot_pins[nand_list[i5][2]-1] = 'D'
            i5 += 1
            var_nand_count -= 1

        i6 = 0
        while not var_inv_count == 0:
            inv_opr = not_gate(Tot_pins[inv_list[i6][0] - 1])
            Tot_pins[inv_list[i6][1] - 1] = inv_opr
            if inv_list[i6][1] == target_pin:
                if Tot_pins[inv_list[i6][1]-1] == 0 and val_stuck_at == 1:
                    Tot_pins[inv_list[i6][1]-1] = 'Dbar'
                if Tot_pins[inv_list[i6][1]-1] == 1 and val_stuck_at == 0:
                    Tot_pins[inv_list[i6][1]-1] = 'D'
            i6 += 1
            var_inv_count -= 1

        i7 = 0
        while not var_buf_count == 0:
            buf_opr = Tot_pins[buf_list[i7][0] - 1]
            Tot_pins[buf_list[i7][1] - 1] = buf_opr
            if buf_list[i7][1] == target_pin:
                if Tot_pins[buf_list[i7][1]-1] == 0 and val_stuck_at == 1:
                    Tot_pins[buf_list[i7][1]-1] = 'Dbar'
                if Tot_pins[buf_list[i7][1]-1] == 1 and val_stuck_at == 0:
                    Tot_pins[buf_list[i7][1]-1] = 'D'
            i7 += 1
            var_buf_count -= 1
    return Tot_pins

def input_all():
    max_inputs = len(input_list_ip1)
    var_1 = 0
    while max_inputs != 0:  # till all the inputs are inputted
        Tot_pins[input_list_ip1[var_1] - 1] = total_inputs[var_1]  # Put inputs in Tot pins
        #print(total_inputs)
        var_1 += 1
        max_inputs -= 1
    return Tot_pins

def create_input_list():
    f.seek(0)
    inp_count = 0
    input_list_ip = []
    for line in f:

        if line.startswith('INPUT'):
            inpnumber1 = line.partition('  ')[2]  # separate char from num
            strnum2 = inpnumber1.rstrip('\n')  # remove \n
            input_list_ip.append(strnum2.split(" "))
            input_list_ip[inp_count] = list(map(int, input_list_ip[inp_count]))
            input_list_ip1 = input_list_ip[inp_count]
            inp_count = + 1
    input_list_ip1.pop()
    return input_list_ip1

def create_output_list():
    f.seek(0)
    out_count = 0
    output_list_ip = []
    output_list = []
    for line in f:
        if line.startswith('OUTPUT'):
            outnumber1 = line.partition('  ')[2]  # separate char from num
            outnum2 = outnumber1.rstrip('\n')  # remove \n
            output_list_ip.append(outnum2.split(" "))
            output_list_ip[out_count] = list(map(int, output_list_ip[out_count]))
            output_list_ip1 = output_list_ip[out_count]
            out_count = + 1
    output_list_ip1.pop()
    return output_list_ip1

def output_write(all_output):
    max_outputs = len(output_list_ip1)
    all_out_1 = []
    for var_12 in range(0, max_outputs):  # till all the inputs are inputted
        # print(Tot_pins[output_list_ip1[var_12] - 1])
        all_out_1.append((Tot_pins[output_list_ip1[var_12] - 1]))
    all_output.append(all_out_1)
    return all_output

def input_write(all_input):
    max_inputs = len(input_list_ip1)
    all_in_1 = []
    for var_12 in range(0, max_inputs):  # till all the inputs are inputted
        if Tot_pins[input_list_ip1[var_12] - 1] == 'D':
            Tot_pins[input_list_ip1[var_12] - 1] = 1
        if Tot_pins[input_list_ip1[var_12] - 1] == 'Dbar':
            Tot_pins[input_list_ip1[var_12] - 1] = 0
        all_in_1.append((Tot_pins[input_list_ip1[var_12] - 1]))
    all_input.append(all_in_1)
    return all_input

def create_inv_list():
    f.seek(0)
    inv_count = 0
    for line in f:
        if line.startswith('INV'):
            invnumber = line.partition(' ')[2]  # separate char from num
            strnum1 = invnumber.rstrip('\n')  # remove \n
            inv_list.append(strnum1.split(" "))
            strnum1 = list(strnum1.split(" "))
            inv_out.append(strnum1[1])
            inv_list[inv_count] = list(map(int, inv_list[inv_count]))
            inv_count += 1
    inv_all.append(inv_list)
    inv_all.append(inv_out)
    return inv_all

def create_and_list():
    f.seek(0)
    and_count = 0
    for line in f:
        if line.startswith('AND'):
            andnumber = line.partition(' ')[2]  # separate char from num
            andnum1 = andnumber.rstrip('\n')  # remove \n
            and_list.append(andnum1.split(" "))
            andnum1 = list(andnum1.split(" "))
            and_out.append(andnum1[2])
            and_list[and_count] = list(map(int, and_list[and_count]))
            and_count += 1
    and_all.append(and_list)
    and_all.append(and_out)
    return and_all

def create_nand_list():
    f.seek(0)
    nand_count = 0
    for line in f:
        if line.startswith('NAND'):
            nandnumber = line.partition(' ')[2]  # separate char from num
            nandnum1 = nandnumber.rstrip('\n')  # remove \n
            nand_list.append(nandnum1.split(" "))
            nandnum1 = list(nandnum1.split(" "))
            nand_out.append(nandnum1[2])
            nand_list[nand_count] = list(map(int, nand_list[nand_count]))
            nand_count += 1
            # print(nand_count)
    nand_all.append(nand_list)
    nand_all.append(nand_out)
    return nand_all

def create_or_list():
    f.seek(0)
    or_count = 0
    for line in f:
        if line.startswith('OR'):
            ornumber = line.partition(' ')[2]  # separate char from num
            ornum1 = ornumber.rstrip('\n')  # remove \n
            or_list.append(ornum1.split(" "))
            ornum1 = list(ornum1.split(" "))
            or_out.append(ornum1[2])
            or_list[or_count] = list(map(int, or_list[or_count]))
            or_count += 1
            # print(or_count)
    or_all.append(or_list)
    or_all.append(or_out)
    return or_all

def create_nor_list():
    f.seek(0)
    nor_count = 0
    for line in f:
        if line.startswith('NOR'):
            nornumber = line.partition(' ')[2]  # separate char from num
            nornum1 = nornumber.rstrip('\n')  # remove \n
            nor_list.append(nornum1.split(" "))
            nornum1 = list(nornum1.split(" "))
            nor_out.append(nornum1[2])
            nor_list[nor_count] = list(map(int, nor_list[nor_count]))
            nor_count += 1
            # print(nor_count)
    nor_all.append(nor_list)
    nor_all.append(nor_out)
    return nor_all

def create_xor_list():
    f.seek(0)
    xor_count = 0
    for line in f:
        if line.startswith('XOR'):
            xornumber = line.partition(' ')[2]  # separate char from num
            xornum1 = xornumber.rstrip('\n')  # remove \n
            xor_list.append(xornum1.split(" "))
            xornum1 = list(xornum1.split(" "))
            xor_out.append(xornum1[2])
            xor_list[xor_count] = list(map(int, xor_list[xor_count]))
            xor_count += 1
            # print(xor_count)
    xor_all.append(xor_list)
    xor_all.append(xor_out)
    return xor_all

def create_buf_list():
    f.seek(0)
    buf_count = 0
    for line in f:
        if line.startswith('BUF'):
            bufnumber = line.partition(' ')[2]  # separate char from num
            bufnum1 = bufnumber.rstrip('\n')  # remove \n
            buf_list.append(bufnum1.split(" "))
            bufnum1 = list(bufnum1.split(" "))
            buf_out.append(bufnum1[1])
            buf_list[buf_count] = list(map(int, buf_list[buf_count]))
            buf_count += 1
    buf_all.append(buf_list)
    buf_all.append(buf_out)
    return buf_all

def find_gate(pin):  # Find which gate has the target pin as the output
    pin = str(pin)
    if and_out.__contains__(pin):
        pin_and = []
        gate = []
        inv_par = 0
        ctr_val = 0
        pin_and = and_list[and_out.index(pin)]
        gate.append(pin_and)
        gate.append('and')
        gate.append(inv_par)
        gate.append(ctr_val)
        return gate
    if or_out.__contains__(pin):
        pin_or = []
        gate = []
        inv_par = 0
        ctr_val = 1
        pin_or = or_list[or_out.index(pin)]
        gate.append(pin_or)
        gate.append('or')
        gate.append(inv_par)
        gate.append(ctr_val)
        return gate
    if nand_out.__contains__(pin):
        pin_nand = []
        gate = []
        inv_par = 1
        ctr_val = 0
        pin_nand = nand_list[nand_out.index(pin)]
        gate.append(pin_nand)
        gate.append('nand')
        gate.append(inv_par)
        gate.append(ctr_val)
        return gate
    if nor_out.__contains__(pin):
        pin_nor = []
        gate = []
        inv_par = 1
        ctr_val = 1
        pin_nor = nor_list[nor_out.index(pin)]
        gate.append(pin_nor)
        gate.append('nor')
        gate.append(inv_par)
        gate.append(ctr_val)
        return gate
    if xor_out.__contains__(pin):
        pin_xor = []
        gate = []
        inv_par = 0
        ctr_val = 0
        pin_xor = xor_list[xor_out.index(pin)]
        gate.append(pin_xor)
        gate.append('xor')
        gate.append(inv_par)
        gate.append(ctr_val)
        return gate
    if inv_out.__contains__(pin):
        pin_inv = []
        gate = []
        inv_par = 1
        pin_inv = inv_list[inv_out.index(pin)]
        gate.append(pin_inv)
        gate.append('inv')
        gate.append(inv_par)
        return gate
    if buf_out.__contains__(pin):
        pin_buf = []
        gate = []
        inv_par = 0
        pin_buf = buf_list[buf_out.index(pin)]
        gate.append(pin_buf)
        gate.append('buf')
        gate.append(inv_par)
        return gate
    else:
        gate = [[int(pin)],'PI',0]
        return gate

def find_inv_par(): # Find Inversion parity of the path
    if gate_inv.count(1) % 2 == 0:
        inv_par = 0
    else:
        inv_par = 1
    return inv_par

def mod_backtrace(pin_no):

    if pin_no == 'no d list':
        return 'no x path'

    gate = []
    gate = find_gate(pin_no)
    gate_list = []
    gate_list = gate[0]
    gate_inv.append(gate[2])
    global bt_loop
    bt_loop += 1
    if bt_loop >= size:
        return 'no x path'

    if gate[1] == 'and' or gate[1] == 'nand' or gate[1] == 'or' or gate[1] == 'nor' or gate[1] == 'xor':
        if PI_BL.__contains__(gate_list[0]) and PI_BL.__contains__(gate_list[1]):
            if len(x_list) == 1:
                return 'no x path'
            if len(x_list) == 0:
                return 'no x path'
            x_list.pop()
            if len(x_list[len(x_list)-1]) == 2 :
                gate_list[0] = x_list[len(x_list)-1][1]
                return mod_backtrace(gate_list[0])
            else:
                while not len(x_list[len(x_list)-1]) == 2:
                    if len(x_list) == 1:
                        break
                    x_list.pop()
                if len(x_list) == 1:
                    return 'no x path'
                gate_list[0] = x_list[len(x_list) - 1][1]
                return mod_backtrace(gate_list[0])
        if PI_BL.__contains__(gate_list[0]):
            gate_list[0] = gate_list[1]
            con = [gate_list[0]]
            x_list.append(con)
            return mod_backtrace(gate_list[0])

        if Tot_pins[gate_list[0]-1] == 'x'and not input_list_ip1.__contains__(gate_list[0]) and not Tot_pins[gate_list[0]-1] == Tot_pins[gate_list[1]-1]: #When only inp1 is x
            con = [gate_list[0]]
            x_list.append(con)

        if not Tot_pins[gate_list[0]-1] == 'x' and Tot_pins[gate_list[1]-1] == 'x'and not input_list_ip1.__contains__(gate_list[1]) and not Tot_pins[gate_list[0]-1] == Tot_pins[gate_list[1]-1]: #When only inp2 is x
            gate_list[0] = gate_list[1]
            con = [gate_list[0]]
            x_list.append(con)
            return mod_backtrace(gate_list[0])

        if Tot_pins[gate_list[1]-1] == 'x' and Tot_pins[gate_list[0]-1] == Tot_pins[gate_list[1]-1] and not gate_list[0] == gate_list[1]:#When both inps are x
            con = [str(gate_list[0])]
            con.append(str(gate_list[1]))
            con = list(map(int, con))
            x_list.append(con)

        if Tot_pins[gate_list[1] - 1] == 'x' and Tot_pins[gate_list[0] - 1] == Tot_pins[gate_list[1] - 1] and gate_list[0] == gate_list[1]:
            con = [gate_list[0]]
            x_list.append(con)

        if input_list_ip1.__contains__(gate_list[0]) and Tot_pins[gate_list[0]-1] == 'x' and (not PI_BL.__contains__(gate_list[0])):
            PI_BL.append(gate_list[0])
            return gate_list[0]

        if Tot_pins[gate_list[0]-1] == 'x':
            return mod_backtrace(gate_list[0])

    if gate[1] == 'PI' and (not PI_BL.__contains__(gate_list[0])):
        PI_BL.append(gate_list[0])
        return gate_list[0]
    else:
        if PI_BL.__contains__(gate_list[0]):
            if len(x_list) == 1:
                return 'no x path'
            if len(x_list) == 0:
                return 'no x path'
            x_list.pop()
            if len(x_list[len(x_list)-1]) == 2 :
                gate_list[0] = x_list[len(x_list)-1][1]
                return mod_backtrace(gate_list[0])
            else:
                while not len(x_list[len(x_list)-1]) == 2:
                    if len(x_list) == 1:
                        break
                    x_list.pop()
                if len(x_list) == 1:
                    return 'no x path'
                gate_list[0] = x_list[len(x_list) - 1][1]
                return mod_backtrace(gate_list[0])

        if Tot_pins[gate_list[0]-1] == 'x'and not input_list_ip1.__contains__(gate_list[0]):
            con = [gate_list[0]]
            x_list.append(con)

        if (input_list_ip1.__contains__(gate_list[0]) and Tot_pins[gate_list[0]-1] == 'x') and (not PI_BL.__contains__(gate_list[0])):
            PI_BL.append(gate_list[0])
            return gate_list[0]
        if Tot_pins[gate_list[0]-1] == 'x':
            return mod_backtrace(gate_list[0])
    return 'no x path'

def pin_assgn(pin_val):

    inv_par = find_inv_par()
    pin_val1 = xor_gate(pin_val,inv_par)
    return pin_val1

def backtrace(target_pin,pin_val):
    global bt_loop
    bt_loop = 0
    pin_no = mod_backtrace(target_pin)

    if pin_no == 'no x path':
        return 'no pin value','no pin value'
    pin_val1 = pin_assgn(pin_val)

    return pin_no,pin_val1

def d_front(pin_no,d_list):

    gate = []
    gate = find_gate(pin_no+1)
    gate_list = []
    gate_list = gate[0]

    if gate[1] == 'and' or gate[1] == 'nand' or gate[1] == 'or' or gate[1] == 'nor' or gate[1] == 'xor':
        if Tot_pins[gate_list[2]-1] == 'x' and (Tot_pins[gate_list[0]-1] =='D' or Tot_pins[gate_list[0]-1] == 'Dbar'):

            d_list.append(pin_no+1)

        if Tot_pins[gate_list[2]-1] == 'x' and (Tot_pins[gate_list[1]-1] =='D' or Tot_pins[gate_list[1]-1] == 'Dbar'):

            d_list.append(pin_no+1)

        return d_list
    return d_list

def create_D_front(d_list):
    d_list1 = []
    for df in range(len(Tot_pins)):
        d_list1 = d_front(df,d_list1)
    return d_list1

def objective(target_pin,stuck_at):

    if Tot_pins[target_pin-1] == 'x':
        if stuck_at==0:
            return target_pin,1
        if stuck_at==1:
            return target_pin,0
    if not len(d_list) == 0:

        gate_pin = d_list[len(d_list)-1]
        d_list.pop()
        gate = find_gate(gate_pin)
        gate_list = []
        gate_list = gate[0]

        if Tot_pins[gate_list[0]-1] == 'x':

            ctr_val = gate[3]
            ctr_val = not_gate(ctr_val)
            return gate_list[0],ctr_val
        if Tot_pins[gate_list[1]-1] == 'x':
            ctr_val = gate[3]
            ctr_val = not_gate(ctr_val)
            return gate_list[1],ctr_val
    return 'no d list',1

def PODEM(target_pin1,stuck_at1):

    global d_list
    d_list = []
    d_list = create_D_front(d_list)
    Tot_pins = eval_logic()

    for out_len in range(len(output_list_ip1)):
        if Tot_pins[output_list_ip1[out_len]-1] == 'D' or Tot_pins[output_list_ip1[out_len]-1] == 'Dbar':
            return 'SUCCESS'

    req_pin,pin_val1 = objective(target_pin1,stuck_at1)
    global x_list
    x_list = []
    pin_no,pin_val = backtrace(req_pin,pin_val1)
    if pin_no == 'no pin value': #no test possible
        return 'FAILURE'

    Tot_pins[pin_no-1] = pin_val
    Tot_pins = eval_logic()
    d_list = []
    d_list = create_D_front(d_list)

    if PODEM(target_pin1,stuck_at1) == 'SUCCESS':
        return 'SUCCESS'
    Tot_pins[pin_no - 1] = not_gate(pin_val)
    Tot_pins = eval_logic()
    d_list = []
    d_list = create_D_front(d_list)

    if PODEM(target_pin1,stuck_at1) == 'SUCCESS':
        return 'SUCCESS'
    Tot_pins[pin_no - 1] = 'x'
    Tot_pins = eval_logic()
    d_list = []
    d_list = create_D_front(d_list)
    return 'FAILURE'

def create_fault_list(fault_list):
    fault_list_ip = []
    with open(sys.argv[4], 'r') as f:
        for line in f:
            fault_list_ip.append(re.findall(r'\d{1,3}', line))

        for i in range(len(fault_list_ip)):
            fault_list.append(fault_list_ip[i])

    return  fault_list

fault_list = []
fault_list = create_fault_list(fault_list)
FF_Tot_pins = []
FF_all_output = []
FF_all_inp = []
PODEM_res = []
for faults in range(len(fault_list)):
    with open(sys.argv[1], 'r') as f:
        all_output = []
        all_input = []
        pin_list = []
        global target_pin,val_stuck_at,size
        target_pin = int(fault_list[faults][0])  # stuck at 1
        val_stuck_at = int(fault_list[faults][1])
        size = 0
        for line in f:
            size = size + 1
            Pins = re.findall(r'\d{1,3}', line)  # finds numbers in each line
            Pins = list(map(int, Pins))  # Converts strings to int
            if Pins:
                Pins = max(Pins)  # max in a line
                pin_list.append(Pins)  # make a list

        Num_pins = max(pin_list)  # max pin number
        Tot_pins = ['x'] * Num_pins

        input_list_ip1 = []
        input_list_ip1 = create_input_list()

        output_list_ip1 = []
        output_list_ip1 = create_output_list()

        inv_list = []
        inv_out = []
        inv_all = []
        inv_all = create_inv_list()
        inv_list = inv_all[0]
        inv_out = inv_all[1]

        and_list = []
        and_out = []
        and_all = []
        and_all = create_and_list()
        and_list = and_all[0]
        and_out = and_all[1]

        nand_list = []
        nand_out = []
        nand_all = []
        nand_all = create_nand_list()
        nand_list = nand_all[0]
        nand_out = nand_all[1]

        or_list = []
        or_out = []
        or_all = []
        or_all = create_or_list()
        or_list = or_all[0]
        or_out = or_all[1]

        nor_list = []
        nor_out = []
        nor_all = []
        nor_all = create_nor_list()
        nor_list = nor_all[0]
        nor_out = nor_all[1]

        xor_list = []
        xor_out = []
        xor_all = []
        xor_all = create_xor_list()
        xor_list = xor_all[0]
        xor_out = xor_all[1]

        buf_list = []
        buf_out = []
        buf_all = []
        buf_all = create_buf_list()
        buf_list = buf_all[0]
        buf_out = buf_all[1]

    PI_BL = []
    gate_inv = []
    bt_loop = 0

    Tot_pins = eval_logic()

    # PODEM
    tes_result = PODEM(target_pin,val_stuck_at)

    PODEM_res.append(tes_result)
    all_output = output_write(all_output)
    # To retain the results after multiple loops
    FF_all_output.append(all_output[0])
    FF_Tot_pins.append(Tot_pins)
    all_input = input_write(all_input)
    FF_all_inp.append(all_input[0])

print('PODEM RESULT:',PODEM_res)

max_outputs = len(output_list_ip1)
with open(sys.argv[2], 'w') as f: #Values at the output of the circuit

    for var_inp_1 in range(len(FF_all_output)):
        for var_12 in range(0, max_outputs):  # till all the outputs are inputted
            f.write(str(FF_all_output[var_inp_1][var_12]))
        f.write('\n')

all_input = input_write(all_input)
max_inputs = len(input_list_ip1)
with open(sys.argv[3], 'w') as f: # Used to create Input vectors file from PODEM results

    for var_inp_1 in range(len(FF_all_inp)):
        for var_12 in range(0, max_inputs):  # till all the inputs are inputted
            f.write(str(FF_all_inp[var_inp_1][var_12]))
        f.write('\n')
        f.write(PODEM_res[var_inp_1])
        f.write('\n')

with open(sys.argv[5], 'w') as f:  #Used to create the Deductive Fault simulator file

    for var_inp_1 in range(len(FF_all_inp)):
        for var_12 in range(0, max_inputs):  # till all the inputs are inputted
            if FF_all_inp[var_inp_1][var_12] == 'x':
                f.write('0')
            if FF_all_inp[var_inp_1][var_12] == 0 or FF_all_inp[var_inp_1][var_12] == 1:
                f.write(str(FF_all_inp[var_inp_1][var_12]))
        f.write('\n')

os.startfile(sys.argv[2])
os.startfile(sys.argv[3])
os.startfile(sys.argv[5])