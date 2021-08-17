from django.db import models

# create category model
class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_catagories():
       return Category.objects.all()


    # changing catagory name in product
    def __str__(self):
      return self.name
