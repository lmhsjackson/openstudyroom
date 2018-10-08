from django.conf.urls import url

from . import views

app_name = 'community'

urlpatterns = [
    url(
        r'^(?P<slug>[\w.@+-]+)/$',
        views.community_page,
        name='community_page'
    ),
    url(
        r'^admin/list/$',
        views.admin_community_list,
        name='admin_community_list'
    ),
    url(
        r'^admin/create/$',
        views.admin_community_create,
        name='admin_community_create'
    ),
    url(
        r'^admin/delete/(?P<pk>[0-9]+)/$',
        views.admin_community_delete,
        name='admin_community_delete'
    ),
    url(
        r'^admin/update/(?P<pk>[0-9]+)/$',
        views.AdminCommunityUpdate.as_view(success_url='/community/admin/list/'),
        name='admin_community_update'
    ),
    url(
        r'^(?P<pk>[0-9]+)/users/$',
        views.admin_user_list,
        name='admin_user_list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/invite/$',
        views.admin_invite_user,
        name='admin_invite_user'
    ),
    url(
        r'^update/(?P<pk>[0-9]+)/$',
        views.CommunityUpdate.as_view(),
        name='community_update'
    ),
    url(
        r'^(?P<community_pk>[0-9]+)/create-league/$',
        views.community_create_league,
        name='create_league'
    ),
    url(
        r'^(?P<community_pk>[0-9]+)/join/(?P<user_pk>[0-9]+)/$',
        views.community_join,
        name='community_join'
    ),
    url(
        r'^(?P<community_pk>[0-9]+)/quit/(?P<user_pk>[0-9]+)/$',
        views.community_quit,
        name='community_quit'
    ),
    url(
        r'^(?P<slug>[\w.@+-]+)/results/$',
        views.community_results_page,
        name='community_resutls'
    ),
    url(
        r'^$',
        views.community_list,
        name='community_list'
    ),
]
