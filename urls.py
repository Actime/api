# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Tuesday, January 5, 2016
"""

# Imports
from django.conf.urls import patterns, url
from .views import *

# Url patterns
urlpatterns = patterns(
    
    'api.views',
    # States module
    url(r'^kitstate/$', KitStateList.as_view() , name='kitstate.list'), # Kit State List
    url(r'^kitstate/(?P<pk>[0-9]+)$', KitStateDetail.as_view(), name='kitstate.detail'), # Kit State Detail
    
    url(r'^registerstate/$', RegisterStateList.as_view() , name='registerstate.list'), # Register State list
    url(r'^registerstate/(?P<pk>[0-9]+)$', RegisterStateDetail.as_view(), name='registerstate.detail'), # Register State list
    
    # Users module UserSystemByUserId
    url(r'^rol/$', RolList.as_view() , name='rol.list'), # Rol list
    url(r'^rol/(?P<pk>[0-9]+)$', RolDetail.as_view(), name='rol.detail'), # Rol Detail
    
    url(r'^usersystem/$', UserSystemList.as_view() , name='usersystem.list'), # Users system list
    url(r'^usersystem/(?P<pk>[0-9]+)$', UserSystemDetail.as_view(), name='usersystem.detail'), # User system Detail
    url(r'^usersystem/getbyuser/$', UserSystemByUserId.as_view(), name='usersystem.getbyuser'), # User system by User id
    
    url(r'^user/$', UserList.as_view(), name='user.list'), # User List
    url(r'^user/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user.detail'), # User Detail
    url(r'^user/login/$', UserLogin.as_view(), name='user.login'), # User Login
    
    # Events module  ImageToGaleryCreate
    url(r'^event/$', EventList.as_view() , name='event.list'), # Event list
    url(r'^event/(?P<pk>[0-9]+)$', EventDetail.as_view(), name='event.detail'), # Event Detail
    url(r'^event/image/(?P<pk>[0-9]+)$', ImageToEventCreate.as_view(), name='event.image'), # Event Detail
    url(r'^event/galery/(?P<pk>[0-9]+)$', ImageToGaleryCreate.as_view(), name='event.galery'), # Event Galery
    
    url(r'^competition/$', CompetitionList.as_view() , name='competition.list'), # Competition List
    url(r'^competition/(?P<pk>[0-9]+)$', CompetitionDetail.as_view(), name='competition.detail'), # Competition Detail
    url(r'^competition/byevent/$', CompetitionListByEvent.as_view(), name='competition.byevent'), # Competition by event list
    url(r'^competition/categories/$', CategoryListByCompetition.as_view(), name='competition.categories'), # Categories by competition_id
    url(r'^competition/image/(?P<pk>[0-9]+)$', ImageToCompetitionCreate.as_view(), name='competition.image'), # Competition Detail

    url(r'^competitiontype/$', CompetitionTypeList.as_view() , name='competitiontype.list'), # Competition type List
    url(r'^competitiontype/(?P<pk>[0-9]+)$', CompetitionTypeDetail.as_view(), name='competitiontype.detail'), # Competition type Detail
    
    url(r'^category/$', CategoryList.as_view() , name='category.list'), # Category type List
    url(r'^category/(?P<pk>[0-9]+)$', CategoryDetail.as_view(), name='category.detail'), # Category type Detail
    
    # Competitros module 
    url(r'^register/$', RegisterList.as_view() , name='register.list'), # Register type List
    url(r'^register/(?P<pk>[0-9]+)$', RegisterDetail.as_view(), name='register.detail'), # Register type Detail
    url(r'^register/competitornum/(?P<pk>[0-9]+)$', RegisterCompetitorNumber.as_view(), name='register.competitor_num'), # Get the Register competitor number
    
    url(r'^timereg/$', TimeRegList.as_view() , name='timereg.list'), # Time Reg type List
    url(r'^timereg/(?P<pk>[0-9]+)$', TimeRegDetail.as_view(), name='timereg.detail'), # Time Reg type Detail
    
    url(r'^authentication/$', AuthenticationList.as_view() , name='authentication.list'), # Authentication type List
    url(r'^authentication/(?P<pk>[0-9]+)$', AuthenticationDetail.as_view(), name='authentication.detail'), # Authentication type Detail
    
    url(r'^competitor/$', CompetitorList.as_view() , name='competitor.list'), # Competitor type List
    url(r'^competitor/(?P<pk>[0-9]+)$', CompetitorDetail.as_view(), name='competitor.detail'), # Competitor type Detail
    
) # End of url patterns