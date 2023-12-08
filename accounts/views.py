from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # 로그인 성공 시 메인으로 이동
            return redirect('../../post/')
        else:
            # 로그인 실패 시 다시 로그인 페이지로 이동
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 정확하지 않습니다.'})
    else:
        return render(request, 'login.html')  # get 요청인 경우에도 로그인 페이지로 이동

# 로그아웃
def logout(request):
    auth.logout(request)
    # 메인페이지로 리다이렉트
    return redirect('../../post/')


# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('../../post/')
        # 비밀번호 일치하지 않는 경우
        return render(request, 'signup.html', {'error': '비밀번호 확인이 일치하지 않습니다.'})
    return render(request, 'signup.html')

# 회원 탈퇴
@login_required
def delete_account(request):
    if request.method == 'POST':
        # 현재 로그인한 사용자 삭제
        request.user.delete()
        messages.success(request, '계정이 성공적으로 삭제되었습니다.')
        return redirect('/accounts/login/')  # 탈퇴 성공 시 로그인 페이지로 이동

    return render(request, 'delete_account.html')

# 마이페이지
def MyPage(request):
    return render(request, 'mypage.html')

