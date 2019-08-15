import sqlite3
from django import forms
from django.conf import settings
from .models import Query
temp_db = sqlite3.connect(settings.DATABASES['default'].get('NAME'), check_same_thread=False)


class QureyForm(forms.Form):
    query = forms.CharField(
        label="Query",
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=True,  # Note: validators are not run against empty fields
    )
    
    def clean_query(self):
        stmnt = self.cleaned_data.get('query', '')
        try:
            temp_db.execute(stmnt)
        except (Exception,sqlite3.OperationalError) as e:
            raise forms.ValidationError("Bad statement:'%s'" % str(e))
        return stmnt