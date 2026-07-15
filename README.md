# Django Login Portal

> A simple user authentication portal built with Django's built-in auth system — register, log in, log out, and land on a protected dashboard page.

## Overview

Django Login Portal is a small Django project that demonstrates a complete authentication flow using Django's built-in `django.contrib.auth`. Users can register a new account, log in, and log out; the home page is gated behind login and renders a styled dashboard template. It's intentionally minimal — a clean reference/starter for wiring up authentication in Django rather than a full-featured application.

## Features

- User registration via Django's `UserCreationForm`, with automatic login on successful signup
- Login and logout backed by Django's built-in `LoginView` and `LogoutView`
- A login-protected home page using the `@login_required` decorator
- Custom-styled login, register, and dashboard templates (plain HTML/CSS)
- Sensible auth redirects (`LOGIN_REDIRECT_URL` / `LOGOUT_REDIRECT_URL`)
- SQLite database out of the box — no external services to configure

## Tech Stack

- **Python** 3.10
- **Django** 5.1
- **SQLite** (default development database)
- HTML + CSS templates (no frontend framework)

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/nickthelegend/django-login-portal.git
cd django-login-portal

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install Django
pip install "Django>=5.1,<5.2"

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) create an admin user
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ — you'll be redirected to the login page. Create an account at `/accounts/register/` to get started.

### Key routes

| Path | Description |
| --- | --- |
| `/` | Login-protected home / dashboard |
| `/accounts/login/` | Log in |
| `/accounts/logout/` | Log out |
| `/accounts/register/` | Create a new account |
| `/admin/` | Django admin site |

## Project Structure

```
django-login-portal/
├── manage.py
├── db.sqlite3
├── MyProject/              # Project configuration
│   ├── settings.py
│   ├── urls.py             # Root URLconf (admin, accounts, home)
│   ├── asgi.py
│   └── wsgi.py
├── accounts/               # Authentication app
│   ├── views.py            # register + login-protected home
│   ├── urls.py             # login / logout / register routes
│   ├── models.py
│   ├── admin.py
│   └── migrations/
└── templates/
    └── accounts/
        ├── login.html
        ├── register.html
        └── home.html       # Dashboard page
```

> **Note:** This is a development/learning setup. The included `settings.py` ships with `DEBUG = True` and a checked-in `SECRET_KEY`; generate a fresh secret and disable debug before deploying anywhere public. The dashboard figures on the home page are static placeholders.

---

Built by [nickthelegend](https://github.com/nickthelegend) · [nickthelegend.tech](https://nickthelegend.tech)
