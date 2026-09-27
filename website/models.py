from django.db import models


class Enquiry(models.Model):
    SERVICE_CHOICES = [
        ("Flight Booking", "Flight Booking"),
        ("Holiday Travel", "Holiday Travel"),
        ("Visa Assistance", "Visa Assistance"),
        ("Accommodation", "Accommodation"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    destination = models.CharField(max_length=100, blank=True)
    travel_date = models.DateField(blank=True, null=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return f"{self.name} - {self.service}"
