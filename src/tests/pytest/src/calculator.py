class Calculator:
    def add(self, a, b):
        try:
            return float(a) + float(b)
        except ValueError:
            raise ValueError("無効な入力です: 両方の引数は数値でなければなりません")

    def subtract(self, a, b):
        try:
            return float(a) - float(b)
        except ValueError:
            raise ValueError("無効な入力です: 両方の引数は数値でなければなりません")

    def multiply(self, a, b):
        try:
            return float(a) * float(b)
        except ValueError:
            raise ValueError("無効な入力です: 両方の引数は数値でなければなりません")

    def divide(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise ValueError("無効な入力です: 両方の引数は数値でなければなりません")

        if b == 0:
            raise ValueError("ゼロで割ることはできません")

        return a / b
