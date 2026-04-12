from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
import json

from .models import Configuracao, Servico, Horario, TarifaDia, Plano, Agendamento
from .forms import AgendamentoForm


def _mapa_tarifas_por_dia():
    mapa = {}

    for tarifa in TarifaDia.objects.all():
        valor = f"{tarifa.dias} — {tarifa.preco}"
        dias = (tarifa.dias or "").lower()

        if "segunda" in dias or "quinta" in dias:
            for dia_semana in [1, 2, 3, 4]:
                mapa[dia_semana] = valor

        if "sexta" in dias or "sábado" in dias or "sabado" in dias:
            for dia_semana in [5, 6]:
                mapa[dia_semana] = valor

    return mapa


def index(request):
    config = Configuracao.objects.first()

    # Horários ocupados por data
    agendamentos = Agendamento.objects.filter(
        status__in=[ "confirmado"],
        data__gte=timezone.now().date()
    ).values("data", "horario")

    ocupado = {}
    for a in agendamentos:
        dia = a["data"].isoformat()
        if dia not in ocupado:
            ocupado[dia] = []
        ocupado[dia].append(a["horario"])

    context = {
        "config":          config,
        "servicos_form":   Servico.objects.filter(no_formulario=True),
        "servicos_card":   Servico.objects.filter(no_card=True),
        "horarios":        Horario.objects.all(),
        "tarifas":         TarifaDia.objects.all(),
        "planos":          Plano.objects.prefetch_related("itens").all(),
        "hoje":            timezone.now().date().isoformat(),
        "tarifas_select":  TarifaDia.objects.all(),
        "ocupados_json":   json.dumps(ocupado),
        "tarifas_map_json": json.dumps(_mapa_tarifas_por_dia()),
    }
    return render(request, "barbearia/index.html", context)


def agendar(request):
    if request.method != "POST":
        return redirect("index")

    form = AgendamentoForm(request.POST)
    if form.is_valid():
        agendamento = form.save()
        messages.success(
            request,
            f"Agendamento confirmado! {agendamento.nome} — {agendamento.data} às {agendamento.horario}",
        )
    else:
        for campo, erros in form.errors.items():
            for erro in erros:
                messages.error(request, erro)

    return redirect("index")
