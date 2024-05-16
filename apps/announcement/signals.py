from django.db.models.signals import post_migrate
from django.dispatch import receiver
from apps.announcement.models import Rubric
from apps.common.constants import RUBRIC_CHOICES


@receiver(post_migrate)
def create_initial_rubrics(sender, **kwargs):
    if sender.name == 'apps.announcement':
        for rubric_title, _ in RUBRIC_CHOICES:
            Rubric.objects.get_or_create(title=rubric_title)
