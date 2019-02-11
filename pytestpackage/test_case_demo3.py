
import pytest

@pytest.yield_fixture()
def setUp():
    print("Running demo3 setUp ")
    yield
    print("Running demo3 tearDown ")

def test_demo3_methodA(setUp):
    print("Running demo3 method A")

def test_demo3_methodB(setUp):
    print("Running demo3 method B")