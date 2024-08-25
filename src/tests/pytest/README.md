# このリポジトリは pytest の練習用リポジトリです

## ライブラリの導入

以下のコマンドで必要なライブラリをインストールします。

```shell
pip install pytest pytest-subtests pytest-cov
```

## テストの実行方法

### 通常のテスト実行

```shell
pytest unit
```

### 詳細なテスト結果を表示して実行

```shell
pytest unit -v
```

### print 文の出力を表示しながら実行

```shell
pytest unit -v -s
```

### 特定のファイルのみをテスト実行

```shell
pytest -v -s unit/tests/test_calculator.py
```

### 特定のテスト関数のみを実行

```shell
pytest -v -s unit/tests/test_calculator.py::test_multiply_invalid_inputs
```

### 特定のファイルを対象にテストを実行し、カバレッジを出力

```shell
pytest --cov=src --cov-report=term-missing -v -s
```

### HTML 形式のカバレッジレポートを生成

```shell
pytest --cov=src --cov-report=html
```

htmlcov ディレクトリが生成され、index.html ファイルを見ることで可視化できます
