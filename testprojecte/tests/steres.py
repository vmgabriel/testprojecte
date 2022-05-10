"""testprojecte - Steres - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from testprojecte.models.steres import Steres


class SteresTestCase(TestCase):
    """Steres test cases"""
    fixtures = ["preducts.json", "steres.json"]

    def test_should_get_datas(self):
        steres = Steres.objects.all()
        self.assertEqual(steres.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        steres_name = Steres.objects.filter(name__icontains="Update")
        self.assertEqual(steres_name.count(), 3)
        steres_description = Steres.objects.filter(description__icontains="Update")
        self.assertEqual(steres_description.count(), 3)
        steres_address = Steres.objects.filter(address__icontains="Update")
        self.assertEqual(steres_address.count(), 3)
        steres_active = Steres.objects.filter(active=True)
        self.assertEqual(steres_active.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        steres_name = Steres.objects.filter(name__icontains="2")
        self.assertEqual(steres_name.count(), 0)
        steres_description = Steres.objects.filter(description__icontains="2")
        self.assertEqual(steres_description.count(), 0)
        steres_address = Steres.objects.filter(address__icontains="2")
        self.assertEqual(steres_address.count(), 0)
        steres_active = Steres.objects.filter(active=False)
        self.assertEqual(steres_active.count(), 0)

    def test_get_data(self):
        pk = 2
        steres = Steres.objects.get(pk=pk)
        self.assertIsInstance(steres, (Steres,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Steres.objects.get(pk=pk)
        data.name = "Update"
        data.description = "Update"
        data.address = "Update"
        data.active = True

        data.save()
        self.assertEqual(data.name, "Update")
        self.assertEqual(data.description, "Update")
        self.assertEqual(data.address, "Update")
        self.assertEqual(data.active, True)

    def test_create_data(self):
        new_object = {
            "name": "Update",
            "description": "Update",
            "address": "Update",
            "active": True,
            "preducts_sc_id": 1
        }
        data = Steres(**new_object)
        data.save()
        pk = data.pk
        datas = Steres.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        steres = Steres.objects.get(pk=pk)
        steres.delete()
        datas = Steres.objects.all().count()
        self.assertEqual(datas, 2)