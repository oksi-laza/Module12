from runner_and_tournament import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """Test for walk function in module runner"""
        obj = Runner('Den')
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        """Test for run function in module runner"""
        obj = Runner('Max')
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        """Test for compare the inequality - run and walk functions in module runner"""
        obj1 = Runner('Alex')
        obj2 = Runner('Lion')
        for _ in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}    # словарь, в который будут сохраняться результаты всех тестов.
        cls.key = 1

    def setUp(self):
        """ Метод, где создаются 3 объекта """
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test_start1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        finishers = tournament.start()
        TournamentTest.all_results[TournamentTest.key] = finishers
        last_runner = self.runner1.name if self.runner1.speed < self.runner3.speed else self.runner3.name
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results)][len(finishers)] == last_runner)

    def test_start2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        finishers = tournament.start()
        TournamentTest.key += 1
        TournamentTest.all_results[TournamentTest.key] = finishers
        last_runner = self.runner2.name if self.runner2.speed < self.runner3.speed else self.runner3.name
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results)][len(finishers)] == last_runner)

    def test_start3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        finishers = tournament.start()
        TournamentTest.key += 1
        TournamentTest.all_results[TournamentTest.key] = finishers
        if self.runner1.speed < self.runner2.speed and self.runner1.speed < self.runner3.speed:
            last_runner = self.runner1.name
        elif self.runner2.speed < self.runner1.speed and self.runner2.speed < self.runner3.speed:
            last_runner = self.runner2.name
        else:
            last_runner = self.runner3.name
        self.assertTrue(TournamentTest.all_results[len(TournamentTest.all_results)][len(finishers)] == last_runner)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():    # если словарь со словарями
            print(result)


if __name__ == '__main__':
    unittest.main()
