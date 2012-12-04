A mixin for a DetailView to easily render a pdf from a Django template using [xhtml2pdf][].

In your view:


    from django.views.generic import DetailView
    from pdfview.views import PDFViewMixin

    class PagePDFView(PDFViewMixin, DetailView):
        model = Page           
        template_name = 'pdf.html'

Then in `pdf.html`:

    {% extends "pdfview/base.html" %}

    {% block css %}
    {{ block.super }}
    <style type="text/css">
        /* put your custom css here */
    </style>
    {% endblock css %}

    {% block content %}
    <p>This is id {{ object.pk }} in a PDF.</p>
    {% endblock content %}


[xhtml2pdf]: http://www.xhtml2pdf.com/
