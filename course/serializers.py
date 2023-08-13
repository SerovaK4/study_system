from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course, Lesson, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True)
    last_payment = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_last_payment(self, instance):
        if instance.payment.all().first():
            return instance.payment.all().first().payment
        return 0


class CourseSerializer(serializers.ModelSerializer):
    last_payment = serializers.FloatField(source='payment.all.first.payment')
    lesson = LessonSerializer(source="lesson_set", many=True)
    payment = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True)

    class Meta:
        model = Lesson
        fields = "__all__"

    def create(self, validated_data):
        payments_data = validated_data.pop('payment')
        lesson = Lesson.objects.create(**validated_data)
        for payment_data in payments_data:
            Payment.objects.create(lesson=lesson, **payment_data)
        return lesson


class LessonPaymentSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
