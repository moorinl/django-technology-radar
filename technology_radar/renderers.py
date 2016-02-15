from django.http import HttpResponse


class AbstractRenderer(object):
    def render(self, request, radar):
        return HttpResponse('')


class JPGRenderer(AbstractRenderer):
    pass


class PDFRenderer(AbstractRenderer):
    pass


class PNGRenderer(AbstractRenderer):
    pass
