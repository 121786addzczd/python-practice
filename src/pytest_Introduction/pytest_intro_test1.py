# とりあえずpytest実行
# 実行コマンドは「pytest pytest_intro_test1.py」
# bash: pytest: command not foundと出力された場合は
#「python -m pytest_intro_test1.py」を試してください
# python -m pytest_intro_test1.py -sコマンド実行するとprint文表示されます


def test_hello_world() -> None:
    print("Hello World! ")