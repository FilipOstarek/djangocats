from django.db import models

# Create your models here.
from django.db import models

def fotky(instance, filename):
    return "cats/" + str(instance.id) + "/fotka/" + filename

class Species(models.Model):
    #Druhy
    jmeno_druhu = models.CharField(max_length=50, unique=True, verbose_name="Druh kočky",
                            help_text='Zadejte prosím druh kočky, popřípadě OwO pokud není známo')
    class Meta:
        ordering = ["jmeno_druhu"]
    def __str__(self):
        return self.jmeno_druhu

class Description_of_the_cat(models.Model):
    #popisek kočky
    '''
    jmeno = Column(String(50), nullable=True)
    vek = Column(Integer)
    vaha = Column(Integer) #kg
    samotny_popis = Column(Text)
    '''
    jmeno = models.CharField(max_length=50, verbose_name="Jméno", blank=True)
    vek = models.IntegerField(verbose_name="Roky Kočky", blank=True)
    vaha = models.IntegerField(verbose_name="Váha", blank=True)
    popisek = models.CharField(max_length=500, verbose_name="popisek", blank=True)

    species = models.ManyToManyField(Species, help_text='Vyberte druh kočky')

    class Meta:
        ordering = ["jmeno"]
    def __str__(self):
        return f"{self.jmeno}"

class Photo(models.Model):
    #Fotka
    nazev_fotky = models.CharField(max_length=50, blank=True, null=True, verbose_name="Název fotky")
    popisek_fotky = models.CharField(max_length=500, blank=True, null=True, verbose_name="popisek fotky")
    fotka = models.ImageField(upload_to=fotky, blank=True, null=True, verbose_name="Fotka")
    '''
    id = Column(Integer, primary_key=True)
    url = Column(String(150), unique=True, nullable=False)
    nazev_fotky = Column(String(length=100))
    '''
    class Meta:
        ordering = ["nazev_fotky"]
    def __str__(self):
        """ Textová reprezentace objektu """
        '''
        return f"{self.title}, ({self.type})"
        '''
        return f"{self.nazev_fotky}"