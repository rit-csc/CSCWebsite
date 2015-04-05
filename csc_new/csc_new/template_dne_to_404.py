from django.template import TemplateDoesNotExist
from django.views.defaults import page_not_found

class TemplateDoesNotExistMiddleware(object):
    """
    If enabled, return a 404 response rather than a 400
    TemplateDoesNotExist -> File Not Found
    """
    def process_exception(self, request, exception):
        if isinstance(exception, TemplateDoesNotExist):
            return page_not_found(request)
