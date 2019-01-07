# Django-Portfolio

Django-Portfolio is a little website about you and your awesome projects powered by Django. Also, it has a blog :)

## Installation

Install a virtual environment:

```bash
pip install virtualenv
```

Create a new virtual environment named like you want (`myvenv` in this example) in a directory, for example, next to the future project folder:

```bash

mkdir portfolio-project
cd portfolio-project
virtualenv myvenv
```

Activate the virtual environment:

```bash
source myvenv/bin/activate
```

Clone this repository to `portfolio-project` directory:

```bash
git clone git@github.com:MNV/django-portfolio.git
```
 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements:

```bash
cd django-portfolio
pip install -r requirements.txt
```

Add your project's local settings to `django-portfolio/portfolio/local_settings.py` file:
```bash
cd portfolio
nano local_settings.py
```

Paste these settings (for [PostgreSQL](https://www.postgresql.org/download/) in this example):

```
SECRET_KEY = 'your random secret key'

DEBUG = True  # or False for production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your db name',
        'USER': 'your user name',
        'PASSWORD': 'your db password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

Apply migrations (run this command in `django-portfolio` directory):

```bash
python manage.py migrate
```

Add static files (photo and resume) to `portfolio/static` directory. Make sure that they have the right name where they're in use (`photo.jpg` and `resume.pdf`).

Collect static files to `static` directory:

```bash
python manage.py collectstatic
```

Run the server:

```bash
python manage.py runserver
```

Go to [localhost](http://127.0.0.1:8000) and enjoy your portfolio website!

## Usage

To manage your new portfolio website you need to add superuser:

```bash
python manage.py createsuperuser
```

Go to [localhost/admin](http://127.0.0.1:8000/admin) and manage your jobs and blog posts.

That's it! :)

## Tests

To run tests:

```bash
python manage.py test
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
