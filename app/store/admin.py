from django.contrib import admin
from store.models import Company, Bikes, Manufacturer, Supplier, Product, Catelogue, Invoice


# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_slug']
    prepopulated_fields = {'company_slug': ('company_name',)}


@admin.register(Bikes)
class BikesAdmin(admin.ModelAdmin):
    list_display = ['bike_name', 'bike_slug']
    prepopulated_fields = {'bike_slug': ('bike_name',)}


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer_name', 'manufacturer_slug']
    prepopulated_fields = {'manufacturer_slug': ('manufacturer_name',)}


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_name', 'supplier_slug']
    prepopulated_fields = {'supplier_slug': ('supplier_name',)}


@admin.register(Catelogue)
class CatelogueAdmin(admin.ModelAdmin):
    list_display = ['part_name', 'part_slug']
    prepopulated_fields = {'part_slug': ('part_name',)}


"""@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['part_name', 'price', 'purchase_price', 'Quantity', 'status']
    list_filter = ['status']
    list_editable = ['price', 'purchase_price', 'status']
    # prepopulated_fields = {'part_slug': ('part_name',)}"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['part_name', 'price', 'purchase_price', 'Quantity', 'added_by', 'status']
    list_filter = ['status']
    list_editable = ['price', 'purchase_price', 'status']
    exclude = ('added_by',)

    def save_form(self, request, form, change):
        obj = super(ProductAdmin, self).save_form(request, form, change)
        if not change:
            obj.added_by = request.user
        return obj


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'invoice_date']
    list_filter = ['invoice_date']


"""@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'company_name','account_no']
    list_filter = ['status']"""
