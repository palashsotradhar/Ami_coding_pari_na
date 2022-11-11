from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import khojform
from  .models import khojm
from django.contrib.auth.models import User


# Create your views here.
# @login_required(login_url='')
class khoj(View):
    def get(self,request):
        fr = khojform()
        return render(request, 'khoj_the_search/khoj_the_search.html',{'fr':fr,'result':''})
    def post(self,request):
        fr = khojform(request.POST)
        if fr.is_valid():
            user_input = fr.cleaned_data['input_values']
            search = fr.cleaned_data['search']
            #i used split for separate all user input and type cast all value into integer
            input = [int(i) for i in user_input.split(',')]
            result = False
            #we cound use a linear search because in soting the complixity we get nlogn so the complixity of this program nlogn
            for i in input:
                if i == int(search):
                    result = True
            #i use build in functionality for sorting of this input value in decending order.This build in sort object used tim sort which complixity is nlogn or something.So we can say that its use efficient algorithm.
            input.sort(reverse = True)
            #i used a join function for made a list to string
            sinput = [str(i) for i in input]
            jinput = ','.join(sinput)
            data = khojm(user_id = request.user.id,input_values = jinput)
            data.save()
            return render(request, 'khoj_the_search/khoj_the_search.html',{'fr':fr,'result':result})