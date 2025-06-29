from django.shortcuts import render
from .models import GalleryImage, Category

# Create your views here.
def gallery_view(request):
    selected_category = request.GET.get('category')
    print("Selected:", selected_category)

    categories = Category.objects.all()

    if selected_category and selected_category != 'Home':
        images = GalleryImage.objects.filter(category__name__iexact=selected_category)
    else:
        images = GalleryImage.objects.all()

    return render(request, 'gallery.html', {
        'images': images,
        'categories': categories,
        'selected_category': selected_category or 'Home',
    })

    