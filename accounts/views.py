from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# 로그인이 되어있지 않을 시에는 settings.LOGIN_URL로 이동
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')