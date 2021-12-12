from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
# Register new account
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Tạo tài khoản thành công, vui lòng kiểm tra email để kích hoạt tài khoản')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Activate registration
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        #return HttpResponse('Cảm ơn bạn đã xác nhận email. Tài khoản của bạn đã được kích hoạt')
    else:
        return HttpResponse('Liên kết kích hoạt tài khoản không hợp lệ!')

def loginUser(request):

    if request.user.is_authenticated:

        return redirect('profile')

    else:

        form = SignupForm()



        if request.method == 'POST':

            username = request.POST.get('username')

            password = request.POST.get('password1')

            user = auth.authenticate(username=username, password=password)



            if user:


                if user.is_active == False:

                    return HttpResponse('Vui lòng xác nhận email để hoàn tất quá trình kích hoạt tài khoản')

                else:

                    login(request, user)

                    return redirect('home')

            else:

                messages.info(request, 'Tên đăng nhập hoặc mật khẩu không hợp lệ hoặc tài khoàn chưa được kích hoạt')



        context = {'form': form}

        return render(request, 'login.html', context)


#Logout
def logoutUser(request):
    logout(request)
    return redirect('login')

#Profile
def profileUser(request):
    return render(request, 'profile.html')
