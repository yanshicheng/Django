from django.shortcuts import render
from app01.models import UserInfor
# Create your views here.
from app01.utils.mypag import Pagination

def indexx(request):
    try:
    # 获取当前页码
        current_page = int(request.GET.get('page',1))
    except Exception as e:
        current_page = 1

    per_age = 10

    data = UserInfor.objects.all()

    # 计算数据
    total_count = data.count()
    # 计算需要多少页
    total_page , more = divmod(total_count,per_age)

    if more:
        total_page += 1

    # 如果访问的页码数超过了总页数,默认显示最后一页
    current_page = total_page if current_page > total_page else current_page
    # 数据切片的开始位置
    start = per_age * (current_page - 1)
    end = current_page * per_age
    # 取到所有数据
    data = UserInfor.objects.all()[start:end]

    # 设置页面最多显示的页码数
    show_page = 11
    # 最多显示页码的一半
    half_show_page = show_page // 2
    # 如果总页面的页码数小于要显示的页码数
    if total_page < show_page:
        show_page_start = 1
        show_page_end = total_page
    # 判断 左边边界
    elif current_page - half_show_page < 1:
        show_page_start = 1
        show_page_end = show_page
    elif current_page + half_show_page > total_page:
        show_page_start = total_page - show_page + 1
        show_page_end = total_page
    else:
    # 页面显示页码的开始
        show_page_start = current_page -half_show_page
        show_page_end = current_page + half_show_page
    # 页面显示页码的结束


    # 生成 html 代码
    page_list = []
    page_list.append('<nav aria-label="Page navigation"><ul class="pagination">')
    # 首页
    page_list.append('<li><a href="/index/?page=1">首页</a></li>')
    page_list.append('<li><a href="/index/?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a>'.format(current_page -1))

    for i in range(show_page_start,show_page_end+1):
        if i == current_page:
            s = ' <li class="active"><a href="/index/?page={0}">{0}</a></li>'.format(i)
        else:
            s = ' <li><a href="/index/?page={0}">{0}</a></li>'.format(i)
        page_list.append(s)

    page_list.append('<li><a href="/index/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a>'.format(current_page +1))
    # 尾页
    page_list.append('<li><a href="/index/?page={}">尾页</a></li>'.format(total_page))
    page_list.append('</ul></nav>')
    page_html = ''.join(page_list)
    return render(request,'index.html',{'data':data,'page_html':page_html})


# 最新
def index(request):

    #取到当前页码
    ret = request.GET.get('page',1)
    # 取到所有要显示的数据
    data_all = UserInfor.objects.all()
    data_count = data_all.count()
    page_obj = Pagination(ret,data_count)

    data = data_all[page_obj.start:page_obj.end]
    page_html = page_obj.page_html
    return render(request, 'index.html', {'data': data,'page_html':page_html})