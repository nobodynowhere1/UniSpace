from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from accounts.models import Profile


class Command(BaseCommand):
    help = 'Create missing Profile objects for existing users.'

    def handle(self, *args, **options):
        user_model = get_user_model()
        created_count = 0
        for user in user_model.objects.all():
            _, created = Profile.objects.get_or_create(user=user)
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f'Profiles created: {created_count}'))
