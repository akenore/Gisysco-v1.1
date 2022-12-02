from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

from frontend.models import Contact, Category, Blog, Page
from frontend.forms import ContactForm, ArticleForm, CategoryForm, PageForm


class HomeView(TemplateView):
    template_name = 'frontend/views/home.html'
    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context['articles'] = Blog.objects.order_by('-published')[:3]
    #     return context


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_message = _(
        "Your submission was successfully received, and our team will answer you as soon as possible")
    success_url = reverse_lazy("contact")
    template_name = 'frontend/views/contact.html'

    def form_valid(self, form, **kwargs):
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        topic = form.cleaned_data['topics']
        message = form.cleaned_data['message']
        subject, from_email, to = topic, 'noreply@gisysco.com', "support@gisysco.com"
        text_content = _('New email from contact help.')
        html_content = _(
            f'Hello Team <br> <p>Mr/Ms: <strong>{full_name}</strong> need help about <strong> {topic} </strong> <br> His/Her message:<br> {message} </p> <p><a href="mailto:{email}">Reply to customer email</a></p>')
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super().form_valid(form)

        # TODO: add notofication to the admin space  when have new contact


class DesignView(TemplateView):
    template_name = 'frontend/views/services/design.html'


class WebView(TemplateView):
    template_name = 'frontend/views/services/web_dev.html'


class MobileView(TemplateView):
    template_name = 'frontend/views/services/mobile_dev.html'


class SeoView(TemplateView):
    template_name = 'frontend/views/services/seo.html'


class MarketingView(TemplateView):
    template_name = 'frontend/views/services/marketing.html'


# Dev Tips View

class AddPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    template_name = 'frontend/views/blog/admin/index.html'
    success_message = _('Your post has been successfully added')
    form_class = ArticleForm
    success_url = reverse_lazy('post-admin-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = ArticleForm
    template_name = 'frontend/views/blog/admin/index.html'
    success_message = _('Your post has been successfully update')
    success_url = reverse_lazy('post-admin-listt')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'frontend/views/blog/admin/delete.html'
    success_url = reverse_lazy('post-admin-list')
    success_message = _('Your post has been successfully deleted')


class ListPostAdminView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Blog
    template_name = 'frontend/views/blog/admin/list.html'
    paginate_by = 5


class BlogView(ListView):
    model = Blog
    paginate_by = 10
    template_name = 'frontend/views/blog/blog.html'

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        kwargs['articles_list'] = Blog.objects.order_by('-published')[:6]

        return super(BlogView, self).get_context_data(**kwargs)


class DetailsBlogView(DetailView):
    model = Blog
    template_name = 'frontend/views/blog/details.html'

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        kwargs['articles_list'] = Blog.objects.order_by('-published')[:6]

        return super(DetailsBlogView, self).get_context_data(**kwargs)


class AddCategoryView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'frontend/views/blog/admin/categories/index.html'
    success_message = _('Your category has been successfully added')
    form_class = CategoryForm
    success_url = reverse_lazy('category-add')

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        return super(AddCategoryView, self).get_context_data(**kwargs)


class UpdateCategoryView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'frontend/views/blog/admin/categories/index.html'
    success_message = _('Your category has been successfully update')
    form_class = CategoryForm
    success_url = reverse_lazy('category-add')

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        return super(UpdateCategoryView, self).get_context_data(**kwargs)


class DeleteCategoryView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'frontend/views/blog/admin/categories/delete.html'
    success_message = _('Your category has been successfully deleted')
    success_url = reverse_lazy('category-add')


class AddPageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Page
    template_name = 'frontend/views/pages/admin/index.html'
    success_message = _('This page has been successfully added')
    form_class = PageForm
    success_url = reverse_lazy('page-list')


class UpdatePageView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Page
    template_name = 'frontend/views/pages/admin/index.html'
    success_message = _('This page has been successfully update')
    form_class = PageForm
    success_url = reverse_lazy('page-list')


class DeletePageView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Page
    template_name = 'frontend/views/pages/admin/delete.html'
    success_url = reverse_lazy('page-list')
    success_message = _('Your page has been successfully deleted')

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeletePageView, self).delete(request, *args, **kwargs)


class ListPageView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Page
    template_name = 'frontend/views/pages/admin/list.html'
    paginate_by = 5


class DetailPageView(SuccessMessageMixin, DetailView):
    model = Page
    template_name = 'frontend/views/pages/details.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
