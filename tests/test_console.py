from unittest import TestCase, mock, main
from console import HBNBCommand
from io import StringIO
import uuid
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.engine.file_storage import FileStorage
import json
import models
import os


class TestConsole_prompt(TestCase):
    """Test console prompt"""

    def test_console_prompt_value(self):
        """test_console_prompt_value"""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_console_with_empty_line_or_space(self):
        """test_console_with_empty_line_or_space"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual("", output.getvalue().strip())

    def test_console_with_new_line(self):
        """test_console_with_new_line"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", output.getvalue().strip())


class TestConsole_help(TestCase):
    """Test case command"""

    def test_console_help_EOF(self):
        """test_console_help_EOF"""
        expected_output = "Exit when EOF or when Press CTRL+D"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_console_help_quit(self):
        """test_console_help_quit"""
        expected_output = "Quit to exit the program"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_console_help_create(self):
        """test_console_help_create"""
        e = "Creates instance and save it to a JSON file Usage:create <class>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_show(self):
        """test_console_help_show"""
        e = "Prints str representation of instance Usage:show <class> <id>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_all(self):
        """test_console_help_all"""
        e = "Prints str representation of"
        e += " all class instances Usage:all <class>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_destroy(self):
        """test_console_help_destroy"""
        e = "Deletes an instance Usage:destroy <class> <id>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_update(self):
        """test_console_help_update"""
        e = "Updates an instance Usage:update <class> <id> <attr> <value>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
            self.assertEqual(e, output.getvalue().strip())


class TestConsole_create(TestCase):
    """Test create command"""

    file_path = "HA_YA_FILE.json"

    def test_create_with_missing_class(self):
        """test_create_with_missing_class"""
        e = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(e, output.getvalue().strip())

    def test_create_with_non_exist_class(self):
        """test_create_with_non_exist_class"""
        e = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create NonExistClass")
            self.assertEqual(e, output.getvalue().strip())

    def test_create_base_model(self):
        """test_create_base_model"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                HBNBCommand().onecmd("create BaseModel")
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_user(self):
        """test_create_user"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                HBNBCommand().onecmd("create User")
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_base_model_save_to_file(self):
        """test_create_base_model_save_to_file"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            with open(self.file_path, "r") as f:
                objs = json.load(f)

                output_value = output.getvalue().strip()
                self.assertIn("BaseModel.{}".format(output_value), objs.keys())

    def test_create_user_save_to_file(self):
        """test_create_user_save_to_file"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            with open(self.file_path, "r") as f:
                objs = json.load(f)

                output_value = output.getvalue().strip()
                self.assertIn("User.{}".format(output_value), objs.keys())


class TestConsole_exit(TestCase):
    """Test exit from console commands"""

    def test_eof_command_return_value(self):
        """test_eof_command_return_value"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_quit_command_return_value(self):
        """test_quit_command_return_value"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))


class TestConsole_show(TestCase):
    """Test show command"""

    def test_show_missing_class(self):
        """test_show_missing_class"""
        expected_output = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_with_non_exist_class(self):
        """test_show_with_non_exist_class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show NonExistClass")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_with_missing_id(self):
        """test_show_with_missing_id"""
        expected_output = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_with_non_exist_id(self):
        """test_show_with_non_exist_id"""
        expected_output = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel xxxx-xxxx-xxxx-xxxx")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_existing_instance(self):
        """test_show_existing_instance"""
        base_id = ""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            base_id = output.getvalue().strip()

        base = models.storage.all()["BaseModel.{}".format(base_id)]
        exp = base.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel {}".format(base_id))
            self.assertEqual(exp, output.getvalue().strip())


class TestConsole_all(TestCase):
    """Test all command"""

    file_path = "HA_YA_FILE.json"

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def test_all_with_non_exist_class(self):
        """test_all_with_non_exist_class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all NonExistClass")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_all_on_empty_storage(self):
        """test_all_on_empty_storage"""
        expected_output = "[]"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_all_with_class_on_empty_storage(self):
        """test_all_with_class_on_empty_file"""
        expected_output = "[]"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_all(self):
        """test_all"""
        base1 = BaseModel()
        base2 = BaseModel()
        user1 = User()
        user2 = User()
        objs = models.storage.all()
        objs_list = [obj.__str__() for obj in objs.values()]

        objs_str = ""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(objs_list), objs_str)

    def test_all_with_class(self):
        """test_all_with_class"""
        base1 = BaseModel()
        base2 = BaseModel()
        user1 = User()
        user2 = User()
        objs = models.storage.all()
        objs_list = [obj.__str__() for obj in objs.values()
                     if obj.__class__.__name__ == "BaseModel"]

        objs_str = ""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(objs_list), objs_str)


class TestConsole_destroy(TestCase):
    """Test destroy command"""

    file_path = "HA_YA_FILE.json"

    def test_destroy_missing_class(self):
        """test_destroy_missing_class"""
        expected_output = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_non_exist_class(self):
        """test_destroy_with_non_exist_class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy NonExistClass")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_missing_id(self):
        """test_destroy_with_missing_id"""
        expected_output = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_non_exist_id(self):
        """test_destroy_with_non_exist_id"""
        expected_output = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel xxxx-xxxx-xxxx-xxxx")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_existing_instance(self):
        """test_destroy_existing_instance"""
        base = BaseModel()

        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel {}".format(base.id))
            objects = models.storage.all()
            self.assertNotIn("BaseModel.{}".format(base.id), objects.keys())

    def test_destroy_and_check_file(self):
        """test_destroy_and_check_file"""
        base = BaseModel()
        models.storage.save()

        HBNBCommand().onecmd("destroy BaseModel {}".format(base.id))
        with open(self.file_path, "r") as f:
            objs = json.load(f)
            self.assertNotIn("BaseModel.{}".format(base.id), objs.keys())

class TestConsole_update(TestCase):
    """Test update command"""

    file_path = "HA_YA_FILE.json"

    def test_update_missing_class(self):
        """test_update_missing_class"""
        expected_output = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_non_exist_class(self):
        """test_update_with_non_exist_class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update NonExistClass")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_missing_id(self):
        """test_update_with_missing_id"""
        expected_output = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_non_exist_id(self):
        """test_update_with_non_exist_id"""
        expected_output = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel xxxx-xxxx-xxxx-xxxx")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_missing_attribute(self):
        """test_update_with_missing_attribute"""
        base = BaseModel()

        expected_output = "** attribute name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel {}".format(base.id))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_missing_attribute_value(self):
        """test_update_with_missing_attribute"""
        base = BaseModel()

        expected_output = "** value missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel {} attr".format(base.id))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_user_first_name_attr(self):
        """test_update_user_first_name_attr"""
        user = User()
        line = "update User {} first_name Hajar".format(user.id)

        HBNBCommand().onecmd(line)
        updated_user = models.storage.all()["User.{}".format(user.id)]
        self.assertEqual(updated_user.first_name, "Hajar")

    def test_update_place_check_float_type_attr(self):
        """test_update_place_check_float_type_attr"""
        place = Place()
        line = "update Place {} latitude -8.242735".format(place.id)

        HBNBCommand().onecmd(line)
        updated_place = models.storage.all()["Place.{}".format(place.id)]
        self.assertEqual(updated_place.latitude, -8.242735)
        self.assertEqual(type(updated_place.latitude), float)

    def test_update_place_check_int_type_attr(self):
        """test_update_place_check_int_type_attr"""
        place = Place()
        line = "update Place {} number_rooms 35".format(place.id)

        HBNBCommand().onecmd(line)
        updated_place = models.storage.all()["Place.{}".format(place.id)]
        self.assertEqual(updated_place.number_rooms, 35)
        self.assertEqual(type(updated_place.number_rooms), int)

    def test_update_place_check_str_type_attr(self):
        """test_update_place_check_str_type_attr"""
        place = Place()
        line = "update Place {} name Amizmiz".format(place.id)

        HBNBCommand().onecmd(line)
        updated_place = models.storage.all()["Place.{}".format(place.id)]
        self.assertEqual(updated_place.name, "Amizmiz")
        self.assertEqual(type(updated_place.name), str)


if __name__ == "__main__":
    main()
