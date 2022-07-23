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
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        invoice = Invoice.objects.get(id=context['pk'])
        context['client_name'] = f'{invoice.client.first_name} {invoice.client.last_name}'
        context['client_address'] = invoice.client.address
        context['invoice'] = invoice
        context['total_price'] = invoice.total_price
        context['total_price_inc_vat'] = invoice.total_price_inc_vat
        
        #context['date'] = datetime.date.today().strftime('%d/%m/%Y') dodati sa unosom
        return self.render_to_response(context)