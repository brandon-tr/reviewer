from __future__ import unicode_literals

from django.db import models
from ..loginreg .models import User
# Create your models here.
class CatManager(models.Manager):
    def addCat(self, postData, sessionData):
        result = {"status":True, "error":[]}
        if not postData['name']:
            result['status'] = False
            result['error'].append("You must have a name for your cat")
        if not postData['age']:
            result['status'] = False
            result['error'].append("You must have an age for your cat")
        if result['status'] == True:
            Cat.objects.create(
                name = postData['name'],
                age = postData['age'],
                user_id = User.objects.get(id = sessionData['id']).id
            )
        return result
    def addLike(self, sessionData, cat_id):
        Like.objects.create( cat_id = cat_id )
    def UpdateInfo(self, postData, cat_id):
        Cat.objects.filter(id = cat_id).update(
        name = postData['name'],
        age = postData['age']
        )
class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    user = models.ForeignKey(User, related_name = "user")
    objects = CatManager()
class Like(models.Model):
    cat = models.ForeignKey(Cat, related_name="like")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CatManager()