"""

************
*          *     
*          *
*          *
************

"""

def boxPrint(symbol, width, height):
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

print(boxPrint('*', 15, 5))
print(boxPrint('O', 5, 16))