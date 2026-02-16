from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = "Prints total number of published blog posts"

    def handle(self, *args, **kwargs):
        count = Post.objects.filter(status='published').count()
        self.stdout.write(f"Total published posts: {count}")
