import os
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from rest_framework.utils import json

from course.models import Course, Lesson


def get_lesson_or_course(paid_lesson_id: int or None, paid_course_id: int or None) -> Course or Lesson or None:
    if paid_course_id:
        return Course.objects.get(pk=paid_course_id)

    return Lesson.objects.get(pk=paid_lesson_id)


def set_shedule():

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES,
    )
    PeriodicTask.objects.create(
        interval=schedule,  # we created this above.
        name='Importing contacts',  # simply describes this periodic task.
        task='course.tasks.block_user',  # name of task.
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )

def get_email(user):
    emails = []
    for us in user:
        emails.append(us.user.email)
    return emails