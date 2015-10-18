from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed

from users.models import UserActiveTime
from .models import FeatureModel
# Create your views here.


@login_required
def changeset_route(request, *args, **kwargs):
    """
    Send to the correct view function based on method
    Note that a more robust implementation would be using,
    for example django REST or a decorator
    """
    if request.method == "GET":
        user = request.user
        return read_changesets(request, user, *args, **kwargs)
    elif request.method == "POST":
        return write_changesets(request, *args, **kwargs)
    else:
        return HttpResponseNotAllowed("Only GET and POST available",
                                      ["GET", "POST"])


def read_changesets(request, user):
    active_time_row = UserActiveTime.objects.get(user=user)
    last_seen, now = active_time_row.last_active, datetime.now()

    new_features = FeatureModel.objects.filter(date__gt=last_seen,
                                               date__lt=now)

    update_last_seen = now
    active_time_row.last_active = update_last_seen
    active_time_row.save()

    return render(request, "feature_list/changesets.html",
                  {"features": new_features})

def write_changesets(request):
    pass
