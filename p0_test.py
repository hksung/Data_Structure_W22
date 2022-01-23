from p0 import *
import pytest

class TestMain:

    def test_initInvalid(self):
        with pytest.raises(ComplexConstructorTypeERROR):
            number1 = Complex(1, None)

        with pytest.raises(ComplexConstructorTypeERROR):
            number1 = Complex(None, 1)

        with pytest.raises(ComplexConstructorTypeERROR):
            number1 = Complex(None, None)

    def test_initValidInt(self):
        try:
            number = Complex(1, 2)
        except:
            raise Exception("Failed Test (ValidInt)")

        assert number.a == 1
        assert number.b == 2

    def test_initValidFloat(self):
        try:
            number = Complex(1.1, 2.1)
        except:
            raise Exception("Failed Test (ValidFloat)")

        assert number.a == 1.1
        assert number.b == 2.1

    def test_addValidInt(self):
        I1 = Complex(3, 2)
        I2 = Complex(2, 3)
        I3 = I1 + I2
        assert I3.a == 5
        assert I3.b == 5

    def test_addValidFloat(self):
        F1 = Complex(3.1, 2.6)
        F2 = Complex(6.2, 7.8)
        F3 = F1 + F2
        assert round(F3.a, 3) == 9.3
        assert round(F3.b, 3) == 10.4

    def test_addInvalid(self):
        N1 = Complex(2, 3)
        N2 = "Hi"
        with pytest.raises(TypeError):
            N3 = N1 + N2

    def test_subValidInt(self):
        I1 = Complex(3, 2)
        I2 = Complex(2, 3)
        I3 = I1 - I2
        assert I3.a == 1
        assert I3.b == -1

    def test_subValidFloat(self):
        F1 = Complex(3.1, 2.6)
        F2 = Complex(6.2, 7.8)
        F3 = F1 - F2
        assert round(F3.a, 2) == -3.1
        assert round(F3.b, 2) == -5.2

    def test_subInvalid(self):
        N1 = Complex(2, 3)
        N2 = "Hi"
        with pytest.raises(TypeError):
            N3 = N1 - N2

    def test_mulValidInt(self):
        I1 = Complex(3, 2)
        I2 = Complex(2, 3)
        I3 = I1 * I2
        assert I3.a == 0
        assert I3.b == 13


    def test_mulValidFloat(self):
        F1 = Complex(3.1, 2.6)
        F2 = Complex(6.2, 7.8)
        F3 = F1 * F2
        assert round(F3.a, 2) == -1.06
        assert round(F3.b, 2) == 40.3

    def test_mulInvalid(self):
        N1 = Complex(2, 3)
        N2 = "Hi"
        with pytest.raises(TypeError):
            N3 = N1 * N2

    def test_divValidInt(self):
        I1 = Complex(3, 2)
        I2 = Complex(2, 3)
        I3 = I1 / I2
        assert round(I3.a, 2) == 0.92
        assert round(I3.b, 2) == -0.38


    def test_divValidFloat(self):
        F1 = Complex(3.1, 2.6)
        F2 = Complex(6.2, 7.8)
        F3 = F1 / F2
        assert round(F3.a, 3) == 0.398
        assert round(F3.b, 3) == -0.081

    def test_divInvalid(self):
        N1 = Complex(2, 3)
        N2 = "Hi"
        with pytest.raises(TypeError):
            N3 = N1 / N2
