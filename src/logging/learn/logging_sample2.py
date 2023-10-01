# ロガーのインスタンス化
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# handler
s_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logging_sample2.log', encoding='utf-8')

# ログレベルの設定
s_handler.setLevel(logging.DEBUG) # ターミナル出力するためのハンドラー
f_handler.setLevel(logging.ERROR) # ファイル出力するためのハンドラー

s_formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
f_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

# handlerにformatterを追加
s_handler.setFormatter(s_formatter)
f_handler.setFormatter(f_formatter)

# loggerにhandlerを設定
logger.addHandler(s_handler)
logger.addHandler(f_handler)

logger.debug('デバッグログ')
logger.info('インフォログ')
logger.warning('ワーニングログ')
logger.error('エラーログ')
logger.critical('クリティカルログ')


left_operand = 10
right_operand = 0
try:
    result = left_operand / right_operand
except Exception as e:
    logger.error(e, exc_info=True) # exc_info=Trueは例外処理で必ずつける



