import datetime
from django.conf import settings
from django_weasyprint import WeasyTemplateView
from .models import Invoice

class InvoicePdfView(WeasyTemplateView):
    datum = datetime.datetime.now().strftime("%d.%m.%Y")
    #datum = datetime.date.today().strftime('%d/%m/%Y')
    template_name = 'Core/invoice-pdf.html'
    pdf_filename = f'Bakop Racun-{datum}.pdf' 
    pdf_stylesheets = [settings.STATIC_ROOT + '/pdf/invoice.css']