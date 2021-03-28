from users.models import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )
        read_only_fields = (
            'is_admin', 'is_staff',
        )

    def __init__(self, *args, **kwargs):
        super(UserRegisterSerializer, self).__init__(*args, **kwargs)
        

    def validate_username(self, data):
       
        if not User.objects.filter(username=data).exists():
            return data
        raise serializers.ValidationError('This username is already in use')

    def validate_password(self, password):
        if len(password) == 0:
            raise serializers.ValidationError('EMPTY PASSWORD')
        return password

    def save(self, *args, **kwargs):
        self.user = super(UserRegisterSerializer, self).save()
        self.user.set_password(self.validated_data.get('password'))
        self.user.save()
        self.user = authenticate(username=self.user.username, password=self.validated_data['password'])
        self.user.save()
        return self.user


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','password')
        read_only_fields = ('is_admin', 'is_staff')

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)

    def validate(self, attrs):
        self.user = authenticate(username=attrs[User.USERNAME_FIELD], password=attrs['password'])
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError('Account is disabled')
            return attrs
        else:
            raise serializers.ValidationError('Invalid username or password')



class UserSerializer(serializers.HyperlinkedModelSerializer) :
    password = serializers.CharField(write_only=True)
    
    class Meta :
        model = User
        fields = ("id","email" , "username", "password")


