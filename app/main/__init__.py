

from flask import Blueprint

main = Blueprint('main', __name__)
print "main-->blueprint"

import views