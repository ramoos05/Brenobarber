import json
from datetime import date, timedelta

from django.contrib import admin
from django.db.models import Count
from unfold.admin import ModelAdmin
from unfold.decorators import display

from .models import Configuracao, Servico, Horario, TarifaDia, Plano, Agendamento


# ====================== DASHBOARD CALLBACK ======================
def dashboard_callback(request, context):
    """Callback principal do Unfold para o dashboard"""

    hoje = date.today()
    mes = hoje.month
    ano = hoje.year
    inicio_mes = hoje.replace(day=1)
    trinta_dias_atras = hoje - timedelta(days=29)

    # ── KPIs ─────────────────────────────────────────────────────────────
    total_hoje = Agendamento.objects.filter(data=hoje).count()
    confirmados_mes = Agendamento.objects.filter(
        data__month=mes, data__year=ano, status="confirmado"
    ).count()
    cancelados_mes = Agendamento.objects.filter(
        data__month=mes, data__year=ano, status="cancelado"
    ).count()

    # ── Receita do mês ───────────────────────────────────────────────────
    servicos_map = {
        s.nome.strip().lower(): _extrair_preco(s.preco)
        for s in Servico.objects.all()
    }

    def _extrair_preco_servico(nome_servico: str) -> float:
        nome_lower = nome_servico.strip().lower()

        # match exato
        if nome_lower in servicos_map:
            return servicos_map[nome_lower]

        # fallback opcional
        for nome, preco in servicos_map.items():
            if nome in nome_lower:
                return preco

        return 0.0
    # ── Receita do mês ───────────────────────────────────────────────────
    SERVICOS_COM_TARIFA = ["corte social"]

    confirmados_mes_qs = Agendamento.objects.filter(
        data__month=mes, data__year=ano, status="confirmado"
    ).values("servico", "tarifa")

    receita_total = 0.0
    receita_por_servico = {}

    for item in confirmados_mes_qs:
        nome_servico = item["servico"] or "Sem serviço"
        usa_tarifa = any(s in nome_servico.strip().lower() for s in SERVICOS_COM_TARIFA)

        if usa_tarifa and item["tarifa"]:
            preco = _extrair_preco(item["tarifa"])
        else:
            preco = _extrair_preco_servico(nome_servico)

        if nome_servico not in receita_por_servico:
            receita_por_servico[nome_servico] = {"qtd": 0, "receita": 0.0}

        receita_por_servico[nome_servico]["qtd"] += 1
        receita_por_servico[nome_servico]["receita"] += preco
        receita_total += preco

    receita_por_servico = sorted([
        {
            "servico": nome,
            "qtd": dados["qtd"],
            "receita": f"{dados['receita']:.2f}".replace(".", ","),
        }
        for nome, dados in receita_por_servico.items()
    ], key=lambda x: x["qtd"], reverse=True)
    # ── Gráfico linha — últimos 30 dias ───────────────────────────────────
    agendamentos = Agendamento.objects.filter(
        data__gte=trinta_dias_atras,
        data__lte=hoje
    )

    from collections import Counter
    contagem = Counter(a.data for a in agendamentos)

    labels, valores = [], []
    for i in range(30):
        dia = trinta_dias_atras + timedelta(days=i)
        labels.append(dia.strftime("%d/%m"))
        valores.append(contagem.get(dia, 0))

    # ── Gráfico pizza ─────────────────────────────────────────────────────
    por_servico = (
        Agendamento.objects
        .filter(data__month=mes, data__year=ano, status="confirmado")
        .values("servico")
        .annotate(total=Count("id"))
        .order_by("-total")[:6]
    )
    pizza_labels = [s["servico"] or "Sem serviço" for s in por_servico]
    pizza_valores = [s["total"] for s in por_servico]

    # ── Próximos hoje ─────────────────────────────────────────────────────
    proximos = Agendamento.objects.filter(
        data=hoje,
        status__in=["confirmado"]
    ).order_by("horario")[:8]

    # Mês por extenso
    MESES = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    context.update({
        "kpis": {
            "hoje": total_hoje,
            "confirmados_mes": confirmados_mes,
            "cancelados_mes": cancelados_mes,
            "receita_mes": f"{receita_total:.2f}".replace(".", ","),
        },
        "receita_por_servico": receita_por_servico,
        "chart_labels_json": json.dumps(labels),
        "chart_valores_json": json.dumps(valores),
        "pizza_labels_json": json.dumps(pizza_labels),
        "pizza_valores_json": json.dumps(pizza_valores),
        "proximos_hoje": proximos,
        "hoje_fmt": hoje.strftime("%d/%m/%Y"),
        "mes_nome": f"{MESES[mes]} de {ano}",
    })

    return context


# Função auxiliar (usada acima)
def _extrair_preco(preco_str: str) -> float:
    import re
    match = re.search(r"[\d]+(?:[.,]\d+)?", preco_str.replace(",", "."))
    return float(match.group().replace(",", ".")) if match else 0.0


# ====================== REGISTER ADMIN ======================

@admin.register(Configuracao)
class ConfiguracaoAdmin(ModelAdmin):
    fieldsets = [
        ("Identidade",    {"fields": ["nome", "slogan"]}),
        ("Contato",       {"fields": ["telefone", "whatsapp", "instagram"]}),
        ("Localização",   {"fields": ["endereco", "cidade"]}),
        ("Texto do Site", {"fields": ["titulo_hero", "titulo_destaque", "subtitulo"]}),
    ]


@admin.register(Plano)
class PlanoAdmin(ModelAdmin):
    list_display  = ["nome", "preco", "periodo", "destaque", "ordem"]
    list_editable = ["ordem", "destaque"]


@admin.register(Servico)
class ServicoAdmin(ModelAdmin):
    list_display  = ["nome", "preco", "tempo", "no_formulario", "no_card", "padrao", "ordem"]
    list_editable = ["preco", "tempo", "no_formulario", "no_card", "padrao", "ordem"]


@admin.register(Horario)
class HorarioAdmin(ModelAdmin):
    list_display  = ["hora", "display_status", "ordem"]
    list_editable = ["ordem"]

    @display(description="Status", label={"livre": "success", "ocupado": "danger"})
    def display_status(self, obj):
        return "ocupado" if obj.ocupado else "livre"


@admin.register(TarifaDia)
class TarifaDiaAdmin(ModelAdmin):
    list_display  = ["dias", "preco", "sigla", "ordem"]
    list_editable = ["preco", "sigla", "ordem"]


@admin.register(Agendamento)
class AgendamentoAdmin(ModelAdmin):
    list_display    = ["nome", "telefone", "servico", "data", "horario", "display_status", "criado_em"]
    list_filter     = ["status", "data"]
    search_fields   = ["nome", "telefone"]
    readonly_fields = ["criado_em"]
    date_hierarchy  = "data"
    ordering        = ["-data", "horario"]

    @display(
        description="Status",
        label={ "confirmado": "success", "cancelado": "danger"},
    )
    def display_status(self, obj):
        return obj.status
