from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(null=True, blank=True, upload_to="post_images")

	def __str__(self):
		return self.title

	def get_detail_url(self):
		return reverse("more:detail", kwargs={"post_id":self.id})

	class Meta:
		ordering = ['title']