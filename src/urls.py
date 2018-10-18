from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from src.classroom.views import classroom, students, teachers

urlpatterns = [
    path('', include('src.classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
