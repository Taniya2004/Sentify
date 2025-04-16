from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = 'Displays all URL patterns in the project'

    def handle(self, *args, **options):
        url_patterns = get_resolver().url_patterns
        self.print_patterns(url_patterns)

    def print_patterns(self, patterns, prefix=''):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                self.print_patterns(pattern.url_patterns, prefix + str(pattern.pattern))
            else:
                self.stdout.write(f"{prefix}{pattern.pattern} -> {pattern.name}")
