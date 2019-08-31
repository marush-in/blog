from .models import Setting


def get_setting(request):
    setting = Setting.objects.first()
    return dict(setting=setting)
