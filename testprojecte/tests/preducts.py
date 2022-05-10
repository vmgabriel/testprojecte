"""testprojecte - Preducts - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from testprojecte.models.preducts import Preducts


class PreductsTestCase(TestCase):
    """Preducts test cases"""
    fixtures = [ "preducts.json"]

    def test_should_get_datas(self):
        preducts = Preducts.objects.all()
        self.assertEqual(preducts.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        preducts_name = Preducts.objects.filter(name__icontains="Update")
        self.assertEqual(preducts_name.count(), 3)
        preducts_description = Preducts.objects.filter(description__icontains="Update")
        self.assertEqual(preducts_description.count(), 3)
        preducts_active = Preducts.objects.filter(active=True)
        self.assertEqual(preducts_active.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        preducts_name = Preducts.objects.filter(name__icontains="2")
        self.assertEqual(preducts_name.count(), 0)
        preducts_description = Preducts.objects.filter(description__icontains="2")
        self.assertEqual(preducts_description.count(), 0)
        preducts_active = Preducts.objects.filter(active=False)
        self.assertEqual(preducts_active.count(), 0)

    def test_get_data(self):
        pk = 2
        preducts = Preducts.objects.get(pk=pk)
        self.assertIsInstance(preducts, (Preducts,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Preducts.objects.get(pk=pk)
        data.name = "Update"
        data.description = "Update"
        data.active = True

        data.save()
        self.assertEqual(data.name, "Update")
        self.assertEqual(data.description, "Update")
        self.assertEqual(data.active, True)

    def test_create_data(self):
        new_object = {
            "name": "Update",
            "description": "Update",
            "active": True
        }
        data = Preducts(**new_object)
        data.save()
        pk = data.pk
        datas = Preducts.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        preducts = Preducts.objects.get(pk=pk)
        preducts.delete()
        datas = Preducts.objects.all().count()
        self.assertEqual(datas, 2)