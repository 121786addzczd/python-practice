from unit.fixtures.calculator_fixture import calculator


def pytest_runtest_call(item):
    """
    pytestフック関数。各テスト関数が実行される際に、そのテスト関数のdocstringを取得して表示する。

    この関数はpytestの実行中に自動的に呼び出され、実行中のテスト関数にdocstringが存在する場合、その内容をターミナルに出力する。出力後の改行を避けるため、print関数のendパラメータに空文字列を指定している。

    Parameters:
    item: pytestのテスト項目。テスト関数やその関連情報が含まれている。
    """
    doc = item.function.__doc__
    if doc:
        print(f"{doc}", end="")
