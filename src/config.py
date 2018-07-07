import os

__author__ = 'vkaser'

DEBUG = True
ADMINS = frozenset([os.environ.get('EMAIL_ADMIN')])
