import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_2.settings")

import django

django.setup()

# fake population script
from app_2.models import User
from faker import Faker

fake = Faker()


def populate(N=10):
    for entry in range(N):

        # Create the fake data:
        fake_name = fake.first_name()
        fake_surname = fake.last_name()
        fake_email = fake.email()

        # Populate a user object:
        new_user = User.objects.get_or_create(
            first_name=fake_name, last_name=fake_surname, email=fake_email
        )[0]


if __name__ == "__main__":
    print("populating databases")
    populate(20)
    print("finished")
