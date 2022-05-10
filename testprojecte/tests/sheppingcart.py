"""testprojecte - Sheppingcart - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from testprojecte.models.sheppingcart import Sheppingcart


class SheppingcartTestCase(TestCase):
    """sheppingCart test cases"""
    fixtures = ["user.json","preducts.json", "sheppingcart.json"]

    def test_should_get_datas(self):
        sheppingcart = Sheppingcart.objects.all()
        self.assertEqual(sheppingcart.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        sheppingcart_ree_mame = Sheppingcart.objects.filter(ree_mame__icontains="Update")
        self.assertEqual(sheppingcart_ree_mame.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        sheppingcart_ree_mame = Sheppingcart.objects.filter(ree_mame__icontains="2")
        self.assertEqual(sheppingcart_ree_mame.count(), 0)

    def test_get_data(self):
        pk = 2
        sheppingcart = Sheppingcart.objects.get(pk=pk)
        self.assertIsInstance(sheppingcart, (Sheppingcart,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Sheppingcart.objects.get(pk=pk)
        data.ree_mame = "Update"

        data.save()
        self.assertEqual(data.ree_mame, "Update")

    def test_create_data(self):
        new_object = {
            "ree_mame": "Update",
            "user_sc_id": 1,
            "preducts_sc_id": 1
        }
        data = Sheppingcart(**new_object)
        data.save()
        pk = data.pk
        datas = Sheppingcart.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        sheppingcart = Sheppingcart.objects.get(pk=pk)
        sheppingcart.delete()
        datas = Sheppingcart.objects.all().count()
        self.assertEqual(datas, 2)