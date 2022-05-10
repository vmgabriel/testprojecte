"""testprojecte - User - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from testprojecte.models.user import User


class UserTestCase(TestCase):
    """User test cases"""
    fixtures = [ "user.json"]

    def test_should_get_datas(self):
        user = User.objects.all()
        self.assertEqual(user.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        user_name = User.objects.filter(name__icontains="Update")
        self.assertEqual(user_name.count(), 3)
        user_nick = User.objects.filter(nick__icontains="Update")
        self.assertEqual(user_nick.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        user_name = User.objects.filter(name__icontains="2")
        self.assertEqual(user_name.count(), 0)
        user_nick = User.objects.filter(nick__icontains="2")
        self.assertEqual(user_nick.count(), 0)

    def test_get_data(self):
        pk = 2
        user = User.objects.get(pk=pk)
        self.assertIsInstance(user, (User,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = User.objects.get(pk=pk)
        data.name = "Update"
        data.nick = "Update"

        data.save()
        self.assertEqual(data.name, "Update")
        self.assertEqual(data.nick, "Update")

    def test_create_data(self):
        new_object = {
            "name": "Update",
            "nick": "Update"
        }
        data = User(**new_object)
        data.save()
        pk = data.pk
        datas = User.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        user = User.objects.get(pk=pk)
        user.delete()
        datas = User.objects.all().count()
        self.assertEqual(datas, 2)