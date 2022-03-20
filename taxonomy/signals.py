from django.db.models.signals import post_save
from django.dispatch import receiver
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies
from specimens.models import SpecimenRecord

@receiver(post_save, sender=Order)
def update_order_value(sender, instance, **kwargs):
    order = {
        "name": instance.name,
        "common_name": instance.common_name,
        "authority": instance.authority
    }
    id = instance.id
    specimens = SpecimenRecord.objects.filter(order=id)
    
    for specimen in specimens:
        specimen.order_json = order
        specimen.save()

@receiver(post_save, sender=Family)
def update_family_value(sender, instance, **kwargs):
    family = {
        "name": instance.name,
        "common_name": instance.common_name,
        "authority": instance.authority
    }
    id = instance.id
    specimens = SpecimenRecord.objects.filter(family=id)
    
    for specimen in specimens:
        specimen.family_json = family
        specimen.save()

@receiver(post_save, sender=Subfamily)
def update_subfamily_value(sender, instance, **kwargs):
    subfamily = {
        "name": instance.name,
        "common_name": instance.common_name,
        "authority": instance.authority
    }
    id = instance.id
    specimens = SpecimenRecord.objects.filter(subfamily=id)
    
    for specimen in specimens:
        specimen.subfamily_json = subfamily
        specimen.save()

@receiver(post_save, sender=Tribe)
def update_tribe_value(sender, instance, **kwargs):
    tribe = {
        "name": instance.name,
        "common_name": instance.common_name,
        "authority": instance.authority
    }
    id = instance.id
    specimens = SpecimenRecord.objects.filter(tribe=id)
    
    for specimen in specimens:
        specimen.tribe_json = tribe
        specimen.save()

@receiver(post_save, sender=Genus)
def update_genus_value(sender, instance, **kwargs):
    genus = {
        "name": instance.name,
        "common_name": instance.common_name,
        "authority": instance.authority
    }
    id = instance.id
    specimens = SpecimenRecord.objects.filter(genus=id)
    
    for specimen in specimens:
        specimen.genus_json = genus
        specimen.save()

@receiver(post_save, sender=Species)
def update_species_value(sender, instance, **kwargs):
    species = {
        "name": instance.name,
        "common_name": instance.common_name,
        "authority": instance.authority,
        "mona": instance.mona,
        "p3": instance.p3
    }
    id = instance.id
    specimens = SpecimenRecord.objects.filter(species=id)

    for specimen in specimens:
        specimen.species_json = species
        specimen.save()

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

