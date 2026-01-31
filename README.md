# UniSpace (Django MVP)

UniSpace is a minimal SSR Django platform for IT students with announcements, discussions, marketplace, and lost & found.

## Setup
1) Create and activate venv
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2) Install dependencies
```bash
pip install django pillow
```

3) Run migrations
```bash
python manage.py migrate
```

4) Backfill profiles for existing users (one-time)
```bash
python manage.py backfill_profiles
```

5) Create superuser
```bash
python manage.py createsuperuser
```

6) Run server
```bash
python manage.py runserver
```

## Routes
- `/` -> redirects to `/discussions/`
- `/announcements/`
- `/discussions/`
- `/buy-sell/`
- `/lost-found/`
- `/accounts/register/`
- `/accounts/login/`
- `/accounts/logout/`
- `/accounts/profile/`

## Where to find each module
- Announcements app: `announcements/`
- Discussions app: `discussions/`
- Buy & Sell app: `marketplace/`
- Lost & Found app: `lostfound/`
- Accounts app: `accounts/`
- Base templates: `templates/`
- Static CSS: `static/styles.css`
- Uploaded media: `media/`

## Defense
- Why Django templates (SSR) for MVP: fast to build, minimal frontend complexity, easy to deploy, and perfect for учебный проект with server-side rendering.
- Why different access levels (staff vs users): announcements are official communications and should be controlled by staff, while student-generated content remains open to authenticated users.
- Why backend checks matter: UI hiding is not security; server-side permission checks prevent unauthorized edits/deletes and protect data integrity.
