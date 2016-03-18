
from flask import Blueprint

auth = Blueprint('auth', __name__)
print "auth-->blueprint"

import forms, views

