from datetime import datetime
from functools import wraps

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserActiveTime(models.Model):
    user = models.ForeignKey(User)
    last_active = models.DateTimeField()

def _user_decorator(create_user):
    """Force a user's 'last active' time
    to be always set when the user is registered.
    """
    @wraps(create_user)
    def register_last_active(*args, **kwargs):
        user = create_user(*args, **kwargs)
        active_time = UserActiveTime(user=user,
                                     last_active=user.date_joined)
        active_time.save()
        return user, active_time

    return register_last_active

create_user = _user_decorator(User.objects.create_user)
