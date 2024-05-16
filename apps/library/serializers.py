from rest_framework import serializers

from apps.library.models import Gallery, GalleryImage, EducationalMaterial


class GallerySerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'first_image', 'created_at')

    def get_first_image(self, obj):
        images = obj.gallery_images.all()
        if images.exists():
            image_path = images.first().image.url
            return self.context['request'].build_absolute_uri(image_path)
        return None


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ('id', 'image')


class GalleryDetailSerializer(serializers.ModelSerializer):
    gallery_images = GalleryImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'description', 'created_at', 'gallery_images')


class EducationalMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalMaterial
        fields = ('id', 'title', 'link')
