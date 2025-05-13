from calculadora import calculadora

def test_soma():
    assert calculadora(2, 3, '+') == 5
    assert calculadora(10, 3, '+') == 13
    assert calculadora(-5, 5, '+') == 0
    assert calculadora(2.5, 2.5, '+') == 5.0

def test_subtracao():
    assert calculadora(5, 3, '-') == 2
    assert calculadora(6, 3, '-') == 3
    assert calculadora(-3, -3, '-') == 0

def test_multiplicacao():
    assert calculadora(2, 4, '*') == 8
    assert calculadora(2, 2, '*') == 4
    assert calculadora(-2, 3, '*') == -6

def test_divisao():
    assert calculadora(10, 2, '/') == 5
    assert calculadora(20, 2, '/') == 10

def test_divisao_por_zero():
    assert calculadora(10, 0, '/') is None
    assert calculadora(20, 0, '/') is None

def test_potenciacao():
    assert calculadora(2, 3, '^') == 8
    assert calculadora(2, 2, '^') == 4
    assert calculadora(9, 0.5, '^') == 3

def test_operacao_invalida():
    assert calculadora(2, 3, '%') is None
    assert calculadora(2, 3, 'x') is None

def test_valores_invalidos():
    assert calculadora("abc", 3, '+') is None
    assert calculadora(2, "xyz", '*') is None
    assert calculadora(None, 2, '+') is None
    assert calculadora(2, None, '-') is None
