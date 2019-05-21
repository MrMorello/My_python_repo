from forum.forms import ThreadForm, PostForm
from django.shortcuts import render
# from django.views.decorators.csrf import csrf


def new_thread(request):
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)

        if thread_form.is_valid() and post_form.is_valid():

            thread = thread_form.save()
            post = post_form.save(False)

            post.thread = thread
            post.save()
      #   else:
      #     thread_form = ThreadForm()
      #     post_form = PostForm()
      #
      #
      # args = {}
      # args.update(csrf(request))
      # args['thread_form'] = thread_form
      # args['post_form'] = post_form

    return render(request, 'index.html', locals())
