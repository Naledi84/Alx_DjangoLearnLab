# Social Media API (starter)

## Setup
1. Create virtualenv and activate
2. Install dependencies:
3. Run migrations:
4. Create superuser:

## Endpoints
- `POST /api/accounts/register/` → register, returns token
- `POST /api/accounts/login/` → login, returns token
- `GET/PUT /api/accounts/profile/` → profile (authenticated)

## Notes
- `AUTH_USER_MODEL = 'accounts.User'` in settings.
- Token authentication via `rest_framework.authtoken`.
- For profile picture uploads enable MEDIA settings and install Pillow.
