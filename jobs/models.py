from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    url = models.URLField(max_length=500, unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    # AI generated fields
    ai_summary = models.TextField(blank=True, null=True)
    match_score = models.IntegerField(default=0) # 0-100
    skills_found = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return f"{self.title} at {self.company}"
