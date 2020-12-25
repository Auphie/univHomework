def coding(inputs, sep):
    base = ''.join(a for a in inputs if a.isalpha())
    baseSW  = base.swapcase()
    sep_base = [baseSW[i:i+sep] for i in range(0,len(baseSW),sep)]
    inv_base = sep_base[::-1]
    #baseIns = '/'.join(baseSW[i:i+sep] for i in range(0,len(baseSW),sep))
    baseIns = '/'.join(a for a in inv_base)
    return baseIns

inputs = input()
sep = input()
result = coding(inputs, int(sep))
print(result)