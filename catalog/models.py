from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта", **NULLABLE
    )
    image = models.ImageField(
        upload_to="product/image", verbose_name="Изображение", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Укажите цену"
    )
    created_at = models.DateField(
        **NULLABLE,
        verbose_name="Дата создания записи",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        **NULLABLE,
        verbose_name="Дата изменения записи",
        help_text="Укажите дату изменения",
    )


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


