from mindocker.main import say_hello, say_goodbye

def test_main():
    assert 1 < 2

def test_say_hello():
    name = 'vim'
    expected = 'hello vim'
    assert say_hello(name) == expected

def test_say_goodbye():
    name = 'vim'
    expected = 'goodbye vim'
    assert say_goodbye(name) == expected

