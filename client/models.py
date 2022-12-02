from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserInfo(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, related_name='profile')
    company_name = models.CharField(_("Company or project Name"), max_length=200)
    company_vat = models.CharField(_("Company VAT"), max_length=200, blank=True, null=True)
    whatsapp = models.CharField(_("WhatsApp"), max_length=200)
    domaine = models.URLField(_("Domain"), max_length=200, blank=True, null=True)
    validated_client = models.BooleanField(default=False)
    accepted_terms = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Personal info"
        verbose_name_plural = "Personal info"

    def __str__(self):
        return self.company_name


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)
    instance.profile.save()
