from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    phone = models.IntegerField(_("phone"))

    

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return self.name

  