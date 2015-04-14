from django.template import TemplateDoesNotExist
from django.shortcuts import render_to_response

class TemplateDoesNotExistMiddleware(object):
    """
    If enabled, return a 404 response rather than a 400
    TemplateDoesNotExist -> File Not Found
    """
    def process_exception(self, request, exception):
        if isinstance(exception, TemplateDoesNotExist):
            template = "pages/404.html"
            return render_to_response(template, {"request": request})
