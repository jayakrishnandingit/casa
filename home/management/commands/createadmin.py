from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    help = 'Create an admin user. This is an idempotent command. Only creates iff there is no admin user.'

    def handle(self, *args, **options):
        admin = User.objects.filter(email=settings.CONTACT_EMAIL)
        if admin.count() > 0:
            self.stdout.write(f"Admin with email {settings.CONTACT_EMAIL} exists. Skipping command.")
            return
        self.stdout.write(f"Creating admin user. email: {settings.CONTACT_EMAIL}, username: admin.")
        User.objects.create_superuser(
            username='admin',
            email=settings.CONTACT_EMAIL,
            password='panj@sara'
        )
        self.stdout.write("Successfully created admin user.")
