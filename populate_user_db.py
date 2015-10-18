from .users.models import create_user

u1, active_time1 = create_user(username="ahchang", password="password")
(u1.save(), active_time1.save())

u2, active_time2 = create_user(username="poutersky", password="password")

(u2.save(), active_time2.save())
