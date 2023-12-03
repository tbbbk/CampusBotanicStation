from django.http import HttpResponse
from .models import *
import markdown
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticlePostForm, CommentForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login as django_login, logout as django_logout



@login_required
def article_list(request):
    search = request.GET.get('search')

    if search:
        articles = ArticlePost.objects.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        # 将 search 参数重置为空
        search = ''
        articles = ArticlePost.objects.all()
    for article in articles:
        article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 目录扩展
        'markdown.extensions.toc',
        ])
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles, 'search': search }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)


@login_required
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    comments = Comment.objects.filter(article=id)
    article.body = md.convert(article.body)
    article.total_views += 1
    article.save(update_fields=['total_views'])
    # 需要传递给模板的对象
    context = { 'article': article, 'toc': md.toc, 'comments': comments }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)


@login_required
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'article/create.html', context)


@login_required
def article_delete(request, id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")


@login_required
def article_update(request, id):
    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article:article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)



# 文章评论
@login_required
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")



def loginORregister(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    type_ = request.POST.get("loginORregister")
    print(username, password)
    if type_ == "login":
        user = authenticate(username=username, password=password)
        if not user:
            print("查无此人")
            return render(request, 'login.html', {'error': '用户名或密码错误'})
        else:
            django_login(request, user)
            return redirect(reverse("index"))
    elif type_ == "register":
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': '用户名已被使用'})
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect(reverse("index")) 


def logout(request):
    django_logout(request)
    return redirect(reverse("index")) 

