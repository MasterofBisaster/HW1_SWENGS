from django.db import models


class OEM(models.Model):

    name = models.TextField()

    class Meta:
        verbose_name_plural = "OEMs"

    def __str__(self):
        return self.name


class CPU(models.Model):
    CHOICES = (
        ('u', 'Unlocked'),
        ('l', 'Locked')
    )

    name = models.TextField()
    coremultiplier = models.CharField(max_length=1, choices=CHOICES)
    release_date = models.DateField()
    price = models.PositiveIntegerField(help_text="in Euros")
    manufacturer = models.ForeignKey(OEM, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "CPUs"

    def __str__(self):
        return self.name
    # TODO: implement __str__ method



