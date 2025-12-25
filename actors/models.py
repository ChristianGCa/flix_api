from django.db import models

# Um valor bruto (USA) e um valor legível (Estados Unidos)
# No banco de dados, será salvo o valor bruto.
NATIONALITY_CHOICES = (
   ('USA', 'Estados Unidos'),
   ('BRAZIL', 'Brasil'),

)

class Actor(models.Model):
    # Se não passamos null e blank, por padrão é False. Ou seja, esse campo é obrigatório.
    name = models.CharField(max_length=200) 
    birthday = models.DateField(null=True, blank=True) # esse não
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name