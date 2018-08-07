import traceback, datetime

try:
    # raised exceptions are for user errors and should raise exceptions
    raise Exception('This is the error message.')
except: 
        errorFile = open('error_log.txt', 'a')
        errorFile.write('Exception occurred at: ' + str(datetime.datetime.now()) + '\n')
        errorFile.write(traceback.format_exc() + '\n')
        errorFile.close()
        print('The traceback info was written to error_log.txt')

"""

************
*          *     
*          *
*          *
************

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2."')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

print(boxPrint('*', 15, 5))
print(boxPrint('O', 5, 16))