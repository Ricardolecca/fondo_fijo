from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from .models import Movimiento, Alerta
from .forms import MovimientoForm
import datetime


@login_required
def dashboard(request):

    movimientos = Movimiento.objects.filter(
        usuario=request.user
    ).order_by('-fecha')

    ingresos = movimientos.filter(
        tipo='INGRESO'
    ).aggregate(Sum('valor'))['valor__sum'] or 0

    gastos = movimientos.filter(
        tipo='GASTO'
    ).aggregate(Sum('valor'))['valor__sum'] or 0

    saldo = ingresos - gastos

    # KPI
    porcentaje_gasto = (
        
        (gastos / ingresos) * 100
        if ingresos > 0 else 0
    )

    # ALERTAS
    hoy = datetime.date.today()

    alertas = Alerta.objects.filter(
        usuario=request.user
    )

    for alerta in alertas:

        gastos_mes = movimientos.filter(
            tipo='GASTO',
            fecha__month=hoy.month,
            fecha__year=hoy.year
        )

        if alerta.categoria:
            gastos_mes = gastos_mes.filter(
                categoria=alerta.categoria
            )

        total_mes = sum(g.valor for g in gastos_mes)

        if total_mes > alerta.limite_mensual:

            messages.warning(
                request,
                f'⚠️ Superaste el límite mensual'
            )

    context = {
        'movimientos': movimientos,
        'ingresos': ingresos,
        'gastos': gastos,
        'saldo': saldo,
        'porcentaje_gasto': porcentaje_gasto,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


@login_required
def movimientos_view(request):

    form = MovimientoForm(
        request.POST or None
    )

    if form.is_valid():

        movimiento = form.save(commit=False)

        movimiento.usuario = request.user

        movimiento.save()

        return redirect('dashboard')

    movimientos = Movimiento.objects.filter(
        usuario=request.user
    ).order_by('-fecha')

    return render(
        request,
        'movimientos.html',
        {
            'form': form,
            'movimientos': movimientos
        }
    )