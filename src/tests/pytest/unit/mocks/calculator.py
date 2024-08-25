# モックの例として、もしCalculatorの挙動をモックしたい場合
class MockCalculator:
    def add(self, a, b):
        return 42  # 固定の値を返す例

    def subtract(self, a, b):
        return 42

    def multiply(self, a, b):
        return 42

    def divide(self, a, b):
        return 42
