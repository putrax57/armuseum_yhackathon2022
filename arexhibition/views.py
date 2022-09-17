from django.shortcuts import render

# Create your views here.
def all_stores(request):
    items = Exhibit_Items.objects.order_by('items_no')
    print(items)
    return render(request,'store/storeitem.html',{'items':items})