from django import forms
from .models import Agendamento
from .models import TarifaDia


def _normalizar_texto(valor: str) -> str:
    return "".join(ch for ch in (valor or "").lower() if ch.isalnum())


def servico_usa_tarifa(nome_servico: str) -> bool:
    nome = _normalizar_texto(nome_servico)
    return nome in {"cortesocial", "cortesocialtradicional"}


def _tarifa_por_dia_semana(dia_semana: int) -> str:
    tarifas = list(TarifaDia.objects.all())

    for tarifa in tarifas:
        dias = (tarifa.dias or "").lower()
        if dia_semana in {4, 5} and ("sexta" in dias or "sábado" in dias or "sabado" in dias):
            return f"{tarifa.dias} — {tarifa.preco}"
        if dia_semana in {0, 1, 2, 3} and ("segunda" in dias or "quinta" in dias):
            return f"{tarifa.dias} — {tarifa.preco}"

    return ""


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model  = Agendamento
        fields = ["nome", "telefone", "servico", "data", "horario", "tarifa"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "nome":     "Nome completo",
            "telefone": "WhatsApp",
            "servico":  "Serviço",
            "data":     "Data",
            "horario":  "Horário",
            "tarifa":   "Tarifa",
        }

    def clean_nome(self):
        nome = self.cleaned_data.get("nome", "").strip()
        if len(nome) < 2:
            raise forms.ValidationError("Por favor, informe seu nome completo.")
        return nome

    def clean(self):
        cleaned = super().clean()
        data    = cleaned.get("data")
        horario = cleaned.get("horario")
        servico = cleaned.get("servico")

        if data and horario:
            from django.utils import timezone
            if data < timezone.now().date():
                self.add_error("data", "Não é possível agendar em datas passadas.")

            # Verifica se já existe agendamento confirmado neste slot
            ja_existe = Agendamento.objects.filter(
                data=data,
                horario=horario,
                status__in=[ "confirmado"],
            ).exists()
            if ja_existe:
                self.add_error("horario", "Este horário já está reservado. Escolha outro.")

        if data and servico:
            cleaned["tarifa"] = _tarifa_por_dia_semana(data.weekday()) if servico_usa_tarifa(servico) else ""

        return cleaned
