import unittest
import controller

class TestController(unittest.TestCase):
    def test_save(self):
        result = controller.save({"id":"1", "nombre":"kartman"})
        self.assertEqual(result,True)