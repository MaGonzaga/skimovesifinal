from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes

from .forms import PersonForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def persons_list(request):
    clientes = Clientes.objects.all()
    return render(request, 'person.html', {'clientes': clientes})




@login_required
def persons_new(request):
    form = PersonForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    clientes = get_object_or_404(Clientes, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=clientes)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_delete(request, id):
    clientes = get_object_or_404(Clientes, pk=id)
    

    if request.method == 'POST':
        clientes.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'clientes': clientes})
