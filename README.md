# Mahedi Hasan — Academic Portfolio

A responsive Django portfolio for Mahedi Hasan, Lecturer in Computer Science and Engineering at IUBAT. Portfolio content is stored in the database and managed through Django Admin, so the owner can update the site without changing templates or code.

## Features

- Professional, responsive portfolio with accessible page navigation.
- Editable profile, education, experience, research, publications, skills, and awards.
- Django Admin content management at `/admin/`.
- SQLite for local development and PostgreSQL for deployment.
- WhiteNoise static-file serving and a Render deployment blueprint.
- The initial content command only seeds empty sections. It does not overwrite existing admin edits.

## Run locally

Python 3.12 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_portfolio
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the portfolio and `http://127.0.0.1:8000/admin/` to edit it.

For local development, the settings use SQLite by default. Set `DATABASE_URL` to a PostgreSQL connection string to use PostgreSQL instead. For any public deployment, set a unique `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=false`, and configure `DJANGO_ALLOWED_HOSTS` for the deployed domain.

## Editing the portfolio

Sign into `/admin/` with the superuser credentials and edit the relevant section. Use the profile record for biography and profile links; add, edit, reorder, or remove records for the other sections. Research interests and experience highlights are entered one item per line. The admin is intentionally separate from the public portfolio.

## Deploy to Render

1. Push this repository to GitHub and import it in Render.
2. Use the included `render.yaml` blueprint to create the web service and PostgreSQL database.
3. Render runs migrations and seeds initial CV content before each deploy. The seed command does not overwrite non-empty sections.
4. Create the first administrator once the site is live:

   ```bash
   python manage.py createsuperuser
   ```

   Run this in Render's shell, then sign in at `/admin/`.

To add social profile links, edit the profile in the admin. They are deliberately blank until the correct URLs are supplied.

## Project structure

```text
config/                 Django settings and URL configuration
portfolio/
  management/commands/  Initial CV content command
  migrations/           Database schema history
  static/portfolio/     Styles and small navigation script
  templates/portfolio/  Public portfolio template
  admin.py              Editable content management
  models.py             Structured portfolio content
```

## Architecture

Django uses the **Model–Template–View (MTV)** pattern, which is Django's equivalent of MVC:

- **Model:** `portfolio/models.py` defines structured, database-backed content.
- **Template:** `portfolio/templates/portfolio/home.html` renders the public page.
- **View:** `portfolio/views.py` selects content and passes it to the template.
- **Controller equivalent:** Django URL routing and request handling connect the view to each request.

## Content accuracy

Initial entries are based on the CV provided for this portfolio. Please check publication metadata, author order, dates, results, and profile URLs in the admin before public launch; all are editable.
