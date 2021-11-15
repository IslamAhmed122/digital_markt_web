from django.db import models
from phone_field import PhoneField
# Create your models here.
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

from django.shortcuts import redirect

from django.utils.text import slugify
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _



# Create your models here.

class web(models.Model):
    title =models.CharField (max_length=200,verbose_name=_("عنوان الموقع "))
    icon = models.ImageField(verbose_name=_("ايقوتة الموقع "),upload_to="img/")
    logo = models.ImageField(verbose_name=_("اللوجو"),upload_to="img/")
    
        
    def __str__(self):
        return str(self.title)
def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(web,self).save(*args, **kwargs)  # save
    


class imagelist(models.Model):
    name = models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/")
    description=models.TextField(max_length=2000)
    
    def __str__(self):
        return str(self.name)








class Aboutus(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("العنوان "))
    description=models.TextField(max_length=2000,verbose_name=_("الوصف"))
   
    imageone=models.ImageField(verbose_name=_("صوره في عنا"),upload_to="img/")
    alt=models.CharField(max_length=100)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    
    def __str__(self):
        return str(self.title)



def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(Aboutus,self).save(*args, **kwargs)  # save



class Service(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("خدمتنا"))
    descriptionservice=models.TextField(max_length=3000,verbose_name=_(",وصف الخدمات"))
    image=models.ImageField(upload_to="img/")
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
   
    def __str__(self):
        return str(self.title)


def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(Service,self).save(*args, **kwargs)  # save


class whychooseus(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("العنوان"))
    description=models.TextField(max_length=3000,verbose_name=_("الوصف"))
    number=models.IntegerField()
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    
    def __str__(self):
        return str(self.title)



def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(whychooseus,self).save(*args, **kwargs)  # save



    


class OurPortfolio(models.Model):
    title=models.CharField(max_length=300,verbose_name=_("العنوان"))
    
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    
    def __str__(self):
        return str(self.title)

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(OurPortfolio,self).save(*args, **kwargs)  # save


class imagelistportfolio(models.Model):
    name = models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/")
    alt=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)





class Team(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    image=models.ImageField(upload_to="img/")
    alt=models.CharField(max_length=50)
    fac_link=models.URLField(max_length=300, verbose_name=_("facbook"),null=True)
    twi_link=models.URLField(max_length=300, verbose_name=_("twitter"),null=True)
    linked_link=models.URLField(max_length=300, verbose_name=_("gmail"),null=True)
    ins_link=models.URLField(max_length=300, verbose_name=_("instgram"),null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )

    
    def __str__(self):
        return str(self.name)

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(Team,self).save(*args, **kwargs)  # save   


class ourclients(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    image=models.ImageField(upload_to="img/")
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )


    
    def __str__(self):
        return str(self.title)

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(ourclients,self).save(*args, **kwargs)  # save






class contactus(models.Model):
    title=models.CharField(max_length=200)
    map=models.URLField(max_length=300)
    address=models.CharField(max_length=200)
    linkcontact=models.URLField(max_length=300)
    phone_number =PhoneField(blank=True, help_text='Contact phone number')
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    gmail=models.URLField(max_length=100)


    
    def __str__(self):
        return str(self.title)





def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(contactus,self).save(*args, **kwargs)  # save
















class footer(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    titletwo=models.CharField(max_length=200)
    titlethre=models.CharField(max_length=200)
    phone_number =PhoneField(blank=True, help_text='Contact phone number')
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )

    
    def __str__(self):
        return str(self.title)


    

    
def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(footer,self).save(*args, **kwargs)  # save




class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)
    
    

    def __str__(self):
        return str(self.email)




