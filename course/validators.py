from rest_framework import serializers


class VideoLinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if value is not None and 'youtube.com' not in tmp_value.lower():
            raise serializers.ValidationError("В поле должна быть ссылка на видео!")