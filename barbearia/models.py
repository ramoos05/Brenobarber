from django.db import models


class Configuracao(models.Model):
    """Informações gerais da barbearia — edite pelo admin."""
    nome            = models.CharField(max_length=100, default="Breno Barber")
    slogan          = models.CharField(max_length=200, default="Estilo, Qualidade e Tradição em cada corte")
    endereco        = models.CharField(max_length=200, default="Rua Manoel de Oliveira Ramos, 212")
    cidade          = models.CharField(max_length=100, default="Florianópolis · SC")
    telefone        = models.CharField(max_length=20,  default="(48) 99183-8244")
    whatsapp        = models.CharField(max_length=20,  default="5548991838244", help_text="Só números, com DDI. Ex: 5548991838244")
    instagram       = models.CharField(max_length=100, default="@breno_barberr_")
    titulo_hero     = models.CharField(max_length=200, default="Estilo. Qualidade.")
    titulo_destaque = models.CharField(max_length=100, default="Tradição.", help_text="Palavra em destaque no título")
    subtitulo       = models.TextField(default="Cada detalhe importa — da primeira passada da navalha ao toque final.")

    class Meta:
        verbose_name        = "Configuração"
        verbose_name_plural = "Configurações"

    def __str__(self):
        return self.nome


class Servico(models.Model):
    """Serviços que aparecem nos cards e no formulário de agendamento."""
    nome          = models.CharField(max_length=100)
    preco         = models.CharField(max_length=30, help_text="Ex: R$ 40 ou R$ 40–50")
    tempo         = models.CharField(max_length=30, help_text="Ex: ~40 min")
    no_formulario = models.BooleanField(default=True,  help_text="Aparece como opção no formulário de agendamento?")
    no_card       = models.BooleanField(default=True,  help_text="Aparece nos cards de serviço da página?")
    padrao        = models.BooleanField(default=False, help_text="Vem selecionado por padrão no formulário?")
    ordem         = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name        = "Serviço"
        verbose_name_plural = "Serviços"
        ordering            = ["ordem", "nome"]

    def __str__(self):
        return f"{self.nome} — {self.preco}"


class Horario(models.Model):
    """Slots de horário disponíveis no formulário."""
    hora    = models.CharField(max_length=10, help_text="Ex: 09:00")
    ocupado = models.BooleanField(default=False, help_text="Marque para bloquear este horário")
    ordem   = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name        = "Horário"
        verbose_name_plural = "Horários"
        ordering            = ["ordem", "hora"]

    def __str__(self):
        return f"{self.hora} {'(ocupado)' if self.ocupado else '(livre)'}"


class TarifaDia(models.Model):
    """Tarifas por dia da semana."""
    dias          = models.CharField(max_length=100, help_text="Ex: Segunda a Quinta")
    preco         = models.CharField(max_length=20,  help_text="Ex: R$ 40")
    descricao     = models.CharField(max_length=100, default="Corte tradicional")
    sigla         = models.CharField(max_length=5,   help_text="Ex: S–Q (aparece no ícone)", default="S–Q")
    link_whatsapp = models.CharField(max_length=200, blank=True, help_text="Mensagem pré-preenchida do botão Agendar")
    ordem         = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name        = "Tarifa por Dia"
        verbose_name_plural = "Tarifas por Dia"
        ordering            = ["ordem"]

    def __str__(self):
        return f"{self.dias} — {self.preco}"


class Plano(models.Model):
    """Planos mensais."""
    nome     = models.CharField(max_length=100)
    preco    = models.CharField(max_length=20, help_text="Ex: R$110")
    periodo  = models.CharField(max_length=100, help_text="Ex: Segunda a Sábado")
    destaque = models.BooleanField(default=False, help_text="Borda vermelha — plano em destaque")
    ordem    = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name        = "Plano"
        verbose_name_plural = "Planos"
        ordering            = ["ordem"]

    def __str__(self):
        return f"{self.nome} — {self.preco}"


class ItemPlano(models.Model):
    """Itens da lista de cada plano."""
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE, related_name="itens")
    texto = models.CharField(max_length=200)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name        = "Item do Plano"
        verbose_name_plural = "Itens do Plano"
        ordering            = ["ordem"]

    def __str__(self):
        return self.texto


class Agendamento(models.Model):
    """Agendamentos feitos pelo formulário do site."""
    STATUS = [
        ("confirmado", "Confirmado"),
        ("cancelado", "Cancelado"),
    ]

    nome      = models.CharField(max_length=100)
    telefone  = models.CharField(max_length=20, blank=True)
    servico   = models.CharField(max_length=100)
    data      = models.DateField()
    horario   = models.CharField(max_length=10)
    tarifa    = models.CharField(max_length=50, blank=True)
    status    = models.CharField(max_length=20, choices=STATUS, default="confirmado")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering            = ["-data", "horario"]

    def __str__(self):
        return f"{self.nome} — {self.data} às {self.horario}"
