"""This Module contains tests for File_Storage Class"""
from unittest import TestCase, main
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.user import User
import models
import os
import json


class TestFileStorage_type(TestCase):
    """Define TestCases of FileStorage"""

    def test_file_storage_objects_type(self):
        """test_file_storage_objects_type"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_file_storage_file_path_type(self):
        """test_file_storage_file_path_type"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_file_storage_instance_storage(self):
        """test_file_storage_instance_storage"""
        self.assertIsInstance(models.storage, FileStorage)

    def test_file_storage_instance(self):
        """test_file_storage_instance"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_all(TestCase):
    """Define TestCase related to all method"""

    def test_storage_new_instance(self):
        """test_storage_new_instance"""
        base = BaseModel()
        objs_keys = models.storage.all().keys()
        self.assertIn("BaseModel.{}".format(base.id), objs_keys)

    def test_storage_multiple_instances(self):
        """test_storage_multiple_instances"""
        user = User()
        place = Place()
        base = BaseModel()
        objs_keys = models.storage.all().keys()
        self.assertIn("BaseModel.{}".format(base.id), objs_keys)
        self.assertIn("Place.{}".format(place.id), objs_keys)
        self.assertIn("User.{}".format(user.id), objs_keys)

    def test_file_storage_all_with_args(self):
        """test_file_storage_all_with_args"""
        with self.assertRaises(TypeError):
            models.storage.all("args")


class TestFileStorage_new(TestCase):
    """Define TestCase related to new method"""

    def test_storage_new_with_multiple_args(self):
        """test_storage_new_with_multiple_args"""
        with self.assertRaises(TypeError):
            models.storage.new(None, "args")

    def test_storage_new_no_valid_obj(self):
        """test_storage_new_no_valid_obj"""
        with self.assertRaises(AttributeError):
            models.storage.new("args")


class TestFileStorage_save(TestCase):
    """Define TestCase related to save method"""

    file_path = "HA_YA_FILE.json"

    def setUp(self):
        """setUp will be executed before each test case"""
        try:
            os.remove(self.file_path)
        except Exception:
            pass

    def test_file_storage_save_with_args(self):
        """test_file_storage_save_with_args"""
        with self.assertRaises(TypeError):
            models.storage.save("args")

    def test_file_storage_save_into_file(self):
        """test_file_storage_save_into_file"""
        base = BaseModel()
        user = User()
        place = Place()
        self.assertEqual(os.path.exists(self.file_path), False)
        models.storage.save()
        self.assertEqual(os.path.exists(self.file_path), True)
        with open(self.file_path, "r", encoding="utf-8") as file:
            dicts = json.load(file)
            self.assertIn("BaseModel.{}".format(base.id), dicts.keys())
            self.assertIn("Place.{}".format(place.id), dicts.keys())
            self.assertIn("User.{}".format(user.id), dicts.keys())


class TestFileStorage_reload(TestCase):
    """Define TestCase related to reload method"""

    def test_file_storage_reload(self):
        """test_file_storage_reload"""
        base = BaseModel()
        user = User()
        place = Place()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        self.assertNotEqual(models.storage.all(), {})

    def test_file_storage_reload_check_data(self):
        """test_file_storage_reload_check_data"""
        base = BaseModel()
        user = User()
        place = Place()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        objs_keys = models.storage.all().keys()
        self.assertIn("BaseModel.{}".format(base.id), objs_keys)
        self.assertIn("Place.{}".format(place.id), objs_keys)
        self.assertIn("User.{}".format(user.id), objs_keys)

    def test_file_storage_reload_with_args(self):
        """test_file_storage_reload_with_args"""
        with self.assertRaises(TypeError):
            models.storage.reload("args")


if __name__ == "__main__":
    main()
