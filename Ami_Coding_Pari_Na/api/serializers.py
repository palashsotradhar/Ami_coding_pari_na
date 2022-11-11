from rest_framework import serializers
from khoj_the_search.models import khojm

class apis(serializers.ModelSerializer):
    class Meta:
        model = khojm
        fields = ['timestamp','input_values']
