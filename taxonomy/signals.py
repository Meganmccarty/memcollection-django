from django.db.models.signals import post_save
from django.dispatch import receiver
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies
from specimens.models import SpecimenRecord

@receiver(post_save, sender=Order)
def update_order_value(sender, instance, **kwargs):
    id = instance.id
    specimens = SpecimenRecord.objects.filter(order=id)
    
    for specimen in specimens:
        specimen.save()

@receiver(post_save, sender=Family)
def update_family_value(sender, instance, **kwargs):
    id = instance.id
    specimens = SpecimenRecord.objects.filter(family=id)
    
    for specimen in specimens:
        specimen.save()

@receiver(post_save, sender=Subfamily)
def update_subfamily_value(sender, instance, **kwargs):
    id = instance.id
    specimens = SpecimenRecord.objects.filter(subfamily=id)
    
    for specimen in specimens:
        specimen.save()

@receiver(post_save, sender=Tribe)
def update_tribe_value(sender, instance, **kwargs):
    id = instance.id
    specimens = SpecimenRecord.objects.filter(tribe=id)
    
    for specimen in specimens:
        specimen.save()

@receiver(post_save, sender=Genus)
def update_genus_value(sender, instance, **kwargs):
    id = instance.id
    specimens = SpecimenRecord.objects.filter(genus=id)
    
    for specimen in specimens:
        specimen.save()

@receiver(post_save, sender=Species)
def update_species_value(sender, instance, **kwargs):
    id = instance.id
    specimens = SpecimenRecord.objects.filter(species=id)

    for specimen in specimens:
        specimen.save()

@receiver(post_save, sender=Subspecies)
def update_subspecies_value(sender, instance, **kwargs):
    id = instance.id
    specimens = SpecimenRecord.objects.filter(subspecies=id)

    for specimen in specimens:
        specimen.save()

