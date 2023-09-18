# とりあえずpytest実行
# 実行コマンドは「pytest test_section_2.py」
# bash: pytest: command not foundと出力された場合は
#「python -m pytest test_section_2.py」を試してください
# python -m pytest test_section_2.py -sコマンド実行するとprint文表示されます


def test_hello_world() -> None:
    print("Hello World!")


