import logging

logging.basicConfig(filename='myFactorialLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# test line
# turn this on/off to enable/disable logging messages
# DEBUG / INFO / WARNING / ERROR / CRITICAL
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' %n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
