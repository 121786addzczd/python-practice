# モジュールに対する前処理＆後処理
import pytest

# "autouse=True" クラスのメソッド引数にsetup_processingを渡さなくても前処理＆後処理実行できる
@pytest.fixture(autouse=True) # デフォルトはFalse
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)


class TestExample():
    def test_hello(self):
        print("Hello")


    def test_goodmorning(self):
        print("goodmorning")


    def test_goodafternoon(self):
        print("goodafternoon")