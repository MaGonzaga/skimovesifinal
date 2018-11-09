

from django.shortcuts import render, redirect, get_object_or_404
from .models import Corretores

from .forms import CorreForm

from django.contrib.auth.decorators import login_required


@login_required
def corre_list(request):
    corretores = Corretores.objects.all()
    return render(request, 'corre.html', {'corretores': corretores})

@login_required
def corre_new(request):
    form = CorreForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('corre_list')
    return render(request, 'corre_form.html', {'form': form})

@login_required
def corre_update(request, id):
    corretores = get_object_or_404(Corretores, pk=id)
    form = CorreForm(request.POST or None, request.FILES or None, instance=corretores)

    if form.is_valid():
        form.save()
        return redirect('corre_list')

    return render(request, 'corre_form.html', {'form': form})
    
@login_required
def corre_delete(request, id):
    corretores = get_object_or_404(Corretores, pk=id)

    if request.method == 'POST':
        corretores.delete()
        return redirect('corre_list')
    
    return render(request, 'corre_delete_confirm.html', {'corretores': corretores})


