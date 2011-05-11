from armstrong.dev.tasks import *

settings = {
    'INSTALLED_APPS': (
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.auth',
        'django.contrib.sites',
        'armstrong.apps.arm_events',
        'armstrong.apps.arm_events.tests.arm_events_support',
        'armstrong.core.arm_content',
    ),
    'TEMPLATE_CONTEXT_PROCESSORS': (
        'django.core.context_processors.request',
        'django.contrib.auth.context_processors.auth',
    ),
    'ROOT_URLCONF': 'armstrong.apps.arm_events.urls',
    'SITE_ID': 1,
}

main_app = 'arm_events'
tested_apps = (main_app,)
