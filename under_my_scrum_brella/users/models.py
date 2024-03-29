###########################################################################
#   Author: Silas Turner
#   Contributors: Ollie Barnes
#
#   The author has written all code in this file unless stated otherwise.
###########################################################################

from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    buddy_name = models.CharField(max_length=17)
    buddy_type = models.CharField(max_length=50)
    total_coins = models.IntegerField(default=0)
    total_xp = models.IntegerField(default=0)
    #Luke - tracks happiness and when it needs to decay
    buddy_happiness = models.FloatField(default=0.75)
    last_happiness_decay_time = models.DateTimeField(auto_now_add=True)


class Friend(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_user')
    pending_first_second= models.BooleanField()
    pending_second_first= models.BooleanField()
    friends = models.BooleanField(default=False)
    class Meta:
        unique_together = ["user1", "user2"]


################################################################
#   This model is used to create groups of which users can later
#   join/be assigned to
#
#   Author: Ollie Barnes
################################################################
class Group(models.Model):
    group_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.group_name


################################################################
#   This model connects the Group model to the User model,
#   allowing a User to be assigned to Group(s)
#
#   Author: Ollie Barnes
################################################################
class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)