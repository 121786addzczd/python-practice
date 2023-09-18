# モジュールに対する前処理＆後処理
import pytest

@pytest.fixture(scope="module")
def setup_module(request):
    print("setup_module")
    def teardown_module():
        print("teardown_module")
    request.addfinalizer(teardown_module)


@pytest.fixture(scope="function")
def setup_function(request):
    print("setup_function")
    def teardown_function():
        print("teardown_function")
    request.addfinalizer(teardown_function)


def test_hellow_world(setup_module, setup_function):
    print("Hello World!")


def test_pytest(setup_module):
    print("pytest")


class TestExample():
    def test_hello_world(self, setup_module):
        print("Hello World!")


    def test_pytest(self, setup_module):
        print("pytest")