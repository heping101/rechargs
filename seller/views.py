from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from seller.form import SellerEditForm
from seller.models import Sellers


class SellerInfo(TemplateView):
    template_name = 'seller/info.html'
    model = Sellers

    def get_context_data(self, **kwargs):

        content = super(SellerInfo, self).get_context_data(**kwargs)

        form = SellerEditForm(initial=self.request.user)
        if self.request and self.request.method == "POST":
            seller = self.model.objects.get(pk=self.request.user.id)
            form = SellerEditForm(self.request.POST, instance=seller)
        content['form'] = form
        return content

    def post(self, *args, **kwargs):
        content = self.get_context_data(**kwargs)
        form = content['form']
        if form.is_valid():
            form.save()

        return self.render_to_response(content)



