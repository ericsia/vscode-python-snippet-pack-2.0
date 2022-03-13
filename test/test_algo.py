from matplotlib.pyplot import cla
from src.algo import is_prime
from src.algo import fast_power

class TestPrime():

    def test_0(self):
        assert is_prime(1) == False
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(4) == False 

    def test_1(self):
        assert is_prime(-23) == False
        assert is_prime(23) == True 

    def test_2(self):
        assert is_prime(7*7) == False
        assert is_prime(11*11) == False
        assert is_prime(13*13) == False
        assert is_prime(13*13*13) == False

class TestFastPower():

    def test_0(self):
        assert fast_power(2, 0) == 1
        assert fast_power(2, 1) == 2
        assert fast_power(2, 2) == 4
        assert fast_power(2, 3) == 8
        assert fast_power(2, 4) == 16

    def test_1(self):
        assert fast_power(2, -1) == 1/2
        assert fast_power(2, -2) == 1/4
        assert fast_power(2, -3) == 1/8
        assert fast_power(2, -4) == 1/16

