# クラスに対する＆前処理＆後処理
# すべてのクラスのメソッドの前後にsetupとteardownメソッドが実行される
class TestExample():
    # 前処理
    @classmethod
    def setup_class(cls):
        print("setup_class")


    # 後処理
    @classmethod
    def teardown_class(cls):
        print("teardown_class")


    def test_example1(self):
        print("Hello World!!")


    def test_example2(self):
        print("pytest!")
