from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):

    #  get_object_or_404，这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用
    post=get_object_or_404(Post,pk=post_pk)
    # 当用户的请求为post时才需要处理表单数据
    if request.method=='POST':
        form=CommentForm(request.POST)
        # 当调用form.is_valid()方法时，Django自动帮我们检查表单的数据是否符合格式要求
        if form.is_valid():
        # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
        # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(post)
        # 数据不合法，重新渲染详情页
        else:
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            comment_list=post.comment_set.all()
            context={'post':post,
                     'form':form,
                     'comment_list':comment_list,
                     }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)
