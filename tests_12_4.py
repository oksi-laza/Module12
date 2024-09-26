from rt_with_exceptions import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """Test for walk function in module runner"""
        try:
            obj = Runner('Den', -5)
            for _ in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """Test for run function in module runner"""
        try:
            obj = Runner(25)
            for _ in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """Test for compare the inequality - run and walk functions in module runner"""
        obj1 = Runner('Alex')
        obj2 = Runner('Lion')
        for _ in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
