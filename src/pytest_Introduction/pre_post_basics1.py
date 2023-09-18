# 前処理＆後処理の関数の作成
# 前処理
def setup_function(function):
    """
    pytestによって自動的に呼び出される特別な関数
    テスト関数が実行される前に、この関数が呼び出されます
    """
    print("setup_function")


# 後処理
def teardown_function(function):
    """
    pytestによって自動的に呼び出される特別な関数
    テスト関数が実行された後に、この関数が呼び出される
    """
    print("teardown_function")


def test_hello_world():
    print("Hello World")


def test_pytest():
    print("pytest")