# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . models import UserProfile,Roles
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Roles)

