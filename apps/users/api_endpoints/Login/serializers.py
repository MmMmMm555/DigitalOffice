from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        return {
            "id": self.user.id,
            "email": self.user.email,
            "role": self.user.role,
            **attrs,
        }
    # @classmethod
    # def get_token(cls, user):
    #     token = super(MyTokenObtainPairSerializer, cls).get_token(user)

    #     # Add custom claims
    #     token['user'] = {
    #         'username': user.username,
    #         'id': user.id,
    #         'email': user.email,
    #         'role': user.role,
    #         }
    #     return token