from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
import json

class CompanyViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        companies = list(Company.objects.values())
        if len(companies)>0:
            datos = {'msg':"Success",'companies':companies}
        else:
            datos = {'msg':'Companies not found'}
        return JsonResponse(datos)
    def post(self,request):
        jd = json.loads(request.body)
        Company.objects.create(companyname=jd['companyname'],direction=jd['direction'],
        NIT=jd['NIT'],cell=jd['cell'])
        datos = {'msg':"Success"}
        return JsonResponse(datos)
    def put(self,request,id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.companyname = jd['companyname'] 
            company.direction   = jd['direction'] 
            company.NIT         = jd['NIT'] 
            company.cell        = jd['cell']
            company.save() 
            datos = {'msg':"Success"}
        else:
            datos = {'msg':'Companies not found'}
        return JsonResponse(datos)

    def delete(self,request,id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
             Company.objects.filter(id=id).delete()
             datos = {'msg':"Success"}
        else:
            datos = {'msg':'Companies not found'}
        return JsonResponse(datos)