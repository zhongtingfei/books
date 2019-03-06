from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
import random
# Create your views here.

def V_index(request):
    books_id = random.sample(range(3,89),9)
    book_list = []
    for i in books_id:
        obj = Books.objects.filter(book_id=i)[0]
        obj.book_img_url = '/static/book_image/'+obj.book_name+'.jpg'

        book_list.append(obj)

    return render(request, 'index.html', locals())


#登录视图
def V_login(request):
    if request.method == 'GET':
        #get方法
        if request.session.get('is_login',''):
            return render(request,'index.html')
        else:
            uname=request.COOKIES.get('uname','')
            upasswd = request.COOKIES.get('upasswd','')
            if uname=='abc' and upasswd=='123':
                return render(request,'index.html')
            else:
                return render(request,'login.html',{'errmsg':''})
    else:
        #post方法
        if request.POST.get('btn')=='register':
            return redirect('/register/')
        else:
            uname=request.POST.get('uname','')
            upasswd = request.POST.get('upasswd','')
            print(uname)
            user=Users.objects.filter(user_name=uname,user_passwd=upasswd)
            if user:
                request.session['is_login']='True'
                res = render(request, 'index.html')
                res.set_cookie('uname',uname)
                res.set_cookie('upasswd',upasswd)
                return res
            else:
                return render(request, 'login.html',{'errmsg':'账号或者密码错误'})



#
def V_register(request):
    uform = userForm()
    if request.method == 'GET':
        return render(request,'register.html',{'uform':uform})
    else:
        # uname = request.POST.get('uname','')
        # upasswd = request.POST.get('upasswd','')
        # uemail = request.POST.get('uemail','')
        form = userForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            user_data={
                "user_name":form_data['uname'],
                "user_passwd":form_data['upasswd'],
                "user_email":form_data['uemail']
            }

            if form_data:
                Users.objects.create(**user_data)
                return HttpResponse('恭喜您，成功注册！')








def V_check(request):

    uname = request.GET.get('uname','')
    uemail = request.GET.get('uemail','')
    if uname:
        if Users.objects.filter(user_name=uname):

            return JsonResponse({'Booldata':'True'})
        else:
            return JsonResponse({'Booldata': 'False'})

    if uemail:
        u=Users.objects.filter(user_email=uemail)
        print(u)
        if u:
            return JsonResponse({'Booldata': 'True'})
        else:
            return JsonResponse({'Booldata': 'False'})




def V_test(request):
    return render(request,'test.html')
