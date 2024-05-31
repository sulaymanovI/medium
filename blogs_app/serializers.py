from .models import Blog, UploadImage
from rest_framework.serializers import Serializer, ModelSerializer,SerializerMethodField

class UploadImageSerializer(ModelSerializer):
    
    class Meta:
        model=UploadImage
        fields=['pk', 'file']

    def to_representation(self, instance):
        return instance.file.url

class BlogSerializer(ModelSerializer):
    images = SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author','created_at', 'updated_at','images']
    
    def get_images(self, obj):
        images = obj.images.all()
        return UploadImageSerializer(instance=images, many=True).data
