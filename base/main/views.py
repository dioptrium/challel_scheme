from django.shortcuts import render

def main(request):
    return render(request, 'index.html')

def loginPage(request):
   
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect ('main_page')
            else:
                messages.info(request, 'Имя или пароль неверны')
            
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
