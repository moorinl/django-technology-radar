from django.http import HttpResponse

from reportlab.pdfgen import canvas


class AbstractRenderer(object):
    def render(self, request, radar):
        return HttpResponse('')


class JPGRenderer(AbstractRenderer):
    pass


class PDFRenderer(AbstractRenderer):
    def render(self, request, radar):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % (
                                          radar.slug)

        pdf = canvas.Canvas(response)
        pdf.drawString(100, 100, radar.name)
        pdf.showPage()
        pdf.save()

        return response


class PNGRenderer(AbstractRenderer):
    pass
