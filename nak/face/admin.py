from django.contrib import admin
from . models import *
from django.http import HttpResponse

# Register your models here.
# admin.site.register(Order)


# export functions will go there

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=order.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"subdivision"),
        smart_str(u"reason"),
        smart_str(u"to_whom"),
        smart_str(u"name"),
        smart_str(u"quantity"),
        smart_str(u"measurement"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.subdivision),
            smart_str(obj.reason),
            smart_str(obj.to_whom),
            smart_str(obj.name),
            smart_str(obj.quantity),
            smart_str(obj.measurement)
        ])
    return response


export_csv.short_description = u"Export CSV"


class OrderAdmin(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Order, OrderAdmin)
