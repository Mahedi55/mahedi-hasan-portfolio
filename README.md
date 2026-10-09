# Mahedi Hasan — Academic Portfolio

A responsive Django portfolio for Mahedi Hasan, Lecturer in Computer Science and Engineering at IUBAT. Portfolio content is stored in the database and managed through Django Admin, so the owner can update the site without changing templates or code.

## Features

- Professional, responsive portfolio with accessible page navigation.
- Editable profile, education, experience, research, publications, skills, and awards.
- Django Admin content management at `/admin/`.
- SQLite for local development and an external PostgreSQL database for Render's free web service.
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

## Deploy to Render's free web service

The Blueprint creates a free Render web service and expects a PostgreSQL database hosted separately. Render's free PostgreSQL databases expire after 30 days and are deleted after a further 14-day grace period, so they are not suitable for long-term portfolio content. See [Render's free-tier limitations](https://render.com/docs/free).

1. Create a PostgreSQL database with a provider whose free-tier limits and retention terms meet your needs. Copy its connection string; do not commit it or send it in chat.
2. In Render, choose **New > Blueprint**, connect this GitHub repository, and select the `main` branch.
3. During Blueprint setup, set the prompted environment variables:
   - `DATABASE_URL`: the external PostgreSQL connection string.
   - `PORTFOLIO_ADMIN_USERNAME` and `PORTFOLIO_ADMIN_EMAIL`: the first Django admin account.
   - `PORTFOLIO_ADMIN_PASSWORD`: a unique, strong password. Enter it only in Render.
4. Confirm the web service plan is **Free** and apply the Blueprint. On startup it runs database migrations, seeds only empty portfolio sections, creates the initial admin if needed, and then starts Gunicorn on Render's assigned port.
5. After the first successful startup, remove `PORTFOLIO_ADMIN_PASSWORD` from the Render service environment. The bootstrap command will leave the existing admin unchanged on subsequent restarts. Sign in at `/admin/`.

The free web service may spin down while idle, so the first visit can take about a minute. Portfolio edits are stored in the external PostgreSQL database; check that provider's backup and retention limits and keep an independent backup of important content.

Once Render is connected to the GitHub `main` branch, future code pushes deploy automatically. Editing portfolio content in Django Admin updates the database directly and does not require a code deployment.

To add social profile links, edit the profile in the admin. They are deliberately blank until the correct URLs are supplied.

## Project structure

```text
config/                 Django settings and URL configuration
portfolio/
  management/commands/  Initial content and admin bootstrap commands
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
