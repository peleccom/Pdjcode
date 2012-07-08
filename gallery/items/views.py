# Create your views here.

from django.views.generic import DetailView
from models import Photo

class PhotoDetailView(DetailView):
    model = Photo

