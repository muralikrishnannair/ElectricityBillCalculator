from django.http import JsonResponse
from django.views.generic import View
from json import loads

# Create your views here.


# Calculate electricity bill

class ElectricityBillView(View):
    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        units = form_data.get("units")

        if units <= 100:
            amount = units * 3

        elif units <= 200:
            amount = (100 * 3) + ((units - 100) * 5)

        else:
            amount = (100 * 3) + (100 * 5) + ((units - 200) * 7)

        return JsonResponse({
            "units_consumed": units,
            "total_bill": amount
        })


# Calculate units consumed

class UnitCalculationView(View):
    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        previous_reading = form_data.get("previous_reading")
        current_reading = form_data.get("current_reading")

        units = current_reading - previous_reading

        return JsonResponse({
            "previous_reading": previous_reading,
            "current_reading": current_reading,
            "units_consumed": units
        })


# Bill details

class BillDetailsView(View):
    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        consumer_name = form_data.get("consumer_name")
        consumer_number = form_data.get("consumer_number")
        units = form_data.get("units")

        if units <= 100:
            amount = units * 3

        elif units <= 200:
            amount = (100 * 3) + ((units - 100) * 5)

        else:
            amount = (100 * 3) + (100 * 5) + ((units - 200) * 7)

        return JsonResponse({
            "consumer_name": consumer_name,
            "consumer_number": consumer_number,
            "units_consumed": units,
            "electricity_charge": amount,
            "bill_status": "Pending"
        })