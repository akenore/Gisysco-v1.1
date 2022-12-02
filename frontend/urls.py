from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/design/', views.DesignView.as_view(), name='design'),
    path('services/web-development/', views.WebView.as_view(), name='web'),
    path('services/mobile-development/', views.MobileView.as_view(), name='mobile'),
    path('services/seo/', views.SeoView.as_view(), name='seo'),
    path('services/marketing/', views.MarketingView.as_view(), name='marketing'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    # Extra Pages
    path('myspace/pages/add/', views.AddPageView.as_view(), name='page-add'),
    path('myspace/pages/update/<slug>/', views.UpdatePageView.as_view(), name='page-update'),
    path('myspace/pages/delete/<slug>/', views.DeletePageView.as_view(), name='page-delete'),
    path('myspace/pages/list/', views.ListPageView.as_view(), name='page-list'),
    path('<slug>/', views.DetailPageView.as_view(), name='page-detail'),

    # Dev Tips(Blog and categories)
    path('dev-tips/', views.BlogView.as_view(), name='articles'),
    path('dev-tips/<slug>/', views.DetailsBlogView.as_view(), name='post-detail'),
    path('myspace/blog/add/', views.AddPostView.as_view(), name='post-add'),
    path('myspace/blog/update/<slug>/', views.UpdatePostView.as_view(), name='post-update'),
    path('myspace/blog/delete/<slug>/', views.DeletePostView.as_view(), name='post-delete'),
    path('myspace/blog/list/', views.ListPostAdminView.as_view(), name='post-admin-list'),

    path('myspace/blog/category/add/', views.AddCategoryView.as_view(), name='category-add'),
    path('myspace/blog/category/update/<slug>/', views.UpdateCategoryView.as_view(), name='category-update'),
    path('myspace/blog/category/delete/<slug>/', views.DeleteCategoryView.as_view(), name='category-delete'),
]
