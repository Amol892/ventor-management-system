from .models import User,UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

# signal receiver function for userprofile instance creatation
@receiver(post_save,sender=User)
def create_user(sender, instance, created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# signal receiver function to save userprofile
@receiver(post_save,sender=User)     
def save_user(sender,instance,**kwargs):
    instance.userprofile.save()