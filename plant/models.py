from django.db import models

# Represents a botanical family.
class Family(models.Model):
    name = models.CharField(max_length=50, primary_key=True)  # Name of the botanical family.
    introduction = models.CharField(max_length=500, default=None)
    img_path = models.CharField(max_length=50, default=None)

# Represents a botanical genus, linked to a family.
class Genus(models.Model):
    name = models.CharField(max_length=50, primary_key=True)  # Name of the botanical genus.
    family = models.ForeignKey(Family, on_delete=models.CASCADE)  # Link to the Family this Genus belongs to.

# Represents a plant, linked to a genus.
class Plant(models.Model):
    name = models.CharField(max_length=50, primary_key=True)  # Name of the plant.
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)  # Link to the Genus this Plant belongs to.
    location = models.CharField(max_length=50)  # Location where the plant is found.
    introduction = models.TextField(max_length=500)  # Brief introduction about the plant.
    image_path = models.CharField(max_length=50)  # Path to the plant's image.
    
    @property
    def family(self):
        return self.genus.family.name

# Represents a recommendation for a video.
class Recommendation(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, default=None)
    
    @property
    def img_path(self):
        return self.plant.image_path
    
    @property
    def plant_name(self):
        return self.plant.name
