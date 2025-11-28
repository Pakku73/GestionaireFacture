from django.shortcuts import render

from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect
from .form import InvoiceItemForm
from .models import InvoiceItem, Invoice



class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/list.html"
    paginate_by = 10

class InvoiceCreateView(CreateView):
    model = Invoice
    fields = ["number"]   # on fera générer automatiquement plus tard
    template_name = "invoices/form.html"
    success_url = reverse_lazy("invoices:detail")
    def get_success_url(self):
        return reverse_lazy("invoices:add_item", kwargs={"invoice_id": self.object.pk})

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "invoices/detail.html"


class InvoiceItemCreateView(CreateView):
    model = InvoiceItem
    form_class = InvoiceItemForm
    template_name = "invoices/item_form.html"

    def form_valid(self, form):
        invoice = Invoice.objects.get(pk=self.kwargs["invoice_id"])
        product = form.cleaned_data["product"]
        quantity = form.cleaned_data["quantity"]

        existing_item = InvoiceItem.objects.filter(invoice=invoice, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
            return redirect(self.get_success_url())

        form.instance.invoice = invoice
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("invoices:detail", kwargs={"pk": self.kwargs["invoice_id"]})


def invoice_pdf(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    template_path = "invoices/pdf.html"
    context = {"invoice": invoice}
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"attachment; filename=facture_{invoice.number}.pdf"
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Erreur lors de la génération du PDF", status=500)

    return response