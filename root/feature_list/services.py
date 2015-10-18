def update_last_seen(time_row, new_time):
    """
    Change the time to the new time
    """
    time_row.last_active = new_time
    return time_row

def features_since(features, first, second):
    """
    Grab all the features in between the
    first and second dates
    """
    return features.objects.filter(date__gt=first,
                                   date__lt=second)
