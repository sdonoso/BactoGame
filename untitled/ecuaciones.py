def temperatura_mar( hora):
    if hora >= 0 and hora <= 8:
        temp = 4
    elif hora > 8 and hora <= 16:
        temp = 2 * hora + -12
    elif hora > 16 and hora <= 24:
        temp = -2 * hora + 52
    return temp
