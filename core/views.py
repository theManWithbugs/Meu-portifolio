from email import message
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from core.forms import NomeSobrenomeForm
from core.models import *
from django.core.paginator import Paginator

def home_view(request):
    return render(request, 'home.html')

def form_view(request):
    text = Profile.objects.all()
    paginator = Paginator(text, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'form.html'
    form = NomeSobrenomeForm()  # Crie uma instância do formulário para o caso de GET

    if request.method == 'POST':
        form = NomeSobrenomeForm(request.POST)

        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            if NomeUser.objects.filter(cpf=cpf).exists():
                message.error(request, 'O dado já consta no banco de dados')
                return redirect('form')
            else:
                try:
                    form.save()
                    return HttpResponse('Dados salvos!')
                except Exception as e:
                    return HttpResponse('Não foi possível concluir a operação.')
        else:
            return HttpResponse('Dados do formulário inválidos!')

    # Para o caso de GET ou se o formulário é inválido, renderize o formulário.
    return render(request, template_name, {'formulario': form, 'page_obj': page_obj})

def base_view(request):
    return render(request, 'base.html')

def comments_list(request):
    text = Profile.objects.all()
    paginator = Paginator(text, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'include/paginator.html', {'page_obj': page_obj})

#-------INCLUDES HERE----------#
def perfil_view(request):
    template_name = 'profile/profile_main.html'
    text = Profile.objects.all()
    paginator = Paginator(text, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, template_name, {'page_obj': page_obj})


    






        
       



        
        


    




