from datetime import timedelta

from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import AgendamentoForm
from .models import Agendamento, Configuracao, Horario, Plano, Servico, TarifaDia


class AgendamentoFormTests(TestCase):
    def setUp(self):
        TarifaDia.objects.create(dias="Segunda a Quinta", preco="R$ 45", ordem=1)
        TarifaDia.objects.create(dias="Sexta e Sábado", preco="R$ 50", ordem=2)

    def test_aplica_tarifa_de_sexta_para_corte_social(self):
        sexta = timezone.localdate()
        while sexta.weekday() != 4:
            sexta += timedelta(days=1)

        form = AgendamentoForm(
            data={
                "nome": "Patrick",
                "telefone": "48999999999",
                "servico": "Corte social",
                "data": sexta.isoformat(),
                "horario": "19:00",
                "tarifa": "",
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["tarifa"], "Sexta e Sábado — R$ 50")

    def test_nao_permite_horario_ja_confirmado(self):
        hoje = timezone.localdate() + timedelta(days=1)
        Agendamento.objects.create(
            nome="Cliente 1",
            telefone="48999999999",
            servico="Corte social",
            data=hoje,
            horario="10:00",
            tarifa="Segunda a Quinta — R$ 45",
            status="confirmado",
        )

        form = AgendamentoForm(
            data={
                "nome": "Cliente 2",
                "telefone": "48888888888",
                "servico": "Corte social",
                "data": hoje.isoformat(),
                "horario": "10:00",
                "tarifa": "",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("horario", form.errors)


class BarbeariaViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.config = Configuracao.objects.create(nome="Breno Barber")
        self.servico = Servico.objects.create(
            nome="Corte social",
            preco="R$ 45",
            tempo="40 min",
            no_formulario=True,
            no_card=True,
            padrao=True,
            ordem=1,
        )
        self.horario = Horario.objects.create(hora="09:00", ocupado=False, ordem=1)
        TarifaDia.objects.create(dias="Segunda a Quinta", preco="R$ 45", ordem=1)
        TarifaDia.objects.create(dias="Sexta e Sábado", preco="R$ 50", ordem=2)
        Plano.objects.create(nome="Plano Mensal", preco="R$ 110", periodo="Segunda a Sábado", ordem=1)

    def test_home_carrega_com_contexto_principal(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Agendar Horário")
        self.assertIn("ocupados_json", response.context)
        self.assertIn("tarifas_map_json", response.context)

    def test_post_agendamento_cria_registro(self):
        sexta = timezone.localdate()
        while sexta.weekday() != 4:
            sexta += timedelta(days=1)

        response = self.client.post(
            reverse("agendar"),
            data={
                "nome": "Novo Cliente",
                "telefone": "48911111111",
                "servico": "Corte social",
                "data": sexta.isoformat(),
                "horario": "09:00",
                "tarifa": "",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        agendamento = Agendamento.objects.get(nome="Novo Cliente")
        self.assertEqual(agendamento.status, "confirmado")
        self.assertEqual(agendamento.tarifa, "Sexta e Sábado — R$ 50")
