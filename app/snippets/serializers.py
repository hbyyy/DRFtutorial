from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICE, STYLE_CHOICE, Snippet


# class SnippetSerializer(serializers.Seriaserilizer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=True)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICE, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICE, default='friendly')
#
#     def create(self, validated_data):
#         """
#             create and return a new "Snippet" instance, given the validated data
#         """
#
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#             update and return an existing "Snippet" instance, given the validated data
#         """
#
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
