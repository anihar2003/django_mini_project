from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse

def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        message = request.POST.get('message')

        if recipient_email and message:
            try:
                email = EmailMessage(
                    subject='Test Email from Django',
                    body=message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[recipient_email],
                )
                email.send()
                return render(request, 'home.html', {'message': 'Email sent successfully'})
            except Exception as e:
                return render(request, 'home.html', {'message': f'Error: {str(e)}'})
        else:
            return render(request, 'home.html', {'message': 'Invalid input'})
    return render(request, 'home.html')
