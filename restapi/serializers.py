# Climatology
# - Arctic & antartica 2 ->Sulphur Detection from Melting Ice Cores
# - Antarctica 1 -> antarctica mass

# Molecular biology
# - fungi -> 14c and 13c data, nucleotide reads, edaphic factors

# Biodiversity
# - Animal 1 -coral
# - Animal 2 -giant petrel bird
# - Plant 1 -glacier algae
# - Plant 2- microbial symbionts

# Disease
# - Disease 1-Influenza -> BELISA, HI
# - Disease 2 ->Cryptosporidium oocyst and giardia cysts

from rest_framework import serializers
from pr_aa.models import sulfur
from pr_antartic.models import antarcticMass
from pr_dna_rna.models import nucleotideRead, edaphicFactors, C14_C13_data
from pr_plant.models import glacierAlgae, microbialSymbionts
from pr_animal.models import coral, giantPetrelBird
from pr_disease.models import birdInfluenza_bELISA, birdInfluenza_HI, wildlife_cysts_oocysts

class SulfurSerializer(serializers.ModelSerializer):
    class Meta:
        model = sulfur
        fields = '__all__'

class AntarcticMassSerializer(serializers.ModelSerializer):
    class Meta:
        model = antarcticMass
        fields = '__all__'

class NucleotideReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = nucleotideRead
        fields = '__all__'

class EdaphicFactorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = edaphicFactors
        fields = '__all__'

class C14_C13DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = C14_C13_data
        fields = '__all__'

class GlacierAlgaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = glacierAlgae
        fields = '__all__'

class MicrobialSymbiontsSerializer(serializers.ModelSerializer):
    class Meta:
        model = microbialSymbionts
        fields = '__all__'

class CoralSerializer(serializers.ModelSerializer):
    class Meta:
        model = coral
        fields = '__all__'

class GiantPetrelBirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = giantPetrelBird
        fields = '__all__'

class BirdInfluenzaBELISASerializer(serializers.ModelSerializer):
    class Meta:
        model = birdInfluenza_bELISA
        fields = '__all__'

class BirdInfluenzaHISerializer(serializers.ModelSerializer):
    class Meta:
        model = birdInfluenza_HI
        fields = '__all__'

class WildlifeCystsOocystsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wildlife_cysts_oocysts
        fields = '__all__'
