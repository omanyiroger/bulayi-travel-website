from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "service",
        "destination",
        "travel_date",
        "created_at",
    )

    list_filter = (
        "service",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "destination",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (
            "Customer Information",
            {
                "fields": (
                    "name",
                    "email",
                    "phone",
                )
            },
        ),

        (
            "Travel Request",
            {
                "fields": (
                    "service",
                    "destination",
                    "travel_date",
                    "message",
                )
            },
        ),

        (
            "Enquiry Information",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )

