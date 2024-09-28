from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CourseViewSet, SessionViewSet, EnrollmentViewSet, FeedbackViewSet, CertificateViewSet, MaterialViewSet, QuizViewSet, QuestionViewSet, OptionViewSet, UserQuizResponseViewSet, NotificationViewSet, UserRolePermissionViewSet, PaymentTransactionViewSet,LoginView,LogoutView,RegisterView

router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'options', OptionViewSet)
router.register(r'user_quiz_responses', UserQuizResponseViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'user_role_permissions', UserRolePermissionViewSet)
router.register(r'payment_transactions', PaymentTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
