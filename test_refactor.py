import unittest
from legacy_unrefactored import p
from clean_refactored import calculate_active_student_metrics

class TestRefactoring(unittest.TestCase):
    def test_functional_consistency(self):
        data = [
            {'n': 'alice', 'g': 85, 's': 'A'},
            {'n': 'bob', 'g': 72, 's': 'B'},
            {'n': 'vedanshi', 'g': 92, 's': 'A'}
        ]
        legacy_avg, legacy_names = p(data)
        clean_avg, clean_names = calculate_active_student_metrics(data)
        self.assertEqual(legacy_avg, clean_avg)
        self.assertEqual(len(legacy_names), len(clean_names))

if __name__ == '__main__':
    unittest.main()
