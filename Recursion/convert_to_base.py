def convert(num,base):
    if num<base:
        return str(num)
    else:
        return convert(num//base,base)+str(num%base)

print(convert(10,2))