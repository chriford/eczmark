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
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Grade)
class GradeModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Issue)
class IssueModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Report)
class ReportModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Link)
class LinkModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Attachment)
class AttachmentModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20


@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []
    list_per_page = 20
