from rest_framework import serializers
from wapp.models import students

class studentsSerializer(serializers.ModelSerializer):
    #create a class meta
    class Meta:
        model=students
 #       fields= ('firstname','lastname')
        fields= '__all__'