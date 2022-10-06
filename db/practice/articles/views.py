from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
# require_GET
def index(request):
    articles = Article.objects.all()
    # objects : ORM 장고 매니저, python과 DB 호환
    # Article 테이블의 모든 데이터 불러오기
    context = {
        'articles': articles,
    }
    # context : python과 html 호환
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
    # 게시글 작성 후
        form = Articleform(request.POST)
        # 데이터로 채워진 형식
        if form.is_valid():
            article = form.save(commit=False)
            # DB에 커밋은 안한 상태지만 객체로 불러올 수 이음
            article.user = request.user
            # FK 할당 (사용자가 하는게 아니라 view함수에서 해결)
            article.save()
            return redirect('articls:detail', article.pk)
            # 생성한 게시글 보여주기 위해 detail(url name)으로 보내주기
    else:
    # 게시글 작성 전
        form = ArticleForm()
        # 비어있는 형식
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 불러올 게시글은 Article 테이블의 pk번 글
    comment_form = CommentForm()
    comments = article.comment_set.all()
    # comment_set : django매니저, 역참조(article의 pk 1 = comment의 fk N)
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = AricleForm(request.POST, instance=article)
            # instance : 변경될 게시글이 뭔지 알려줘야함
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else: # 수정 값 입력 전
            form = ArticleForm(instance=article)
            # instance : 화면에 수정하기 전 값 보여주기 위해
    else: # 게시글 작성자오 요청한 유저가 다르면
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'artciles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detial', article.pk)