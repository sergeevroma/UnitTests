import unittest
from test_geometry import TestRectangle, TestCircle, TestSquare, TestTriangle

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_geometry.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\nРезультаты тестирования:")
    print(f"Тестов выполнено: {result.testsRun}")
    print(f"Ошибок: {len(result.errors)}") # Python exceptions
    print(f"Провалов: {len(result.failures)}") #Unittest's assertion fails
    
    total = result.testsRun
    passed_tests = total - len(result.failures) - len(result.errors)
    coverage = (passed_tests / total) * 100 if total > 0 else 0
    print(f"Покрытие: {coverage:.1f} %")


if __name__ == '__main__':
    run_tests()