from django.contrib import admin
from .models import User,Course,Certificate,Session,Enrollment,Feedback,Material,Quiz,Question,Option,UserQuizResponse,Notification,UserRolePermission,PaymentTransaction

# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Certificate)
admin.site.register(Session)
admin.site.register(Enrollment)
admin.site.register(Feedback)
admin.site.register(Material)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserQuizResponse)
admin.site.register(Notification)
admin.site.register(UserRolePermission)
admin.site.register(PaymentTransaction)

