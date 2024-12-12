from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from pr_aa.models import sulfur
from pr_antartic.models import antarcticMass
from pr_dna_rna.models import nucleotideRead, edaphicFactors, C14_C13_data
from pr_plant.models import glacierAlgae, microbialSymbionts
from pr_animal.models import coral, giantPetrelBird
from pr_disease.models import birdInfluenza_bELISA, birdInfluenza_HI, wildlife_cysts_oocysts

@api_view(['GET'])
def getroutes(request):
    routes = [
        'GET /api',
        'GET /api/sulfur',
        'GET /api/antarctic_mass',
        'GET /api/nucleotide_read',
        'GET /api/edaphic_factors',
        'GET /api/c14_c13_data',
        'GET /api/glacier_algae',
        'GET /api/microbial_symbionts',
        'GET /api/coral',
        'GET /api/giant_petrel_bird',
        'GET /api/bird_influenza_belisa',
        'GET /api/bird_influenza_hi',
        'GET /api/wildlife_cysts_oocysts',
    ]
    
    return Response(routes)

@api_view(['GET'])
def get_sulfur(request):
    sulfurs = sulfur.objects.all()
    serializer = SulfurSerializer(sulfurs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_antarctic_mass(request):
    antarctic_masses = antarcticMass.objects.all()
    serializer = AntarcticMassSerializer(antarctic_masses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_nucleotide_read(request):
    nucleotide_reads = nucleotideRead.objects.all()
    serializer = NucleotideReadSerializer(nucleotide_reads, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_edaphic_factors(request):
    edaphic_factors = edaphicFactors.objects.all()
    serializer = EdaphicFactorsSerializer(edaphic_factors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_c14_c13_data(request):
    c14_c13_data = C14_C13_data.objects.all()
    serializer = C14_C13DataSerializer(c14_c13_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_glacier_algae(request):
    glacier_algae = glacierAlgae.objects.all()
    serializer = GlacierAlgaeSerializer(glacier_algae, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_microbial_symbionts(request):
    microbial_symbionts = microbialSymbionts.objects.all()
    serializer = MicrobialSymbiontsSerializer(microbial_symbionts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_coral(request):
    corals = coral.objects.all()
    serializer = CoralSerializer(corals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_giant_petrel_bird(request):
    giant_petrel_birds = giantPetrelBird.objects.all()
    serializer = GiantPetrelBirdSerializer(giant_petrel_birds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_bird_influenza_belisa(request):
    bird_influenza_belisas = birdInfluenza_bELISA.objects.all()
    serializer = BirdInfluenzaBELISASerializer(bird_influenza_belisas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_bird_influenza_hi(request):
    bird_influenza_his = birdInfluenza_HI.objects.all()
    serializer = BirdInfluenzaHISerializer(bird_influenza_his, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_wildlife_cysts_oocysts(request):
    wildlife_cysts_oocysts = wildlife_cysts_oocysts.objects.all()
    serializer = WildlifeCystsOocystsSerializer(wildlife_cysts_oocysts, many=True)
    return Response(serializer.data)
