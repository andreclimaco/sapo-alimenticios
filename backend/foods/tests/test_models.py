from django.test import TestCase
from django.db import models
from foods.models import Food


class FoodModelTest(TestCase):

    def test_name(self):
        field = Food._meta.get_field('name')
        self.assertEquals(isinstance(field, models.CharField), True)
        self.assertEquals(field.verbose_name, 'name')
        self.assertEquals(field.max_length, 255)
        self.assertEquals(field.unique, True)

    def test_quantity(self):
        field = Food._meta.get_field('quantity')
        self.assertEquals(isinstance(field, models.PositiveIntegerField), True)
        self.assertEquals(field.verbose_name, 'quantity')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.default, 0)

    def test_proteins(self):
        field = Food._meta.get_field('proteins')
        self.assertEquals(isinstance(field, models.PositiveIntegerField), True)
        self.assertEquals(field.verbose_name, 'proteins')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.default, 0)

    def test_carbohydrates(self):
        field = Food._meta.get_field('carbohydrates')
        self.assertEquals(isinstance(field, models.PositiveIntegerField), True)
        self.assertEquals(field.verbose_name, 'carbohydrates')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.default, 0)

    def test_fats(self):
        field = Food._meta.get_field('fats')
        self.assertEquals(isinstance(field, models.PositiveIntegerField), True)
        self.assertEquals(field.verbose_name, 'fats')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.default, 0)

    def test_created_at(self):
        field = Food._meta.get_field('created_at')
        self.assertEquals(isinstance(field, models.DateTimeField), True)
        self.assertEquals(field.auto_now_add, True)

    def test_updated_at(self):
        field = Food._meta.get_field('updated_at')
        self.assertEquals(isinstance(field, models.DateTimeField), True)
        self.assertEquals(field.auto_now, True)

    def test_object_name(self):
        Food.objects.create(name='Azeite', quantity=100,
                            proteins=2, carbohydrates=3, fats=40)
        food = Food.objects.get(id=1)
        expected_object_name = food.name
        self.assertEquals(expected_object_name, str(food))

    # def teste_name_max_length(self):
    #     food = Food.objects.get(id=1)
    #     max_length = food._meta.get_field('name').max_length
    #     self.assertEquals(max_length, 255)

    # def test_date_of_death_label(self):
    #     author = Author.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_death').verbose_name
    #     self.assertEquals(field_label, 'died')

    # def test_first_name_max_length(self):
    #     author = Author.objects.get(id=1)
    #     max_length = author._meta.get_field('first_name').max_length
    #     self.assertEquals(max_length, 100)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author = Author.objects.get(id=1)
    #     expected_object_name = f'{author.last_name}, {author.first_name}'
    #     self.assertEquals(expected_object_name, str(author))

    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(), '/catalog/author/1')
