import pytest


@pytest.fixture()
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)


class TestExample():
    def test_hello(self, setup_processing):
        print("Hello")


    def test_goodmorning(self):
        print("goodmorning")


    def test_goodafternoon(self, setup_processing):
        print("goodafternoon")
