from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Exhibit_Items

# Create your views here.
def all_stores(request):
    items = Exhibit_Items.objects.order_by('items_no')
    print(items)
    return render(request,'store/storeitem.html',{'items':items})

def details(request,itemsno):
    print("WAN START")
    print("items_no",itemsno)

    eitem = get_object_or_404(Exhibit_Items,items_no=itemsno)
    # print("item:" + str(eitem))
    print(eitem)
    print("WAN END")
    return render(request,'store/details.html',{'item':eitem})
    # return render(request,'store/details.html')

def completed(request,itemsno): 

    print("itemsno",itemsno)
    eitem = get_object_or_404(Exhibit_Items,items_no=itemsno)

    print("WAN END completed:")
    return render(request,'store/buycompleted.html',{'item':eitem})

def buyupdate(request,itemsno):
#   mymember = Exhibit_Items.objects.get(items_no=itemsno)
#   buytransact = request.POST['buy']
  print("WAN update completed")

  items = Exhibit_Items.objects.get(items_no=itemsno)
  print(items)
  items.buystatus = 1
  items.save()
  return HttpResponseRedirect(reverse('store:completed', kwargs={'itemsno':itemsno}))
 
#参考
# https://fedingo.com/how-to-fix-noreversematch-error-in-django/