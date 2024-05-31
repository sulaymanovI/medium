from rest_flex_fields.serializers import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Blog , BlogImages

class BlogSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author','created_at', 'updated_at']
        expandable_fields={
            'image' : ('uesrs_app.BlogImageSerializer' , {'many' : True})
        }


class BlogImageSerializer(FlexFieldsModelSerializer):
    image =  VersatileImageFieldSerializer(
        sizes=[
            ('full_size' ,'url'),
            ('thumbnail' , 'thumbnail__100x100')
        ]
    )

    class Meta:
        model=BlogImages
        fields=['pk' , 'image']
