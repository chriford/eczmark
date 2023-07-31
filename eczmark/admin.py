from django.contrib import admin

from eczmark.models import (
    Grade,
    Issue,
    Report,
    Subject,
    Question,
    Link,
    Attachment,
    Answer,
)
from eczmark.models.auth import (
    User,
    Profile
)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','email','is_active']
    search_fields = ['email','username','first_name','last_name']
    list_per_page = 20


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
    search_fields = ['user']
    list_per_page = 20


@admin.register(Grade)
class GradeModelAdmin(admin.ModelAdmin):
    list_display = ['grade']
    search_fields = ['grade']
    list_per_page = 10


@admin.register(Issue)
class IssueModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Report)
class ReportModelAdmin(admin.ModelAdmin):
    list_display = ['user','issue','message','active']
    search_fields = ['issue','issue','message','active']
    list_per_page = 20


@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['user','question_paper','grade','year_uncleaned','year_cleaned','subject']
    search_fields = ['subject', 'year_cleaned', 'grade']
    list_per_page = 20


@admin.register(Link)
class LinkModelAdmin(admin.ModelAdmin):
    list_display = ['link','note']
    search_fields = ['link','note']
    list_per_page = 20


@admin.register(Attachment)
class AttachmentModelAdmin(admin.ModelAdmin):
    list_display = ['file', 'note']
    search_fields = ['note']
    list_per_page = 20


@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ['user','body']
    search_fields = ['body']
    list_per_page = 20
