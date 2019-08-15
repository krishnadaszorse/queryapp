from django.db import models

class Query(models.Model):
    query = models.TextField(verbose_name=u'Sql query',max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def get_query_set(self):
    #     return self.objects.raw(self.query)
    
    # def get_query_data(self):
    #     query_set = self.get_query_set()
    #     columns = query_set.columns
    #     data = [(getattr(item, col) for col in columns) for item in query_set]
    #     return columns, data
