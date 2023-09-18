# 指定した関数のテストのみを実行する場合
# python -m pytest skip_test3.py -k "hello" -s
# helloの文字列が含まれる関数のみテストが実行されます
# 対象の関数に指定した文字が含まれていない場合はnotを付けて実行
# python -m pytest skip_test3.py -k "not hello" -s

def test_hello():
    print("Hello1")


def test_hello2():
    print("hello2")


def test_afternoon1():
    print("afternoon1")