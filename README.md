# Django Case Insensitive Field


Django Case Insensitive Field is used to make Django Model Field case insensitive - by default Django can't do this. 

Let's assume you have a `username`  field on your `UserModel` which ofcourse would require `username` to be unique accross the `table` but to Django `abc` is different from `ABC` because it is case sensitive (meaning: users can use the same username but with different case).

Look at the example below:

```python
from django.db import models

class UserModel(models.Model):

    username = models.CharField(max_length=16, unique=True)



user1 = UserModel(username='user1')

user1.save()  # will go through

user2 = UserModel(username='User1') # will still go through

user2.save()  # will go through


```



## Using Django Case Insensitive Model

To make Django Model Field insensitive, you can use the code below:

No need for installation ot inclusion in app.


```python

# fields.py

from django.db.models import CharField

from django_case_insensitive_field import CaseInsensitiveFieldMixin


class CaseInsensitiveCharField(CaseInsensitiveFieldMixin, CharField):
    """[summary]
    Makes django CharField case insensitive \n
    Extends both the `CaseInsensitiveMixin` and  CharField \n
    Then you can import 
    """

    def __init__(self, *args, **kwargs):

        super(CaseInsensitiveMixin, self).__init__(*args, **kwargs) 


```

```python

# models.py

from .fields import CaseInsensitiveCharField


class UserModel(models.Model):

    username = CaseInsensitiveCharField(max_length=16, unique=True)

user1 = UserModel(username='user1')

user1.save()  # will go through


user2 = UserModel(username='User1') 

user2.save() # will not go through


```


## Dependencies

Holla! No dependecy. Lightweight!
