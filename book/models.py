from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    '''A company that ppublishes books.'''
    name = models.CharField(max_length = 50, help_text ='The name of the publisher.')
    website = models.URLField(help_text = "The Publisher's website")
    email = models.EmailField(help_text = "The Publisher's email address.") 


    def __str__(self):
        return self.name
    
class Bookr(models.Model):
    """A Published book."""
    title = models.CharField(max_length = 70, help_text = 'The title of the book.')
    publication_date = models.DateField(verbose_name="Date the booj was published.")
    isbn = models.CharField(max_length = 20, verbose_name = "ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through = 'BookContributor')
    def __str__(self):
        return self.title

class Contributor(models.Model):
    """A contributor to a Book, e.g. author, editor, co-author."""
    first_names = models.CharField(max_length = 50, help_text= "The contributor's first name or names.")
    last_names = models.CharField(max_length = 50, help_text = "The contributor's last name or names.")
    email = models.EmailField(help_text = "The contact email for the contributor.")
    
    def __str__(self):

        return self.first_names

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR    = 'EDITOR', "Editor"
    book = models.ForeignKey(Bookr, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this dcontributor had in the book.",\
                            choices=ContributionRole.choices,  max_length=20)
class Review(models.Model):
    content = models.TextField(help_text = 'The review text.')
    rating = models.IntegerField(help_text = 'The rating the reviewer has given' )
    date_created = models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created.')
    date_edited = models.DateTimeField(null = True, help_text='The date and the time the review was edited.')
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, help_text='The book this review is for.')


class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length= 30)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
class DriveLicense(models.Model):
    person = models.OneToOneField(Person, on_delete = models.CASCADE)
    licence_number = models.CharField(max_length =20)

  