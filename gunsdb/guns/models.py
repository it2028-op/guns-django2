from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


def meadia_attachment_path(instance, filename):
    return "film/" + str(instance.gun.id) + "/attachments/" + filename


class Type(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Označení typu",
                            help_text="Zadejte název typu")
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name="Popis a charakteristika typu")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Název firmy/výrobce",
                            help_text="Zadejte název výrobce nebo firmy")
    address = models.CharField(max_length=150, verbose_name="Adresa firmy/výrobce",
                               help_text='Zadejte adresu firmy nebo výrobce, pokud je známá.')
    about = models.TextField(max_length=300, blank=True, null=True,
                             verbose_name="O vyrábějící firmě nebo výrobci zbraně")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Gun(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Označení zbraně",
                            help_text="Zadejte označení zbraně")
    length = models.FloatField(verbose_name="Celková délka zbraně (mm)",
                               help_text="Zadejte délku zbraně v milimetrech",
                               validators=[MinValueValidator(0.1), MaxValueValidator(2000.0)])
    barrel_length = models.FloatField(verbose_name="Délka hlavně zbraně (mm)",
                                      help_text="Zadejte délku hlavně zbraně v milimetrech",
                                      validators=[MinValueValidator(0.1), MaxValueValidator(2000.0)])
    weight = models.FloatField(verbose_name="Celková hmotnost zbraně (g)",
                               validators=[MinValueValidator(0.1), MaxValueValidator(20000.0)],
                               help_text="Zadejte hmotnost zbraně v gramech")
    magazine = models.IntegerField(verbose_name="Celková kapacita obvyklého zásobníku",
                                   help_text="Zadejte množtví munice v základním zásobníku zbraně", default=1)
    description = models.TextField(max_length=300, blank=True, verbose_name="Popis zbraně",
                                   help_text="Popište tuto zbraň (historie, vlastnosti"
                                             ", zvláštnosti...)")
    type = models.ManyToManyField(Type, help_text='Vyberte typ zbraně')
    maker = models.ManyToManyField(Maker, help_text='Vyberte výrobce zbraně')

    rate = models.FloatField(default=5.0,
                             validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
                             null=True,
                             verbose_name="Hodnocení",
                             help_text="Prosím, ohodnoťte na stupnici 1-10")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, Hodnocení: {str(self.rate)}"

    def get_detail_url(self):
        return reverse('gun-detail', arg=[str(self.id)])


class Attachment(models.Model):
    title = models.CharField(max_length=300, verbose_name='Titul obrázku')
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=meadia_attachment_path, null=True, verbose_name="Soubor")
    TYPE_OF_ATTACHMENT = (
        ('image', 'Image'),
        ('video', 'Video')
    )
    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True,
                            default='image', help_text='Vyberte typ přílohy(obrázek nebo video)',
                            verbose_name="Typ přílohy")
    gun = models.ForeignKey(Gun, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-last_update", "type"]

        def __str__(self):
            return f"{self.title} - {self.type} - {str(self.last_update)}"
