# テストのスキップ
# pytest skip_test2.py -m "morning" コマンドで確認できます
# -m "morning"は実行したいグループ名を指定しています
# morningだけのグループをテストしない場合は以下コマンド
# pytest skip_test2.py -m "not morning -s"
# 同じ階層にある「pytest.ini」はグループのテストを実行した際に、
# ターミナルからwarningが表示されないように追加してあります
import pytest

def test_hello():
    print("Hello")

# 以下の関数をmorningのグループに入れる
@pytest.mark.morning
def test_goodmorning():
    print("goodmorning")


@pytest.mark.afternonn
def test_goodafternonn():
    print("goodafternonn")