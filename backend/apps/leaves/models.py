from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
from django.db import models

from apps.users.models import User 
from config.constants import LEAVE_TYPE, LEAVES_STATUS

# Create your models here.

class Leave(models.Model):
    class Meta(object):
        db_table = 'leave'

    user = models.ForeignKey(
        User, on_delete=CASCADE, blank=False, null=False, related_name='ID'
    )

    applied_to = models.ForeignKey(
        User, on_delete=CASCADE, blank=False, null=False, db_index=True, related_name='applied_to'
    )
    team = models.ForeignKey(
        User, on_delete=CASCADE, blank=False, null=False, db_index=True, related_name='team'
    )
    leave_type = models.CharField(
        'Leave Type', blank=False, null=False, default='N/A', choices=LEAVE_TYPE, max_length=50
    )

    leave_balance = models.IntegerField(
        'Leave Balance', blank=False, null=False, default=0
    )

    from_date = models.DateTimeField(
        'From Date', blank=False, null=False
    )

    to_date = models.DateTimeField(
        'To Date', blank=False, null=False
    )

    duration = models.IntegerField(
        'Duration', blank=False, null=False, default=0
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=False, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated Datetime', blank=False, auto_now=True
    )

    description = models.CharField(
        'Notes', blank=False, null=False, db_index=True, max_length=400, default='Description & Responsibilities Assigned'
    )

    leave_status = models.CharField(
        'Leave Status', blank=True, null=True, default='applied', choices=LEAVES_STATUS, max_length=30
    )
    def __str__(self):
        return self.user_name.name

  

