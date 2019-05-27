from face.forms import OrderForm, ProductsForm
from django.shortcuts import render
# from django.views.decorators.csrf import csrf


def new_order(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        products_form = ProductsForm(request.POST)

        if order_form.is_valid() and products_form.is_valid():

            order = order_form.save()
            products = products_form.save(False)

            products.order = order
            products.save()
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
