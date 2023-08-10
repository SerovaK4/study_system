from django.contrib import admin

from course.models import Course, Lesson, Payment


# Register your models here.

@admin.register(Course)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'description')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "img", "description", "link_video", "course")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "date_payment", "course", "lesson", "payment", "payment_method")
