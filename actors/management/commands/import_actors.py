import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor

# Esses scripts sempre devem ter uma classe que herda de BaseCommand,
# e um método principal, no caso, handle, que será sobrescrito para
# colocar a nossa lógica.
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',                             # argumento posicional
            type=str,                                # tipo do argumento
            help="Nome do arquivo CSV com atores",   # descrição do argumento
        )
    
    def handle(self, *args, **options):
        file_name = options['file_name']
        
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']
            
                # Isso seria uma espécie de print estilizado do Django command. NOTICE mostra cor vermelha
                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        # SUCCESS mostra cor verde
        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))
