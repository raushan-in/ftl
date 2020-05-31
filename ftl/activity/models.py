from django.db import models
from django.contrib.auth.models import User
from . import TIMEZONE_CHOICES
from hashids import Hashids

hashids = Hashids(salt='raushan_thl', min_length=9)


class Member(models.Model):
    user = models.OneToOneField(User,
                                null=True, on_delete=models.SET_NULL)
    tz = models.CharField(choices=TIMEZONE_CHOICES, max_length=10)

    def __str__(self):
        return f'{self.user.first_name}'

    @property
    def real_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def hash_id(self):
        return hashids.encode(self.user.pk)


class ActivityPeriod(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,
                               related_name="activity")
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f'activity - {self.member}'
