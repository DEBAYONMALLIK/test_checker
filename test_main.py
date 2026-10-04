from main import is_prime

def test_prime_number():
    assert is_prime(7)==True

def test_is_not_prime():
    assert is_prime(10)==False

def test_two_is_prime():
    assert is_prime(2)==True   