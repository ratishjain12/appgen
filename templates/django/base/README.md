# Django Base Template

## Usage

1. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and update values as needed.

4. Run migrations and start the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Access the admin at [http://localhost:8000/admin/](http://localhost:8000/admin/)
