from users.models import UserActiveTime
from .models import FeatureModel
import services

def check_newest(request):
    user = request.user

    if user.is_authenticated():
        features = FeatureModel.objects.all()

        last_seen = UserActiveTime.objects.get(user=user).last_active
        is_new_feature = services.is_new_feature(features, last_seen)
        return {"feature_changes": is_new_feature}
    else:
        # Just always have feature changes off
        # as a guest user, or a preset number
        # likely to increase conversion
        return {"feature_changes": False}
