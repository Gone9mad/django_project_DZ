from django.core.management import BaseCommand
from catalog.models import Product, Category
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстур с категориями
        with open('fixtur/category_data.json', 'r', encoding='utf-8') as file:
            categories = json.load(file)
        return categories

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстур с продуктами
        with open('fixtur/products_data.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        return products

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()

        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category["fields"]["name"],
                         description=category["fields"]["description"],
                         pk=category["pk"]
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        image=product["fields"]["image"],
                        purchase_price=product["fields"]["purchase_price"],
                        created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"],
                        pk=product["pk"],
                        # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=category["pk"],)
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)