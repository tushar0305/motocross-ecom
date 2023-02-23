from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
from django.urls import reverse


class Company(models.Model):
    company_name = models.CharField(max_length=255, db_index=True)
    company_slug = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "1. Companies"

    def __str__(self):
        return self.company_name


class Bikes(models.Model):
    bike_name = models.CharField(max_length=255, db_index=True, null=True)
    bike_slug = models.SlugField(max_length=255, unique=True, null=True)
    company_name = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE, null=True)
    status = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "2. Bikes"
        ordering = ('-created',)

    def __str__(self):
        return self.bike_name


class Manufacturer(models.Model):
    choices = (("0", "INACTIVE"), ("1", "ACTIVE"),)
    manufacturer_name = models.CharField(max_length=255, db_index=True, null=True)
    manufacturer_slug = models.SlugField(max_length=255, unique=True, null=True)
    status = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "3. Manufacturer"
        ordering = ('-created',)

    def __str__(self):
        return self.manufacturer_name


class Supplier(models.Model):
    choices = (("0", "INACTIVE"), ("1", "ACTIVE"),)
    supplier_name = models.CharField(max_length=255, help_text='supplier Name')
    supplier_slug = models.SlugField(max_length=255, unique=True, null=True)
    manufacturer_name = models.ForeignKey(Manufacturer, related_name='manufacturer', on_delete=models.CASCADE,
                                          null=True)
    account_no = models.CharField(max_length=255,null=True,blank=True)
    pan_no = models.CharField(max_length=255,null=True,blank=True)
    gst_no = models.CharField(max_length=255,null=True,blank=True)
    cin_no = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=10, choices=choices, default='1')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "4. Supplier"
        ordering = ('-created',)

    def __str__(self):
        return self.supplier_name


class Catelogue(models.Model):
    part_name = models.CharField(max_length=255)
    part_slug = models.SlugField(max_length=255, unique=True, null=True)
    part_number = models.CharField(max_length=255)
    part_for_bike = models.ForeignKey(Bikes, related_name='bike', on_delete=models.CASCADE, null=True)
    part_manufacturer = models.ForeignKey(Manufacturer, related_name='product_manufacturer', on_delete=models.CASCADE,
                                          null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    item_Description = models.TextField(blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='catlogue_added_by', on_delete=models.CASCADE, null=True)
    photo = models.ImageField(blank=True, upload_to="product_images/")  # storing links in database
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "5. Catelogue"
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.part_slug])

    def __str__(self):
        return str(self.part_name)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)
    invoice_date = models.DateField()
    file = models.FileField(upload_to="invoices/")

    class Meta:
        verbose_name_plural = "6. Invoice"

    def __str__(self):
        return str(self.invoice_number)


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(status=0)
        # _________________________________________


class Product(models.Model):
    status_choice = (("0", "Available"), ("1", "Not Available"),)
    part_name = models.ForeignKey(Catelogue, related_name='catlogue_part_name', on_delete=models.CASCADE, null=True)
    # part_number = models.ForeignKey(Catelogue, related_name='catlogue_part_number', on_delete=models.CASCADE, null=True)
    # photo_display = models.ForeignKey(Catelogue, related_name='related_photo', on_delete=models.CASCADE, null=True)
    # reference for photo in html should be like below
    # src = "{{ product.photo_display.photo.url }}
    invoice_number = models.ForeignKey(Invoice, related_name='invoice', on_delete=models.CASCADE, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_added_by', on_delete=models.CASCADE, null=True)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10, default='0')
    price = models.DecimalField(decimal_places=2, max_digits=10, default='0')
    Quantity = models.IntegerField(default='0')
    max_discount = models.DecimalField(decimal_places=2, max_digits=10, default='0')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=status_choice, default='0')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = "7. Products"
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:detail_product', args=[self.id])

    def __str__(self):
        return str(self.part_name)


"""class Vendor (models.Model):
    choices = (("0", "INACTIVE"), ("1", "ACTIVE"),)
    vendor_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    account_no = models.CharField(max_length=255)
    pan_no = models.CharField(max_length=255)
    gst_no = models.CharField(max_length=255)
    cin_no = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=choices, default='1')


    class Meta:
        verbose_name_plural = "8. Vendor"

    def __str__(self):
        return str(self.vendor_name)"""
