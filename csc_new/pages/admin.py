from django.contrib import admin
from pages.models import ExamReview, Photo, GeneralMeetingSlides, Attendance

# Register your models here.
admin.site.register(ExamReview)
admin.site.register(Photo)
admin.site.register(GeneralMeetingSlides)
admin.site.register(Attendance)
