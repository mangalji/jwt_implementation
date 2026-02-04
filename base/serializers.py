from rest_framework import serializers
from .models import Advocate, Company

class CompanySerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        # fields = "__all__"
        fields = ["name","bio","employee_count"]
        # fields = "__all__"

    def get_employee_count(self,obj):
        # count = 0
        count = obj.advocate_set.count()
        return count

class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        # in the fields attribute you specify that which model field or fields you want to show
        
        fields = ["username","bio","name","profile_pic","twitter_api","company"] 
        # fields = '__all__'
        # sometimes you show the limited fields because in many models there are many fields 
        # like password or created_at, but you can't show these fields for everyone 
        # so you wants to hide them, for this reason you want to show only some limited fields. 
        # But, at this stage we only have 2 fields which we want to show so if we want to show 
        # these all fields we use the '__all__' function in value, that's why we use this method.

