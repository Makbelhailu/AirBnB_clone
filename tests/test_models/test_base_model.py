#!usr/bin/python3
"""unittesting"""

import unittest
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Contains the actual tests"""

    def setUp(self):
        '''Set up the base by creating an instance of the BaseModel'''
        self.base_model = BaseModel()
        self.base_model1 = BaseModel()

    def tearDown(self):
        """Delete instances"""
        del self.base_model
        del self.base_model1

    def test_instances(self):
        """Tests if the instances are created"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model1, BaseModel)

    def test_uuid(self):
        """tests uuid"""
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model1, "id"))
        self.assertNotEqual(self.base_model.id, self.base_model1.id)

    def test_datetime(self):
        """datetime test"""
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        datenow = datetime.datetime.now()
        self.testmodel = BaseModel()
        self.assertNotEqual(self.testmodel.created_at, datenow)
        self.assertNotEqual(self.testmodel.created_at,
                            self.testmodel.updated_at)
        self.testmodel.save()
        self.assertNotEqual(self.testmodel.created_at,
                            self.testmodel.updated_at)

    def test_todict(self):
        """Tests the to_dict() method"""
        model_dict = self.base_model.to_dict()
        self.assertTrue(type(model_dict), dict)
        for key in model_dict:
            self.assertTrue(type(key), str)
            self.assertNotEqual(key, None)


if __name__ == "__main__":
    unittest.main()
