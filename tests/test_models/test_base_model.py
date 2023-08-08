from unittest import TestCase, mock, main
"""Test for BaseModel Class"""
from models.engine import FileStorage 
from models.base_model import BaseModel
import datetime


class TestBaseModel(TestCase):
    """Tests BaseModel instances"""
    def test_unique_id(self):
        """test_unique_id"""
        baseM1 = BaseModel()
        baseM2 = BaseModel()
        self.assertNotEqual(baseM1.id, baseM2.id)

    def test_created_at(self):
        """test_created_at"""
        mock_date = datetime.datetime(2023, 8, 8, 00, 00, 00, 00000)
        datetime_mock = mock.Mock(wraps=datetime.datetime)
        datetime_mock.now.return_value = mock_date
        with mock.patch('models.base_model.datetime', new=datetime_mock):
            base = BaseModel()
            self.assertEqual(base.created_at, mock_date)
   
    def test_updated_at(self):
        """test_updated_at"""
        mock_date = datetime.datetime(2023, 8, 8, 00, 00, 00, 00000)
        datetime_mock = mock.Mock(wraps=datetime.datetime)
        datetime_mock.now.return_value = mock_date
        with mock.patch('models.base_model.datetime', new=datetime_mock):
            base = BaseModel()
            self.assertEqual(base.updated_at, mock_date)

    def test_2_instances_with_diff_dates(self):
        """test_2_instances_with_diff_dates"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)
        self.assertNotEqual(base1.created_at, base1.updated_at)

class TestBaseModel_save(TestCase):
    """TestBaseModel_save"""
    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def updated_at_change(self):
        """test_updated_at_change"""
        base = BaseModel()
        updated_date = base.updated_at
        print(updated_date)
        base.save()
        self.assertNotEqual(base.updated_at, updated_date)

class TestBaseModel_Kwargs(TestCase):
    """TestBaseModel_Kwargs"""
    pass

if __name__ == "__main__":
    main()
