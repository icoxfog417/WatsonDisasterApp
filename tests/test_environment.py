import unittest
from app.environment import Environment


class TestEnvironment(unittest.TestCase):

    def test_load_environment(self):
        env = Environment()
        self.assertTrue(env)
        print(env)