import unittest
import app

class TestApp(unittest.TestCase):
    def testMeters(self):
        self.assertEqual(app.calculate_meters(4,3), 12)
        self.assertEqual(app.calculate_meters(8, 3), 24)

    def testWindows(self):
        self.assertEqual(app.calculate_windows(1), 2.4)
        self.assertEqual(app.calculate_windows(2), 4.8)

    def testDoors(self):
        self.assertEqual(app.calculate_doors(1), 1.52)
        self.assertEqual(app.calculate_doors(2), 3.04)

    def subtractWindowsDoors(self):
        self.assertEqual(app.subtract_windows_doors(1, 0, 12), 9.6)
        self.assertEqual(app.subtract_windows_doors(0, 1, 12), 10.48)

    def testCheckRules(self):
        self.assertEqual(app.check_rules(8, 0, 1, 2), 0)
        self.assertEqual(app.check_rules(8, 5, 1, 4), 0)

    def testCalculateLiters(self):
        self.assertEqual(app.calculate_liters(12), 2.4)

if __name__ == '__main__':
    unittest.main()