def isEven(item):
    item = str(int(item)).split()
    if item[len(item)-1] in ("1","3","5","7","9"):
        return False
    return True
