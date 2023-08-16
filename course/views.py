from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny

from course.models import Course, Lesson, Payment
from course.paginators import CoursePagination
from course.permissions import IsOwner, IsModerator
from course.serializers import CourseSerializer, LessonSerializer, LessonCreateSerializer, LessonPaymentSerializer, \
    PaymentSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CoursePagination

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            new_course = serializer.save()
            new_course.owner = self.request.user
            new_course.save()

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderator').exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CoursePagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonPaymentListAPIView(generics.ListAPIView):
    serializer_class = LessonPaymentSerializer
    queryset = Payment.objects.filter(lesson__isnull=False)


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("lesson", "course", 'payment_method')
    ordering_fields = ("date_payment",)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
