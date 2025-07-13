# This script will remove all migration files except __init__.py, then create fresh migrations.
import os
import glob

migrations_path = os.path.join(os.path.dirname(__file__), 'myapp', 'migrations')
for filename in glob.glob(os.path.join(migrations_path, '*.py')):
    if not filename.endswith('__init__.py'):
        os.remove(filename)
for filename in glob.glob(os.path.join(migrations_path, '*.pyc')):
    os.remove(filename)
print('Old migrations removed. Now run makemigrations and migrate.')
