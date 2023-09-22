from django.contrib.auth.models import User
from django.db.utils import  IntegrityError
try:
    print("Create super user")
    User.objects.create_superuser('admin_2', 'adminn@example.com', 'adminpass')
except IntegrityError as e:
    print(f"exception: {e}")
    pass