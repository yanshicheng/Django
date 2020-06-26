import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_page.settings")

    import django
    django.setup()

    from app01.models import UserInfor


    # 先创建500个Publisher对象
    obj_list = (UserInfor(username='张三{}'.format(i), addr='上海{}'.format(i)) for i in range(500))
    # bulk_create
    UserInfor.objects.bulk_create(obj_list)
