from django.urls import path
from . import views

app_name = "invoices"

urlpatterns = [
    path("", views.InvoiceListView.as_view(), name="list"),
    path("create/", views.InvoiceCreateView.as_view(), name="create"),
    path("<int:pk>/", views.InvoiceDetailView.as_view(), name="detail"),
    path("<int:invoice_id>/add-item/", views.InvoiceItemCreateView.as_view(), name="add_item"),
    path("<int:pk>/pdf/", views.invoice_pdf, name="pdf"),

]
