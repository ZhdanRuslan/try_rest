from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from ..users.models import User


class Category(MPTTModel):
    """
        Category model with dependency django-mptt for calculate
        nested categories
    """
    name = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, default=None, null=True, blank=True,
                            related_name='nested_category')
    amount_items = models.IntegerField(blank=True, default=0)
    amount_inner_categories = models.IntegerField(blank=True, default=0)

    class MPTTMeta:
        parent_attr = 'parent'

    def __str__(self):
        return f'name: {self.name}'


class Item(models.Model):
    """
        Item model
    """
    name = models.CharField(blank=True, max_length=255)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.FloatField()
    description = models.TextField(blank=True, max_length=255)
    photo = models.ImageField(blank=True, null=True)
    amount_views = models.PositiveIntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.category is not None:
            cat = Category.objects.get(pk=self.category.id)
            cat.amount_items += 1
            cat.save()

        super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        if self.category is not None:
            cat = Category.objects.get(pk=self.category.id)
            cat.amount_items -= 1
            cat.save()
        return super().delete(using, keep_parents)


