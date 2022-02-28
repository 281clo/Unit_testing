'''pytest
test1
test_1
test_1
1_test
pytest will run all files from current dir/ subdirec test_*.py or *_test.py
'''

def test_1():
    x=10
    y=10
    assert x==y

def test_2():
    name="Selenium"
    title="Selenium is for web automation"
    assert name in title

def test_3():
    name="Jenkins is CI server"
    title="Jenkins is CI server"
    assert name is title , "Title does not match"