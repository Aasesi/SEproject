import unittest
from unittest.mock import MagicMock
from System import System


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_register(self):
        self.system.user_database.add_user = MagicMock()
        self.system.register("John", "John", "Doctor", "John", "password")
        self.system.user_database.add_user.assert_called_with("John", "John", "Doctor", "John", "password")

    def test_login_valid_credentials(self):
        self.system.user_database.validate = MagicMock(return_value=1)
        self.system.user_database.get_current_user = MagicMock(return_value=[("John", "John", "Doctor")])
        self.assertTrue(self.system.login("John", "password"))
        self.assertEqual(self.system.current_user.name, "John")
        self.assertEqual(self.system.current_user.surname, "John")
        self.assertEqual(self.system.current_user.userType, "Doctor")

    def test_login_invalid_credentials(self):
        self.system.user_database.validate = MagicMock(return_value=0)
        self.assertFalse(self.system.login("John", "password"))

    def test_change_patient_code(self):
        self.system.user_database.assign_csv_code = MagicMock(return_value=True)
        self.assertTrue(self.system.change_patient_code("johndoe", 12345))
        self.system.user_database.assign_csv_code.assert_called_with("johndoe", "12345")

    def test_get_database_data(self):
        self.system.patient_database.load_data = MagicMock(return_value=True)
        self.system.patient_database.get_column_names = MagicMock(return_value=["Patient_code", "HighBP", "HighChol",
                                                                                "CholCheck", "BMI", "Smoker", "Stroke",
                                                                                "Diabetes", "PhysActivity", "Fruits",
                                                                                "Veggies", "HvyAlcoholConsump",
                                                                                "AnyHealthcare", "NoDocbcCost",
                                                                                "GenHlth",
                                                                                "MentHlth", "PhysHlth", "DiffWalk",
                                                                                "Sex",
                                                                                "Age", "Education", "Income"])


if __name__ == '__main__':
    unittest.main()
