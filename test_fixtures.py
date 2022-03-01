"""
    Precondition
        Setup, Connection, API

    Test

    Test

    Assertion

    Postcon
        clean, close, close

"""
import pytest

@pytest.fixture
def setup():
    print("Start Browser")

def test_1():
    print("Start Browser")
    print("Test 1 executed")
    print("Close Browser")

def test_2():
    print("Start Browser")
    print("Test 2 executed")
    print("Close Browser")

def test_3():
    print("Start Browser")
    print("Test 3 executed")
    print("Close Browser")