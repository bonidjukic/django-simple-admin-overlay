# Django Admin Shortcuts
**Lightweight Django app which displays simple overlay with admin links on the frontend pages.**

# Requirements

* Python (3.5)
* Django (1.10)

# Installation

Install using `pip`...

    pip install django-admin-shortcuts

Add `'admin_shortcuts'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'admin_shortcuts',
    )

Enable `admin_shortcuts` middleware.

    MIDDLEWARE = [
        ...
        'admin_shortcuts.middleware.AdminLayerMiddleware',
    ]

# Configuration

You can change a limited number of options by adding `ADMIN_SHORTCUTS_CONFIG` dictionary to your `settings.py`.

Default values are:

    ADMIN_SHORTCUTS_CONFIG = {
        'TOOLBAR_POSITION': 'top', # top, right, bottom, left
        'DEFAULT_STATE': 'open', # open, closed
    }

# Common issues

Make sure that you're logged in as an authenticated user and have access to the admin interface, i.e. that your `User` instance has `is_authenticated=True` and `is_staff=True`

# To-do list

- Ability to manually exclude an app or a model via `settings.py`
- Persist toolbar state (open, closed) via cookie or local storage