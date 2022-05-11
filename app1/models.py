from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=25)

    def __str__(self):
        return self.soz


class Notogri(models.Model):
    xato_soz = models.CharField(max_length=25)
    togri = models.ForeignKey(Togri, on_delete=models.CASCADE)

    def __str__(self):
        return self.xato_soz
