from unittest import TestCase, mock, main
from console import HBNBCommand
from io import StringIO
import uuid
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
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
        e = "Prints str repr of"
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

    def test_update_2_attrs(self):
        """test_update_2_attrs"""
        user = User()
        line = "update User {} first_name Hajar last_name ALX"

        HBNBCommand().onecmd(line.format(user.id))
        self.assertEqual(user.first_name, "Hajar")
        self.assertEqual(user.last_name, "")


class TestConsole_default(TestCase):
    """Test case of Console default"""

    file_path = "HA_YA_FILE.json"

    def setUp(self):
        """setUp method executes before each test case"""
        FileStorage._FileStorage__objects = {}

    def test_console_default_all(self):
        """test_console_default_all"""
        base1 = BaseModel()
        base2 = BaseModel()
        user1 = User()
        user1.first_name = "Yassine"
        user1.last_name = "Amzmiz"
        user2 = User()
        user2.first_name = "Hajar"
        user2.last_name = "Test"
        place1 = Place()
        place1.name = "Marrakech"
        place2 = Place()
        place2.name = "Sale"
        objs = models.storage.all()
        base_list = [obj.__str__() for obj in objs.values()
                     if obj.__class__.__name__ == "BaseModel"]
        user_list = [obj.__str__() for obj in objs.values()
                     if obj.__class__.__name__ == "User"]
        place_list = [obj.__str__() for obj in objs.values()
                      if obj.__class__.__name__ == "Place"]
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(base_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(user_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("Place.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(place_list), objs_str)

    def test_console_default_count(self):
        """test_console_default_count"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "0")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            base1 = BaseModel()
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            base2 = BaseModel()
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "2")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel {}".format(base2.id))
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(output.getvalue().strip(), "0")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            amenity = Amenity()
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(output.getvalue().strip(), "1")

    def test_console_default_show_no_exist_class(self):
        """test_console_default_show_no_exist_class"""
        expected = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('NoExist.show("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_show_no_exist_id(self):
        """test_console_default_show_no_exist_id"""
        expected = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_show_missing_id(self):
        """test_console_default_show_no_exist_id"""
        expected = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_show(self):
        """test_console_default_show"""
        user = User()
        user.email = "yassine1990@alx.com"
        user.password = "yassine@1991*$"
        usr_str = user.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('User.show("{}")'.format(user.id))
            self.assertEqual(usr_str, output.getvalue().strip())

    def test_console_default_destroy_no_exist_class(self):
        """test_console_default_destroy_no_exist_class"""
        expected = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('NoExist.destroy("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_destroy_no_exist_id(self):
        """test_console_default_destroy_no_exist_id"""
        expected = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.destroy("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_destroy_missing_id(self):
        """test_console_default_destroy_no_exist_id"""
        expected = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_destroy_instance(self):
        """test_console_default_destroy_instance"""
        user = User()
        user.email = "yassine1990@alx.com"
        user.password = "yassine@1991*$"
        HBNBCommand().onecmd('User.destroy("{}")'.format(user.id))
        objs = models.storage.all()
        self.assertNotIn("User.{}".format(user.id), objs.keys())

    def test_console_default_destroy(self):
        """test_console_default_show"""
        user1 = User()
        user2 = User()
        user3 = User()
        HBNBCommand().onecmd('User.destroy("{}")'.format(user1.id))
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "2")
        HBNBCommand().onecmd('User.destroy("{}")'.format(user2.id))
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "1")
        HBNBCommand().onecmd('User.destroy("{}")'.format(user3.id))
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "0")

    def test_console_default_update_no_exist_class(self):
        """test_console_default_update_no_exist_class"""
        expected = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('NoExist.update()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_missing_id(self):
        """test_console_default_update_missing_id"""
        expected = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_no_exist_id(self):
        """test_console_default_update_no_exist_id"""
        expected = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_attr_name_missing(self):
        """test_console_default_update_attr_name_missing"""
        expected = "** attribute name missing **"
        amenity = Amenity()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update("{}")'.format(amenity.id))
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_attr_value_missing(self):
        """test_console_default_update_attr_value_missing"""
        expected = "** value missing **"
        amenity = Amenity()
        id = amenity.id
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update("{}", "attr")'.format(id))
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_user_email(self):
        """test_console_default_update_user_email"""
        user = User()
        self.assertEqual(user.email, "")
        user_mail = "Yassine_kech@alx.com"
        cmd = 'User.update("{}", "email", {})'.format(user.id, user_mail)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(user.email, user_mail)

    def test_console_default_update_multiple_attrs(self):
        """test_console_default_update_multiple_attrs"""
        user = User()
        user_mail = "Yassine_kech@alx.com"
        user_pwd = "Y1990*$ssine"
        cmd = 'User.update("{}", "email", {}, "password", {})'
        HBNBCommand().onecmd(cmd.format(user.id, user_mail, user_pwd))
        self.assertEqual(user.email, "Yassine_kech@alx.com")
        self.assertEqual(user.password, "")

    def test_console_default_update_by_using_dict(self):
        """test_console_default_update_by_using_dict"""
        place = Place()
        amenity_list = [Amenity().id for i in range(4)]
        desc = "Hotel Hajar: Best place in the world"
        p_dict = {
                "name": "Hotel Hajar",
                "description": desc,
                "number_rooms": "1",
                "max_guest": 1,
                "latitude": "7589.201",
                "amenity_ids": amenity_list
                }
        cmd = 'Place.update("{}", {})'.format(place.id, p_dict)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(place.name, "Hotel Hajar")
        self.assertEqual(place.description, desc)
        self.assertEqual(place.number_rooms, 1)
        self.assertEqual(place.max_guest, 1)
        self.assertEqual(place.latitude, 7589.201)
        self.assertListEqual(place.amenity_ids, amenity_list)

    def test_console_default_update_by_dict_check_types(self):
        """test_console_default_update_by_dict_check_types"""
        place = Place()
        amenity_list = [Amenity().id for i in range(4)]
        desc = "Hotel Hajar: Best place in the world"
        p_dict = {
                "name": "Hotel Hajar",
                "description": desc,
                "max_guest": 1,
                "latitude": "7589.201",
                "number_rooms": "1",
                "amenity_ids": amenity_list
                }
        cmd = 'Place.update("{}", {})'.format(place.id, p_dict)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_console_default_update_by_using_empty_dict(self):
        """test_console_default_update_by_using_empty_dict"""
        review = Review()
        review.place_id = "xxxx-xxxx-xxxx-xxxx"
        review.user_id = "yyyy-yyyy-yyyy-yyyy"
        review.text = "Thank you Hajar <3"
        cmd = 'Review.update("{}", {})'.format(review.id, {})
        HBNBCommand().onecmd(cmd)
        self.assertEqual(review.place_id, "xxxx-xxxx-xxxx-xxxx")
        self.assertEqual(review.user_id, "yyyy-yyyy-yyyy-yyyy")
        self.assertEqual(review.text, "Thank you Hajar <3")

    def test_console_default_update_by_using_dict_special_characters(self):
        """test_console_default_update_by_using_dict_special_characters"""
        review = Review()
        review.place_id = "xxxx-xxxx-xxxx-xxxx"
        review.user_id = "yyyy-yyyy-yyyy-yyyy"
        r_dict = {
                "text": "Thank you Hajar <3 :)"
                }
        cmd = 'Review.update("{}", {})'.format(review.id, r_dict)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(review.text, "Thank you Hajar <3 :)")


if __name__ == "__main__":
    main()
