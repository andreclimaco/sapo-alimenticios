from rest_framework import viewsets, mixins, permissions
from .models import Food
from .serializers import FoodSerializer
from rest_framework import filters
from django.db.models import F


class FoodsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API Foods: Method GET
    """

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    def get_queryset(self):

        macronutrients = self.request.query_params.get('macronutrients')
        if macronutrients is not None:
            if hasattr(Food, macronutrients):
                if macronutrients == 'proteins':
                    return self.queryset.filter(
                        active=True, proteins__gte=F('carbohydrates')) \
                        .filter(proteins__gte=F('fats'))
                if macronutrients == 'carbohydrates':
                    return self.queryset.filter(
                        active=True, carbohydrates__gte=F('proteins')) \
                        .filter(carbohydrates__gte=F('fats'))
                if macronutrients == 'fats':
                    return self.queryset.filter(
                        active=True, fats__gte=F('proteins')) \
                        .filter(carbohydrates__gte=F('carbohydrates'))
        else:
            return self.queryset.all()


class FoodViewSet(viewsets.ModelViewSet):
    """
    API Food: Method GET, POST, PUT, DELETE
    """
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
