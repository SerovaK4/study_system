from django.urls import path

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, LessonCreateAPIView, LessonListView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentCreateAPIView, LessonPaymentListAPIView, PaymentListAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('', LessonListView.as_view(), name='lesson-list'),
    path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

                  # milage
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('lesson/payment/', LessonPaymentListAPIView.as_view(), name='payment-course'),
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),

              ] + router.urls