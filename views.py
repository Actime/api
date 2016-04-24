# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Wednesday, January 5, 2016
"""

# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
# Rest framework imports
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .Permissions import QuietBasicAuthentication # Custom permissions 
# Import classes 
from states.models import KitState, RegisterState
from customusers.models import Rol, UserSystem
from events.models import Event, Competition, CompetitionType, Category
from competitors.models import TimeReg, Register, Authentication, Competitor
from .imgur import *
# Import Serializers
from states.serializers import KitStateSerializer, RegisterStateSerializer
from customusers.serializers import RolSerializer, UserSystemSerializer, UserSerializer
from events.serializers import EventSerializer, CompetitionSerializer, CompetitionTypeSerializer, CategorySerializer
from competitors.serializers import TimeRegSerializer, RegisterSerializer, AuthenticationSerializer, CompetitorSerializer
# Image decode shit
from PIL import Image
from base64 import *

""" Users module """

"""
Rol List Api View
Object list and creation
"""
class RolList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Rol.objects.all()
    # Serializer class
    serializer_class = RolSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function
# End of Rol List class

"""
Rol Detail Api View
"""
class RolDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Rol.objects.all()
    # Serializer class
    serializer_class = RolSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Rol Detail class
    
"""
User System List Api View
Object list and creation
"""
class UserSystemList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = UserSystem.objects.all()
    # Serializer class
    serializer_class = UserSystemSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of User System List class

"""
User System Detail Api View
"""
class UserSystemDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = UserSystem.objects.all()
    # Serializer class
    serializer_class = UserSystemSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of User System Detail class

###################### End of api views users module

""" Competitors module """

"""
RegisterList Api View
Object list and creation
"""
class RegisterList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Register.objects.all()
    # Serializer class
    serializer_class = RegisterSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Register List class

"""
Register Detail Api View
"""
class RegisterDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Register.objects.all()
    # Serializer class
    serializer_class = RegisterSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Register Detail class

"""
TimeRegList Api View
Object list and creation
"""
class TimeRegList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = TimeReg.objects.all()
    # Serializer class
    serializer_class = TimeRegSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Time Reg List class

"""
Time Reg Detail Api View
"""
class TimeRegDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = TimeReg.objects.all()
    # Serializer class
    serializer_class = TimeRegSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Time Reg Detail class

"""
AuthenticationList Api View
Object list and creation
"""
class AuthenticationList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Authentication.objects.all()
    # Serializer class
    serializer_class = AuthenticationSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Authentication List class

"""
Authentication Detail Api View
"""
class AuthenticationDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Authentication.objects.all()
    # Serializer class
    serializer_class = AuthenticationSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Authentication Detail class

"""
CompetitorList Api View
Object list and creation
"""
class CompetitorList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Competitor.objects.all()
    # Serializer class
    serializer_class = CompetitorSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function
# End of Competitor List class

"""
Competitor Detail Api View
"""
class CompetitorDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Competitor.objects.all()
    # Serializer class
    serializer_class = CompetitorSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Competitor Detail class

###################### End of api views competitors module

""" Events module """

"""
EventList Api View
Object list and creation
"""
class EventList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Event.objects.all()
    # Serializer class
    serializer_class = EventSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Event List class

"""
Event Detail Api View
"""
class EventDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Event.objects.all()
    # Serializer class
    serializer_class = EventSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Event Detail class

"""
CompetitionList Api View
Object list and creation
"""
class CompetitionList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Competition.objects.all()
    # Serializer class
    serializer_class = CompetitionSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Competition List class

"""
Competition Detail Api View
"""
class CompetitionDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Competition.objects.all()
    # Serializer class
    serializer_class = CompetitionSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Competition Detail class

"""
CompetitionList Api View
Object list and creation
"""
class CompetitionListByEvent( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Competition.objects.all()
    # Serializer class
    serializer_class = CompetitionSerializer
    # Get query set definition
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the event id from the request
        event_id = self.request.GET['event_id']
        # filter the objects and then return them
        return Competition.objects.filter(competition_event=event_id)
    # End of get_query
    
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    
# End of Competition List by Event class

"""
CompetitionTypeList Api View
Object list and creation
"""
class CompetitionTypeList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = CompetitionType.objects.all()
    # Serializer class
    serializer_class = CompetitionTypeSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Competition Type List class

"""
Competition Type Detail Api View
"""
class CompetitionTypeDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = CompetitionType.objects.all()
    # Serializer class
    serializer_class = CompetitionTypeSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Competition Type Detail class

"""
CategoryList Api View
Object list and creation
"""
class CategoryList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Category.objects.all()
    # Serializer class
    serializer_class = CategorySerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Category List class

"""
Category Detail Api View
"""
class CategoryDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Category.objects.all()
    # Serializer class
    serializer_class = CategorySerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Category Detail class

"""
CategoryListByCompetition Api View
Object list and creation
"""
class CategoryListByCompetition( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = Category.objects.all()
    # Serializer class
    serializer_class = CategorySerializer
    # Get query set definition
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the event id from the request
        competition_id = self.request.GET['competition_id']
        # get the object and then return it or return a 404 if it doesn't exist 
        competition = get_object_or_404( Competition, pk = competition_id )
        # return the categories
        return competition.categories
    # End of get_query
    
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    
# End of Category List by Competition class

###################### End of api views events module

""" States module """

"""
Kit State List Api View
Object list and creation
"""
class KitStateList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = KitState.objects.all()
    # Serializer class
    serializer_class = KitStateSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Kit State List class

"""
Kit State Detail Api View
"""
class KitStateDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = KitState.objects.all()
    # Serializer class
    serializer_class = KitStateSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Kit State Detail class

"""
Register State List Api View
Object list and creation
"""
class RegisterStateList( generics.ListCreateAPIView ) :
    # Authentication classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set variable
    queryset = RegisterState.objects.all()
    # Serializer class
    serializer_class = RegisterStateSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function
# End of Register State List class

"""
Register State Detail Api View
"""
class RegisterStateDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = RegisterState.objects.all()
    # Serializer class
    serializer_class = RegisterStateSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Register State Detail class

###################### End of api views states module

###################### Other functions for desktop pettitions

"""
Add image to event
"""
class ImageToEventCreate( APIView ) : 
    
    def get_object( self, pk ) :
        """
        Get object function
        """
        try :
            # Get the object by the primary key
            return Event.objects.get( pk=pk )
        except Event.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def put( self, request, pk, format=None ) :
        """
        when posting the event image
        """
        # Get the object by primary key
        event = self.get_object( pk )
        # Event serializer
        event_serializer = EventSerializer(event)
        # Get the images from the pettition
        fh = open("imageToSave.png", "wb")
        # Write on the file
        fh.write(request.data.decode('base64'))
        # Close the file
        fh.close()
        # Save the image on the event
        save_image_event( "imageToSave.png", event.id )
        # return the event serialized
        return Response(event_serializer.data)
    # End of post function
# End of Image To Event Create class

"""
Image to copmetition
this request is for saving the image on the imgur server app
all this of the competition model
"""
class ImageToCompetitionCreate( APIView ) :
    
    def get_object( self, pk ) :
        """
        Get object function
        """
        try :
            # Get the object by the primary key
            return Competition.objects.get( pk=pk )
        except Competition.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def put( self, request, pk, format=None ) :
        """
        When postin the competition image
        """
        # Get the object by primary key
        competition = self.get_object( pk )
        # Competition serializer
        copmetition_serializer = CompetitionSerializer( competition )
        # Get the images from the pettition
        fh = open( "imageToSave.png", "wb" )
        # Write the file
        fh.write( request.data.decode( "base64" ) )
        # Close the file
        fh.close()
        # Save the image on the competition
        save_image_competition( "imageToSave.png", competition.id )
        # return the competition serialized
        return Response( copmetition_serializer )
    # End of put function
# End of ImageToCompetitionCreate view class

"""
Image to galery
this request is for saving the image on the imgur server app
all this of the galery model
"""
class ImageToGaleryCreate( APIView ) :
    
    def get_object( self, pk ) :
        """
        Get object function
        """
        try :
            # Get the object by the primary key
            return Event.objects.get( pk=pk )
        except Event.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def put( self, request, pk, format=None ) :
        """
        When postin the gallery image
        """
        # Get the object by primary key
        event = self.get_object( pk )
        # Competition serializer
        event_serializer = EventSerializer( event )
        # Get the images from the pettition
        fh = open( "imageToSave.png", "wb" )
        # Write the file
        fh.write( request.data.decode( "base64" ) )
        # Close the file
        fh.close()
        # Save the image on the competition
        save_image_to_galery( "imageToSave.png", event.id )
        # return the competition serialized
        return Response( event_serializer )
    # End of put function
# End of ImageToGaleryCreate view class

###### Using images and shit

"""
Register competitor number
this will return the next competitor number of the event
"""
class RegisterCompetitorNumber( APIView ) :
    
    def get_object( self, pk ) :
        """
        Get object funciton
        This will return a competition
        """
        try :
            # Get the object by the primary key
            return Competition.objects.get( pk = pk )
        except Competition.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def get( self, request, pk, format=None ) : 
        """
        Get function just for getting the fucking register number
        """
        # First get the competition by primary key
        competition = self.get_object( pk )
        # Get the event by competition 
        event = Event.objects.get( pk = competition.competition_event.pk )
        # Get all the competitions by event
        competitions = Competition.objects.filter( competition_event = event.pk )
        # Init an empty list of registers
        registers = list()
        # Get all registers by each competition
        for comp in competitions :
            temporal_registers = Register.objects.filter( competition = comp.pk )
            # Verify if the temporal registers are actually not null
            if temporal_registers is not None :
                # Merge the temporal registers to the registers list
                registers = registers + [entry for entry in temporal_registers]
        # End of for
        # validate if the registers list is empty
        if len(registers) :
            # Merge all by order of timestamp
            registers.sort(key=lambda x:x.timestamp, reverse=False)
            # Get the last competitors number
            last_competitor_num = registers[-1].competitor_num
            # data encaps, data bitch!!!!
            data = {
                'data' : (last_competitor_num + 1)   
            }
            # Return the last number plus one, the puls one is on the data encaps
            return Response( data )
        # If there is no register return 1
        else :
            data = {
                'data' : 1,    
            }
            return Response( data )
        # End of else
    # End of get function
# End of RegisterCompetitorNumber api view class

"""
CategoryListByCompetition Api View
Object list and creation
"""
class UserList( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = User.objects.all()
    # Serializer class
    serializer_class = UserSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    
# End of Category List by Competition class

"""
User detail
view for getting the detail, update and destroy user
"""
class UserDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = User.objects.all()
    # Serializer class
    serializer_class = UserSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of UserDetail class

"""
Register competitor number
this will return the next competitor number of the event
"""
class UserSystemByUserId( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query Set
    queryset = UserSystem.objects.all()
    # Serializer class
    serializer_class = UserSystemSerializer
    # Get custom object
    def get_object( self, pk ) :
        """
        Get object funciton
        This will return a competition
        """
        try :
            # Get the object by the primary key
            return UserSystem.objects.get( user = pk )
        except Competition.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object( self.request.GET['user_id'] )
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of RegisterCompetitorNumber api view class

"""
User login
This will return the user if it is validated
"""
class UserLogin( generics.CreateAPIView ) :
    # Authentication classes
    authentication_classes = ( QuietBasicAuthentication, )
    # Query set variable
    queryset = User.objects.all()
    # Serializer variable
    serializer_class = UserSerializer
    
    def get_object( self, user_name ) :
        """
        Function that retrieves the object with the sending user_name
        """
        try :
            # Get the object by the primary key
            return User.objects.get( username = user_name )
        except User.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def create(self, request, *args, **kwargs):
        """
        Create function
        This will just work for our custom post function
        hehe pretty lazy if you ask me :)
        """
        # Serialize the object we have
        user = User()
        user.username = request.data["username"]
        user.password = request.data["password"]
        # Need to get the user from the username we have 
        user_from_db = self.get_object( user.username )
        # Data variable
        data = {
            "data" : None
        }
        # Validate the user_from_the_db
        if user_from_db is not None :
            # Validate password
            if user_from_db.check_password( user.password ) :
                # Return the hole user
                data["data"] = { 
                    "pk" : user_from_db.id,
                    "username" : user_from_db.username,
                    "email" : user_from_db.email,
                    "password" : user.password
                }
                response = Response(data)
                return response 
            else :
                # Return the response data empty
                return Response( data )
        else :
            # Return the response data empty
            return Response( data )
        # End of user validation
    # End of create function
# End of UserLogin class