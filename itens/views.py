from django.shortcuts import render, redirect, get_object_or_404
from .models import Casas

from .forms import CasasForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def casa_list(request):
    casas = Casas.objects.all()
    return render(request, 'casa.html', {'casas': casas})




@login_required
def casa_new(request):
    form = CasasForm(request.POST, request.FILES, None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('casas_list')
    return render(request, 'casa_form.html', {'form': form})


@login_required
def casas_update(request, id):
    casas = get_object_or_404(Casas, pk=id)
    form = CasasForm(request.POST or None, request.FILES or None, instance=casas)

    if form.is_valid():
        form.save()
        return redirect('casas_list')

    return render(request, 'casa_form.html', {'form': form})

@login_required
def casas_delete(request, id):
    casas = get_object_or_404(Casas, pk=id)
    

    if request.method == 'POST':
        casas.delete()
        return redirect('casas_list')

    return render(request, 'casa_delete_confirm.html', {'casas': casas})
