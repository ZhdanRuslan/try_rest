from django.db import models
from django.db.models import Count


class Category(models.Model):
    name = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    child = models.ForeignKey('self', on_delete=models.PROTECT, default=None, null=True, blank=True,
                              related_name='nested_category')
    amount_items = models.IntegerField(blank=True, default=0, null=True)
    amount_inner_categories = models.IntegerField(blank=True, default=0, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        items = self.item_set.all().count()

        self.amount_items = items + 1
        cat = None
        try:
            cat = Category.objects.get(name=self.child.name)
        except Exception as exc:
            pass

        child_amount = Category.objects.aggregate(num_cat=Count('child'))
        if cat is not None:
            cat.amount_inner_categories = child_amount['num_cat'] + 1
            cat.save()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'name: {self.name}'


class Item(models.Model):
    name = models.CharField(blank=True, max_length=255)
    owner = models.CharField(blank=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.FloatField()
    description = models.TextField(blank=True, max_length=255)
    photo = models.ImageField(blank=True, null=True)
    amount_views = models.IntegerField(blank=True, default=None, null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        Category.objects.get(name=self.category.name).save()
        super().save(force_insert, force_update, using, update_fields)
