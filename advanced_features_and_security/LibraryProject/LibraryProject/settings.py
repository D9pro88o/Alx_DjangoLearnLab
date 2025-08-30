# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1#11k+z=5l8!yj_n=z7_9jhp==r#3^cl&tu0v)yh041%+bsm4^'

# SECURITY WARNING: turn off debug in production
DEBUG = False  # Must be False in production

# Specify allowed hosts for your domain
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']  # adjust for production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'accounts',
    'csp',  # Content Security Policy
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # protects against CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # clickjacking protection
    'csp.middleware.CSPMiddleware',  # CSP middleware
]

# Browser-side security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# Cookies over HTTPS only
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Optional: HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Content Security Policy settings
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self'",)

# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'
