import os
import StringIO
import xhtml2pdf.pisa as pisa

from django.http import HttpResponse, HttpResponseServerError
from django.template import Context, loader


class PDFViewMixin(object):
    """
    A Mixin to use with DetailView's that replaces render_to_response with
    a PDF using xhtml2pdf/pisa.
    """
    font_path = "{0}/fonts".format(os.path.dirname(os.path.abspath(__file__)))
    template_name = 'pdfview/base.html'  # extend this

    def get_filename(self):
        return "{cls}-{pk}.pdf".format(
            cls=self.object.__class__.__name__,
            pk=self.object.pk)

    def render_to_response(self, context, **kwargs):
        filename = self.get_filename()
        data = self.get_context_data(font_path=self.font_path)
        template = loader.get_template(self.get_template_names()[0])

        html = template.render(Context(data))
        result = StringIO.StringIO()
        pdf = pisa.pisaDocument(StringIO.StringIO(html.encode('UTF-8')), result)
        if pdf.err:
            return HttpResponseServerError
        response = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Disposition'] = 'filename={0}'.format(filename)
        return response
