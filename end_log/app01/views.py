from django.shortcuts import render,HttpResponse,redirect
from django import views
from app01.models import UserInfo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import JsonResponse
from app01.forms import RegForm



class login(views.View):
    def get(self,request):
        rep = render(request, 'login.html')
        return rep
    def post(self,request):
        print(request.POST)
        username = request.POST.get('userName')
        pwd = request.POST.get('passWord')
        # 获取用户是否勾选七天免登录
        remember_7 = request.POST.get('check1',None)
        user_obj = UserInfo.objects.filter(username=username,password=pwd).first()
        if user_obj:
            # 获取用户上个页面跳转的 地址 如果没有获取到则设置 默认值
            return_url = request.GET.get('return_Url','/home/')
            print(return_url)
            # 设置 session 字典属性
            request.session['user'] = user_obj.username
            request.session['age'] = 88
            # 进行判断
            if remember_7:
                # 如果用户勾选七天免登录则设置 session 过期时间
                request.session.set_expiry(7*24*60*60)
            else:
                # 如果用户没有勾选则设置 session 过期时间为0
                request.session.set_expiry(0)

            return redirect(return_url)
        return render(request, 'login.html',{'msg':'用户名或密码错误!'})





class register(views.View):
    def get(self,request):
        form_obj = RegForm()
        return render(request,'register.html', {'form':form_obj},)
    def post(self,request):
        res = {'code':0}
        # 利用 post 提交的数据实例化 form 类
        form_obj = RegForm(request.POST)
        print(form_obj)
        # 校验数据的有效性
        if form_obj.is_valid():
            # 移除 re_password
            form_obj.cleaned_data.pop('re_password')
            UserInfo.objects.create(**form_obj.cleaned_data)
            res['url'] = '/login/'
        else:
            # 数据有问题
            res['code'] = 1
            res['error_msg'] = form_obj.errors
        return JsonResponse(res)




def home(request):
    if request.method == "POST":
        request.session.flush() # 删除当前 session 并让 cookie 失效
        return redirect('/login/')
    return render(request, 'home.html')

def test(request):
    return HttpResponse('Test - OK')

class UserinfoView(views.View):
    # 取消 csrf 跨站请求伪造限制
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserinfoView,self).dispatch(request, *args, **kwargs)
    def get(self,request):
        return render(request,'userinfo.html')
    def post(self,request):
        request.session.flush()  # 删除当前 session 并让 cookie 失效
        return redirect('/login/')