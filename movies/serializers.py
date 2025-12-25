from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer

class MovieModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 2000:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 2000.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior do que 200 caracteres.')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True) # many=True porque é uma lista de atores
    genre = GenreSerializer()

    # Adicionando um campo além dos que estão em Movie
    # SerializerMethodField é um campo calculado
    # read_only = serve só para get. Ao cadastrar um filme, ele não deve estar lá
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume'] # ordenamos dessa forma

    # obj é o objeto de movies, onde teremos acesso aos dados de um filme
    def get_rate(self, obj):
        # reviews = obj.reviews.all(stars__lte=3)  --> Todas as reviews menor que 3 estrelas
        # reviews = obj.reviews.all()

        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars
        #     reviews_count = reviews.count()
        #     # arredonda pra 1 casa decimal depois da vírgula
        #     return round(sum_reviews / reviews_count, 1)

        # return None

        # Avg -> average, média
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()