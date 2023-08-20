from course.models import Course, Lesson


def get_lesson_or_course(paid_lesson_id: int or None, paid_course_id: int or None) -> Course or Lesson or None:
    if paid_course_id:
        return Course.objects.get(pk=paid_course_id)

    return Lesson.objects.get(pk=paid_lesson_id)