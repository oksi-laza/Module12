from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        Test for walk function in module runner
        """
        obj = Runner('Den')
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        """
        Test for run function in module runner
        """
        obj = Runner('Max')
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        """
        Test for compare the inequality - run and walk functions in module runner
        """
        obj1 = Runner('Alex')
        obj2 = Runner('Lion')
        for _ in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)


# Если изменить значения в тестах, то они не будут пройдены, результат кода 'FAILED (failures=2)'
# class RunnerTest(unittest.TestCase):
#     def test_walk(self):
#         """
#         Test for walk function in module runner
#         """
#         obj = Runner('Den')
#         for _ in range(10):
#             obj.walk()
#         self.assertEqual(obj.distance, 60)    # AssertionError: 50 != 60
#
#     def test_run(self):
#         """
#         Test for run function in module runner
#         """
#         obj = Runner('Max')
#         for _ in range(10):
#             obj.run()
#         self.assertEqual(obj.distance, 90)    # AssertionError: 100 != 90
#
#     def test_challenge(self):
#         """
#         Test for compare the inequality - run and walk functions in module runner
#         """
#         obj1 = Runner('Alex')
#         obj2 = Runner('Lion')
#         for _ in range(10):
#             obj1.run()
#             obj2.walk()
#         self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == '__main__':
    unittest.main()
