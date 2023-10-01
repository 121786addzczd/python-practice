import logging

logging.basicConfig(level=logging.DEBUG, filename='sample.log',
                    format='%(asctime)s-%(process)s-%(levelname)s-%(message)s')
logging.debug('debug log')
logging.info('info log')
logging.warning('warning log')
logging.error('error log')
logging.critical('critical log')


user = 'Jon'
# logging.error('%s raised error', user)
# logging.error(f'{user} raised error') # python3.6以上
logging.error(f'{user=} raised error') # python3.8以上

left_operand = 10
right_operand = 0
try:
    result = left_operand / right_operand
except Exception as e:
    logging.error(e, exc_info=True) # exc_info=Trueは例外処理で必ずつける