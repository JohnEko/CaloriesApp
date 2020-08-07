from django import forms 
from .models import Food

class AddFood(forms.ModelForm):

    class Meta:
        model = Food
        fields = [
                "protein",
                "carbohydrates",
                "cholestrol",
                "fat",
                "fiber",
                "saturated_salt"
                ]