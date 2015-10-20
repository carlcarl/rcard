RCard
========================

Below you will find basic setup and deployment instructions for the rcard
project. To begin you should have the following applications installed on your
local development system::

- Python >= 3.0
- Django >= 1.8
- Postgres >= 9.4

Getting Started
------------------------

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    mkvirtualenv rcard
    $VIRTUAL_ENV/bin/pip install -r $PWD/requirements/dev.txt

Then create a local settings file and set your ``DJANGO_SETTINGS_MODULE`` to use it::

    cp rcard/settings/local.example.py rcard/settings/local.py
    echo "export DJANGO_SETTINGS_MODULE=rcard.settings.local" >> $VIRTUAL_ENV/bin/activate
    echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

Exit the virtualenv and reactivate it to activate the settings just changed::

    deactivate
    workon rcard

Create the Postgres database and run the initial syncdb/migrate::

    python manage.py makemigrations waterfall_wall
    python manage.py migrate

You should now be able to run the development server::

    python manage.py runserver

