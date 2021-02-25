from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 100)
#     description = serializers.CharField(max_length = 100)


#     def create(self, validated_data):
#         return Article.objects.create(validated_data)


#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)


# ModelSerializer
# The ModelSerializer class provides a shortcut that lets you automatically create a 
# Serializer class with fields that correspond to the Model fields.

# The ModelSerializer class is the same as a regular Serializer class, except that:
# It will automatically generate a set of fields for you, based on the model.
# It will automatically generate validators for the serializer, 
# such as unique_together validators.
# It includes simple default implementations of .create() and .update().

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']


