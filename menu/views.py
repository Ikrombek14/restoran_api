from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from .serializers import MenuCategorySerializer, MenuProductsSerializer, MenuOrderSerializer
from .models import MenuCategory, MenuProducts, MenuOrder
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.


class MenuCategoryView(ListAPIView):
    queryset = MenuCategory.objects.all()
    permission_classes = [AllowAny]
    serializer_class = MenuCategorySerializer
    read_only = True


class MenuProductView(APIView):
    def get(self, request, pk):
        try:
            category = MenuCategory.objects.get(id=pk)
            products = MenuProducts.objects.filter(category=category)
            serializer = MenuProductsSerializer(products, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)



class MenuOrderView(ListAPIView):
    queryset = MenuOrder.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MenuOrderSerializer
    read_only = True
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def menu_order(request, pk):
    try:
        product = MenuProducts.objects.get(id=pk)
        serializer = MenuOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product, user=request.user)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def update_order(request, pk):
    try:
        order = MenuOrder.objects.get(id=pk)
        serializer = MenuOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_order(request, pk):
    try:
        order = MenuOrder.objects.get(id=pk)
        order.delete()
        return Response({"message": "Order deleted"}, status=HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)