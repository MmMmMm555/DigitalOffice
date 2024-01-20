from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        if self.user.profil:
            name = self.user.profil.first_name
            last_name = self.user.profil.last_name
        else:
            name = None
            last_name = None
        return {
            "id": self.user.id,
            "email": self.user.email,
            "username": self.user.username,
            "role": self.user.role,
            "first_name": name,
            "last_name": last_name,
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