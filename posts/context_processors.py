from .models import Setting

def settings(request):
    settings = Setting.objects.all()    

    context = {}
    for setting in settings:
        context[setting.key] = setting.value

    return {
        'setting': context,
    }

def colors(request):
    return {
        'primary_color': 'teal lighten-2',
    }
