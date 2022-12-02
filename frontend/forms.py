from django import forms
from frontend.models import Contact, Category, Blog, Page


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'class': 'form-control mb-30'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-30'})
        self.fields['topics'].widget.attrs.update(
            {'class': 'form-control mb-30'})
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control mb-30'})


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']
        widgets = {
            "category": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['feature_image'].widget.attrs.update({'class': 'hidden'})
        self.fields['content'].widget.attrs.update(
            {'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['category'].widget.attrs.update(
            {'class': 'font-medium text-gray-900 dark:text-gray-300', })


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['feature_image'].widget.attrs.update({'class': 'hidden'})


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['content'].widget.attrs.update(
            {'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
