from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course, Lesson, Payment, Subscription
from course.validators import VideoLinkValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True, read_only=True)
    last_payment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_last_payment(self, instance):
        if instance.payment.all().first():
            return instance.payment.all().first().payment
        return 0


class CourseSerializer(serializers.ModelSerializer):
    last_payment = serializers.FloatField(source='payment.all.first.payment', read_only=True)
    lesson = LessonSerializer(source="lesson_set", many=True)
    payment = PaymentSerializer(many=True)
    subscribe = serializers.SerializerMethodField(read_only=True)

    def get_subscribe(self, instance):
        request = self.context.get("request")
        if instance.subscribe.filter(user=request.user).exists():
            item = instance.subscribe.filter(user=request.user)
            return item[0].is_subscribe
        return False

    class Meta:
        model = Course
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True)

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [VideoLinkValidator(field='link_video')]

    def create(self, validated_data):
        if validated_data.get('payment'):
            payment = validated_data.pop('payment')
            lesson_item = Lesson.objects.create(**validated_data)
            for m in payment:
                Payment.objects.create(**m, lesson=lesson_item)

            return lesson_item
        return validated_data


class LessonPaymentSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
