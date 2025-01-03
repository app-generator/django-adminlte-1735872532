# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    cpf_cnpj = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Proposta(models.Model):

    #__Proposta_FIELDS__
    data_criacao_prosposta = models.DateTimeField(blank=True, null=True, default=timezone.now)
    titulo_proposta = models.TextField(max_length=255, null=True, blank=True)
    data_viagem = models.DateTimeField(blank=True, null=True, default=timezone.now)
    capa = models.TextField(max_length=255, null=True, blank=True)
    id_status_proposta = models.IntegerField(null=True, blank=True)
    descricao_proposta = models.TextField(max_length=255, null=True, blank=True)
    id_proposta = models.IntegerField(null=True, blank=True)

    #__Proposta_FIELDS__END

    class Meta:
        verbose_name        = _("Proposta")
        verbose_name_plural = _("Proposta")



#__MODELS__END
