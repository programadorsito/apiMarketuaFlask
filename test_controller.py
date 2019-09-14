import unittest
import controller

class TestController(unittest.TestCase):

    def test_save(self):
        result = controller.save({"id":"1","nombre":"kartman"})
        self.assertEqual(result,True)

    def test_get(self):
        controller.save({"id":"1","nombre":"kartman"})
        result = controller.get("1")
        self.assertEqual(result,{"id":"1","nombre":"kartman"})

    def test_update(self):
        result = controller.update({"id":"1","nombre":"kenny"})
        self.assertEqual(result,True)

    def test_delete(self):
        controller.save({"id":"1","nombre":"kartman"})
        result = controller.delete("1")
        self.assertEqual(result,True)
        
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
