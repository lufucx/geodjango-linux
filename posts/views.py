from django.shortcuts import render, get_object_or_404
from .models import Post

# View para exibir detalhes de um post específico
def detalhes_post(request, pk):
    # Recupera o post pelo ID (pk) ou retorna 404 se não for encontrado
    post = get_object_or_404(Post, pk=pk)
    # Renderiza o template 'detalhes_post.html' com o contexto do post
    return render(request, 'posts/detalhes_post.html', {'post': post})
