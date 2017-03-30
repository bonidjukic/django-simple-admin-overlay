# Django Simple Admin Overlay

**Lightweight Django app which displays simple overlay with admin links on the frontend pages.**

Django Simple Admin Overlay replaces the need to manually append `/admin` to the browser's URL bar or to bookmark the administration link during the development of Django projects.

Version: 0.1

# Screenshots

### Position: top, state: open

![Top Open Toolbar](docs/img/django_simple_admin_overlay_top_open.png?raw=true "Top Open Toolbar")

### Position: top, state: closed

![Top Closed Toolbar](docs/img/django_simple_admin_overlay_top_closed.png?raw=true "Top Closed Toolbar")

# Requirements

* Python (3.5)
* Django (1.10)

Currently tested only on the above noted versions of Python and Django. Will test further with older versions and update the list.

# Installation

Install using `pip`

    pip install django-simple-admin-overlay

Add `'simple_admin_overlay'` to your `INSTALLED_APPS` setting

    INSTALLED_APPS = (
        ...
        'simple_admin_overlay',
    )

Enable `simple_admin_overlay` middleware

    MIDDLEWARE = [
        ...
        'simple_admin_overlay.middleware.SimpleAdminOverlayMiddleware',
    ]

# Configuration

You can change a limited number of options by adding `SIMPLE_ADMIN_OVERLAY_CONFIG` dictionary to your `settings.py`.

Default values are:

    SIMPLE_ADMIN_OVERLAY_CONFIG = {
        'OVERLAY_POSITION': 'top', # top, right, bottom, left
        'DEFAULT_STATE': 'open', # open, closed
    }

# Common issues

Make sure that you're logged in as an authenticated user and have access to the admin interface, i.e. that your `User` instance has `is_authenticated=True` and `is_staff=True`

# To-do list

- Add `DEVELOPMENT_MODE` option which would depend on the `DEBUG` setting
- Ability to manually exclude an app or a model via `settings.py`
- Persist toolbar state (open, closed) via cookie or local storage