from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a custom admin user'

    def handle(self, *args, **options):
        admin_username = 'admin'
        admin_email = 'admin@gmail.com'
        admin_password = 'admin'

        admin, created = User.objects.get_or_create(
            username=admin_username,
            email=admin_email,
            defaults={'is_staff': True, 'is_superuser': True}
        )

        if created:
            admin.set_password(admin_password)
            admin.save()
            self.stdout.write(self.style.SUCCESS('Custom admin created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Custom admin already exists!'))
