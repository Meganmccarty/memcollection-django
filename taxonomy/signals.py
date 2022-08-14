from django.db.models.signals import post_save
from django.dispatch import receiver
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies
from specimens.models import SpecimenRecord

def update_specimen_record(instance, field):
    id = instance.id
    test = {field: id}
    specimens = SpecimenRecord.objects.filter(**test)

    for specimen in specimens:
        specimen.save()

@receiver(post_save, sender=Order)
def update_order_value(sender, instance, **kwargs):
    update_specimen_record(instance, "order")

@receiver(post_save, sender=Family)
def update_family_value(sender, instance, **kwargs):
    update_specimen_record(instance, "family")

@receiver(post_save, sender=Subfamily)
def update_subfamily_value(sender, instance, **kwargs):
    update_specimen_record(instance, "subfamily")

@receiver(post_save, sender=Tribe)
def update_tribe_value(sender, instance, **kwargs):
    update_specimen_record(instance, "tribe")

@receiver(post_save, sender=Genus)
def update_genus_value(sender, instance, **kwargs):
    update_specimen_record(instance, "genus")

@receiver(post_save, sender=Species)
def update_species_value(sender, instance, **kwargs):
    update_specimen_record(instance, "species")

@receiver(post_save, sender=Subspecies)
def update_subspecies_value(sender, instance, **kwargs):
    update_specimen_record(instance, "subspecies")
