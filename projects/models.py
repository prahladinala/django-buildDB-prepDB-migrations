from django.db import models

import uuid
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


# CharField > Small field
    # max_length > sets the max length to the Field

# TextField > Larger Field
    # null=True > null is for database to know to accept empty field or not > True means allows empty field > False means doesnt
    # blank=True > blank is for django to know to accept empty field or not > True means allows empty field > False means doesnt

# DateTimeField > Date and Time Picker
    #auto_now_add > automatically creates date and time of model instance created

# UUIDField > 16 digit character
    #default=uuid.uuid4 > uuid4
    #unique > Means no other value in database can have this id
    #primary_key > use this as a primary_key or id
    # () as django creates an id by default , will be replaced by this id
    #editable > No one can edit this

# AFTER CREATING MODEL
#   WE HAVE TO PREPARE MIRATIONS AND MIGRATE > TO CREATE TABLES
#   AFTER PREPARING FOR MIGRATIONS > python manage.py makemigrations > WE CAN SEE A FOLDER migrations>0001_initial.py
#   THEN MIGRATE > python manage.py migrate > SO TABLES WILL BE CREATED IN DB

#   BUT WE CANNOT SEE THE TABLE IN ADMIN PANEL > 
#   WE NEED TO > REGISTER THE MODEL WITH ADMIN PANEL TO SEE > TABLE IN ADMIN PANEL
#   [APP FOLDER]>admin.py

# def __str__(self):
#         return self.title
# IS USED TO SHOW THE TITLE ON THE TABLE