from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.conf import settings
class CheckLogin(MiddlewareMixin):
    def process_request(self,request):
        # 判断 WHITE_URLS 变量是否在 settings 配置文件中, 如果不在则设置为空列表.
        white_urls = settings.WHITE_URLS if settings.WHITE_URLS else []
        # 判断访问的URL 是否在白名单中.如果存在则返回 None
        if request.path_info in white_urls:
            return None
        # 如果访问 URL 不在白名单中则在 session 中取用户名判断用户是否登录
        user_name = request.session.get('user',None)
        # 如果没有取到则进行跳转.
        if not user_name:
            return_url = request.path_info
            return redirect('/login/?return_Url={}'.format(return_url))

# class M2(MiddlewareMixin):
#     def process_request(self,request):
#         print(request)
#         print('in M2')