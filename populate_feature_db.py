"""
Script to be redirected to the django shell
in order to create several columns of dummy
data inside Feature model.
"""

from feature_list.models import FeatureModel
from datetime import datetime

f1 = FeatureModel(date=datetime(2010, 1, 1, 1, 1, 1),
                  description="Internationalization of pages is now available "
                  "in: English, Mandarin, Klingon, Shoggothese",
                  lead_developer="Alan Chang",
                  title="Add additional langauges",
                  )
f1.save()

f2 = FeatureModel(date=datetime(2010, 1, 1, 1, 1, 2),
                  description="Single Sign-on is now supported via okta."
                  "You will be redirected to the correct identity provider "
                  "after identifying them",
                  lead_developer="Alan Chang",
                  title="SSO 1.0",
                  url="/sso/login")

f2.save()

f3 = FeatureModel(date=datetime(2010, 1, 1, 1, 1, 3),
                  description="Upon signing up to this website, "
                  "users will acquire powers such as telekinesis, "
                  "invisibility and Very Loud sneezes",
                  lead_developer="Patrik Outericky",
                  title="sudo superhero",
                  )

f3.save()
