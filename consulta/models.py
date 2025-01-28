from django.db import models
from django.core.exceptions import ValidationError
from tutores.models import Tutor
from clientes.models import Clientes  # Importing Clientes class


class Consulta(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='consultas_tutor')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='consultas_cliente')  # New field added
    data = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    
    # EXAME A DISTÂNCIA
    COMPORTAMENTO_CHOICES = [
        ('D', 'Depressivo'),
        ('E', 'Excitado'),
    ]
    comportamento = models.CharField(max_length=1, choices=COMPORTAMENTO_CHOICES)
    voz = models.CharField(max_length=10, verbose_name='Voz')
    
    ALIMENTACAO_CHOICES = [
        ('N', 'Normal'),
        ('A', 'Alterada'),
    ]
    alimentacao = models.CharField(max_length=10, choices=ALIMENTACAO_CHOICES, verbose_name='Alimentação')
    
    APETITE_CHOICES = [
        ('B', 'Bom'),
        ('R', 'Reduzido'),
    ]
    apetite = models.CharField(max_length=10, choices=APETITE_CHOICES)
    
    preensao = models.CharField(max_length=10, verbose_name='Prensão')
    mastigacao = models.CharField(max_length=10, verbose_name='Mastigação')
    degluticao = models.CharField(max_length=10, verbose_name='Deglutição')
    vomitos = models.CharField(max_length=10, verbose_name='Vômitos')
    regurgitacao = models.CharField(max_length=10, verbose_name='Regurgitação')
    excrecao = models.CharField(max_length=10, verbose_name='Excreção', default="N/A")
    constipacao = models.CharField(max_length=10, verbose_name='Constipação', default="N/A")
    diarreia = models.CharField(max_length=10, verbose_name='Diarreia')
    miccao = models.CharField(max_length=10, verbose_name='Micção')
    
    COND_CORP_CHOICES = [
        ('C', 'Caquético'),
        ('M', 'Magro'),
        ('N', 'Normal'),
        ('S', 'Sobrepeso'),
        ('O', 'Obeso'),
    ]
    condicao_corporal = models.CharField(max_length=1, choices=COND_CORP_CHOICES, verbose_name='Condição Corporal', default='N')    
    postura = models.CharField(max_length=20, verbose_name='Postura', default="N/A")
    marcha = models.CharField(max_length=25, verbose_name='Marcha', default="N/A")
    pele = models.CharField(max_length=25, verbose_name='Pele', default="N/A")
    cabeca = models.CharField(max_length=25, verbose_name='Cabeça', default="N/A")
    olhos = models.CharField(max_length=25, verbose_name='Olhos', default="N/A")
    salivacao = models.CharField(max_length=25, verbose_name='Salivação', default="N/A")
    pescoco = models.CharField(max_length=25, verbose_name='Pescoço', default="N/A")
    torax = models.CharField(max_length=25, verbose_name='Torax', default="N/A")
    abdomem = models.CharField(max_length=25, verbose_name='Abdomem', default="N/A")
    genitalia_externa = models.CharField(max_length=25, verbose_name='Genitália Externa', default="N/A")
    glandulas_mamarias = models.CharField(max_length=25, verbose_name='Glândulas Mamárias', default="N/A")
    
    # EXAME DE PERTO
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Temperatura', null=True, blank=True)
    frequencia_cardiaca = models.IntegerField(verbose_name='Frequência Cardíaca', null=True, blank=True)
    frequencia_respiratoria = models.IntegerField(verbose_name='Frequência Respiratória', null=True, blank=True)
    
    circ_periferica_hidratacao = models.TextField(verbose_name='Circulação Periférica e Hidratação', default="N/A")
    
    MUCOSAS_CHOICES = [
        ('P', 'Pálidas'),
        ('I', 'Ictéricas'),
        ('N', 'Normal'),
        ('C', 'Congesta'),
        ('H', 'Hipocorada'),
    ]
    mucosas = models.CharField(max_length=1, choices=MUCOSAS_CHOICES, verbose_name='Mucosas', default='N')
    
    torax_perto = models.TextField(verbose_name='Torax', default="N/A")
    abdomem_perto = models.TextField(verbose_name='Abdomem Perto', default="N/A")
    cabeca_pescoco = models.TextField(verbose_name='Cabeça e Pescoço', default="N/A")
    sistema_urinario = models.TextField(verbose_name='Sistema Urinário', default="N/A")
    trato_reprodutor = models.TextField(verbose_name='Trato Reprodutor', default="N/A")
    glandulas_mamarias_perto = models.TextField(verbose_name='Glândulas Mamárias', default="N/A")
    sist_musculo_esqueletico = models.TextField(verbose_name='Sistema Músculo Esquelético', default="N/A")
    sistema_nervoso = models.TextField(verbose_name='Sistema Nervoso', default="N/A")
    diagnostico = models.TextField(verbose_name='Diagnóstico', default="N/A")
    tratamento = models.TextField(verbose_name='Tratamento', default="N/A")

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        
    def clean(self):
        if self.cliente.tutor != self.tutor:
            raise ValidationError("O tutor selecionado não corresponde ao tutor do cliente.")
        
    def __str__(self):
        return f"{self.data} - {self.tutor}"
