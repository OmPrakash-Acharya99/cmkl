from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from embed_video.fields import EmbedVideoField

# Custom validator to ensure the name is unique
def validate_unique_name(value):
    if Tools.objects.filter(name__iexact=value).exists():
        raise ValidationError(f"The name '{value}' is already in use.")

# Tools table
class Tools(models.Model):
    Category = models.CharField(max_length=100)
    tool_id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    name = models.CharField(max_length=100, validators=[validate_unique_name])
    descriptions = models.CharField(max_length=200)
    download_link = models.URLField()
    Website_link = models.URLField()
    License = models.CharField(max_length=100)
    Platforms = models.CharField(max_length=100)

    class Meta:
        ordering = ['-tool_id']  # Display the latest items at the top

    def __str__(self):
        return self.name

# Training video table
class Training_video(models.Model):
    Category = models.CharField(max_length=100)
    Video_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=2000)
    Video_URL = EmbedVideoField()
    Skill_levels = models.CharField(max_length=100)
    pdf_field = models.FileField(upload_to='pdfs/', default='pdfs/default.pdf')

    class Meta:
        ordering = ['-Video_id']  # Display the latest items at the top

    def __str__(self):
        return self.Title
