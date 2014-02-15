from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "An example command to copy."

    def handle_noargs(self, **options):
        # Put execution code here.
        print("Example command")

