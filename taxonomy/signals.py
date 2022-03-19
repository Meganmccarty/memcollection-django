from django.db.models.signals import post_save
from django.dispatch import receiver
from taxonomy.models import Subspecies
from specimens.models import SpecimenRecord

@receiver(post_save, sender=Subspecies)
def update_subspecies_value(sender, instance, **kwargs):
    subspecies = {
        "name": instance.name,
        "common_name": instance.common_name,
        "authority": instance.authority,
        "mona": instance.mona,
        "p3": instance.p3
    }
    id = instance.id
    specimens = SpecimenRecord.objects.filter(subspecies=id)

    for specimen in specimens:
        specimen.subspecies_json = subspecies
        specimen.save()

