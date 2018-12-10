from mindocker.main import say_hello

def test_main():
    assert 1 < 2

def test_say_hello():
    name = 'vim'
    expected = 'hello vim'
    assert say_hello(name) == expected

