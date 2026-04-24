# AES Round 1 Simulation for Security Assignment

def shift_rows(state):
    """تطبيق عملية إزاحة الصفوف"""
    res = [None] * 16
    # Row 0: No shift
    res[0], res[4], res[8], res[12] = state[0], state[4], state[8], state[12]
    # Row 1: Shift left by 1
    res[1], res[5], res[9], res[13] = state[5], state[9], state[13], state[1]
    # Row 2: Shift left by 2
    res[2], res[6], res[10], res[14] = state[10], state[14], state[2], state[6]
    # Row 3: Shift left by 3
    res[3], res[7], res[11], res[15] = state[15], state[3], state[7], state[11]
    return res

def main():
    # القيم المستخرجة من تمرينك (Round 1 Start)
    input_hex = "00102030405060708090a0b0c0d0e0f0"
    state = [int(input_hex[i:i+2], 16) for i in range(0, len(input_hex), 2)]
    
    print(f"Input State:  {input_hex}")
    
    # محاكاة لخطوة ShiftRows (Decalage) المذكورة في الورقة
    shifted = shift_rows(state)
    output_hex = "".join(format(b, '02x') for b in shifted)
    
    print(f"After ShiftRows: {output_hex}")
    print("\nNote: Complete Round 1 includes SubBytes, MixColumns and AddRoundKey.")

if __name__ == "__main__":
    main()
