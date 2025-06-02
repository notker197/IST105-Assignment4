from django.shortcuts import render
from .forms import InputForm
import math

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            # Validaciones y lógica
            if a < 1:
                error = "El valor de A es demasiado pequeño."
            elif c < 0:
                error = "El valor de C no puede ser negativo."
            else:
                c_cubed = c ** 3
                if c_cubed > 1000:
                    result = math.sqrt(c_cubed) * 10
                else:
                    if a == 0:
                        error = "No se puede dividir entre cero."
                    else:
                        result = math.sqrt(c_cubed) / a
                if result is not None:
                    result += b
                if b == 0:
                    result = f"{result} (Nota: B es 0, no afectó el resultado)"
        else:
            error = "Formulario inválido. Revisa los datos ingresados."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error
    })
