from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ThingSerializer
from .models import Thing
from .permissions import IsOwnerOrReadOnly

class ThingListView(ListCreateAPIView):
    queryset = Thing.objects.all()
    model = Thing
    serializer_class = ThingSerializer

class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    model = Thing
    serializer_class = ThingSerializer
    permission_classes = (IsOwnerOrReadOnly,)
