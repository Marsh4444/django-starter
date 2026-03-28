# Django Starter Template

> A clean, production-aware Django boilerplate by Marsh.
> Clone it, rename it, and start building — the boring setup is already done.

---

## What's Included

- Split settings (`base.py` / `dev.py` / `prod.py`)
- Custom `User` model with role field — ready to extend
- Role-based access control via `@role_required` decorator
- Registration, Login, Logout, Profile views — all wired up
- Project-level `templates/` and `static/` folders
- Dark design system CSS (variables, buttons, forms, tables, badges, navbar, footer)
- Whitenoise for static files in production
- `.env` driven configuration via `python-dotenv`
- PostgreSQL by default
- `.gitignore` and `.env.example` included

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/yourusername/django-starter.git my-project
cd my-project

# 2. Remove starter git history and start fresh
rm -rf .git
git init
git add .
git commit -m "Initial commit from django-starter"

# 3. Virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure environment
cp .env.example .env
# Edit .env — set SECRET_KEY and database credentials

# 6. Create database (PostgreSQL)
createdb my_project_db

# 7. Migrate
python manage.py migrate

# 8. Create superuser
python manage.py createsuperuser

# 9. Run
python manage.py runserver
```

---

## Project Structure

```
my-project/
├── apps/
│   └── accounts/           # Custom user model, auth, decorators
│       ├── models.py        # CustomUser with role field
│       ├── views.py         # Register, Login, Logout, Profile
│       ├── forms.py         # RegisterForm, ProfileUpdateForm
│       ├── decorators.py    # @role_required
│       ├── urls.py
│       └── admin.py
├── config/
│   ├── settings/
│   │   ├── base.py          # Shared settings
│   │   ├── dev.py           # Development overrides
│   │   └── prod.py          # Production overrides + security headers
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── css/
│       └── base.css         # Full design system
├── templates/
│   ├── base.html            # Global layout
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── profile.html
│       └── profile_edit.html
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## Customizing for a New Project

### Step 1 — Rename the project
Update `config/wsgi.py` and `manage.py` if you want a custom project name. Otherwise, leave as-is.

### Step 2 — Update roles
In `apps/accounts/models.py`, change `ROLE_CHOICES` to match your app:
```python
ROLE_CHOICES = [
    ('landlord', 'Landlord'),
    ('manager', 'Manager'),
    ('tenant', 'Tenant'),
]
```
Then run `makemigrations` + `migrate`.

### Step 3 — Update the brand name
In `templates/base.html`, find `{% block brand %}Starter{% endblock %}` and override it per project in your child templates.

### Step 4 — Add your apps
```bash
python manage.py startapp my_feature
mv my_feature apps/my_feature
```
Register it in `config/settings/base.py` under `LOCAL_APPS`.

### Step 5 — Customize the CSS
All color variables are in the `:root` block of `static/css/base.css`. Change `--accent` and `--bg` to match your project's identity.

---

## Deployment (PythonAnywhere / Railway)

1. Set `DJANGO_SETTINGS_MODULE=config.settings.prod` in your environment
2. Fill all production variables in `.env` (or server environment panel)
3. Run `python manage.py collectstatic`
4. Use `gunicorn config.wsgi:application` as your entry point

---

## Author

**Holyfield Nwadike** — Backend Developer  
[GitHub](https://github.com/yourusername) · [X](https://x.com/yourhandle)
