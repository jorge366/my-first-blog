from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

#ver que no haya espacios en blanco antes sino tabuladores

def post_list(request):
		aaa = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		return render(request, 'blog/post_list.html', { 'v_html': aaa })
		
def post_detail(request, pk):
		detalle = get_object_or_404(Post, pk=pk)
		return render(request, 'blog/post_detail.html', { 'v_html': detalle })