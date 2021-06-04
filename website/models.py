from django.db import models

# Create your models here.

class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:

        abstract = True


class Categorie(Base):
    nom = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):

        return self.nom

class DrinkMenu(Base):
    nom = models.CharField(max_length=100) 
    description = models.TextField()
    prix = models.FloatField()
    image = models.FileField(upload_to="drink_menu_image")
    categorie = models.ForeignKey("Categorie", related_name="drinkcategorie", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'DrinkMenu'
        verbose_name_plural = 'DrinkMenu'

    def __str__(self):

        return self.nom

class Website(Base):
    logo = models.FileField()
    nom_site = models.CharField(max_length=100)
    copyright = models.CharField(max_length=100)
    titre_contact = models.CharField(max_length=100)
    description_contact = models.TextField()
    titre_about = models.CharField(max_length=100)
    image_about = models.FileField(upload_to="image_about")
    description_about = models.TextField()

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):

        return self.nom_site
    
class About(Base):
    titre = models.CharField(max_length=100)
    sous_titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to="image")

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):

        return self.titre

class SpecialItems(Base):
    image = models.FileField(upload_to="image_items")
    titre = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'SpecialItems'
        verbose_name_plural = 'SpecialItems'

    def __str__(self):

        return self.titre

class Contact(Base):
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):

        return self.nom