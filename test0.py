import unittest as t
from random import Random

global random
random = Random()

class TestSet0(t.TestCase):
    a = np.array((1, 2, 3))
    b = np.array((4, 5, 6))
    c = np.array((7,8))
    z = np.zeros(3)

    def test_valid_additions(self):
        for i in range(4):
            size = random.randint(2,20)
            z = np.zeros(size)
            for j in range(25):
                a = np.random.rand(size)
                b = np.random.rand(size)
                np.testing.assert_array_equal(vector_addition(a, b), a+b)
                np.testing.assert_array_equal(vector_addition(a, z), a)

    def test_invalid_additions(self):
        for i in range(4):
            size1 = random.randint(2,20)
            size2 = size1 + random.randint(1,5)
            a = np.random.rand(size1)
            b = np.random.rand(size2)
            with self.assertRaises(Exception):
                vector_addition(a, d)

    def test_inversions(self):
        for i in range(4):
            size = random.randint(2,20)
            z = np.zeros(size)
            np.testing.assert_array_equal(inverse_vector(z), z)
            for i in range(25):
                a = np.random.rand(size)
                np.testing.assert_array_equal(inverse_vector(a), -a)

    def test_additions_with_inverse(self):
        for i in range(4):
            size = random.randint(2,20)
            z = np.zeros(size)
            np.testing.assert_array_equal(inverse_vector(z), z)
            for i in range(25):
                a = np.random.rand(size)
                np.testing.assert_array_equal(vector_addition(a, inverse_vector(a)), z)

if __name__ == '__main__':
    suite.addTest(t.TestLoader().loadTestsFromTestCase(TestSet0))
    runner = t.TextTestRunner(verbosity=2)
    runner.run(suite)
    #t.main(argv=['first-arg-is-ignored'], exit=False)
