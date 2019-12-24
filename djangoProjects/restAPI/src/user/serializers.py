"""
Serializer Module for User
"""

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the user object """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        """Default Meta Class"""
        model = get_user_model()
        fields = ('email', 'password', 'password2', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def validate(self, data):
        print(f"data is {data}")
        pass1 = data.get('password')
        pass2 = data.pop('password2', None)
        if pass1 != pass2:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        """Create function of serializer"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update function of serializer"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer class for issuing auth Token"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validating the submitted username and password"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate user with provied credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
