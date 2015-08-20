INSTALLATION

Granted you have python and django already installed
install django rest framework

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

i reccomend deleting the sqlite3 file and just resyncing
if you feel the need for it, its there.

build database
python manage.py syncdb
-create super user

run server
python manage.py runserver 

open up localhost:8000/index for docs