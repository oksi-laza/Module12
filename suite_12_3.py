import unittest
import tests_12_3


contestST = unittest.TestSuite()    # создали объект 'TestSuite()'
contestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
contestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)    # cоздали объект класса TextTestRunner, с аргументом verbosity=2.
runner.run(contestST)    # указываем какой TestSuite запускаем
