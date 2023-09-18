# fixtureの利用
# fixtureを使用すると自分が付与したい関数に前処理＆後処理関数付与できる
import pytest

@pytest.fixture() # デフォルトではscope="function"
def setup_processing(request):
    print("setup_processing") # 後処理だけ実行したい場合はこの行削除
    # 前処理だけでいい場合は以下記述削除
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)


def test_hello(setup_processing):
    print("Hello")


def test_goodmorning():
    print("goodmorning")


def test_goodafternoon(setup_processing):
    print("goodafternoon")
