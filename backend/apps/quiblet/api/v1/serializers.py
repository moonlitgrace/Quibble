from rest_framework import exceptions, serializers

from ...models import QuibletModel


class QuibletModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuibletModel
        fields = '__all__'

    def validate_name(self, name):
        if QuibletModel.objects.filter(name__iexact=name).exists():
            raise exceptions.ValidationError(
                f"Quiblet with name {name} already exists (case-insensitive)."
            )

        return name


class QuibletSlimModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuibletModel
        fields = ('name', 'avatar')


class QuibletExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
