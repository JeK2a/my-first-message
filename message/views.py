from django.shortcuts import render
from django.utils import timezone
from .models import Message


def message_list(request):
    messages = Message.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'message/message_list.html', {'messages': messages})


