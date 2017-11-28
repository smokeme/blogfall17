from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from posts.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer
from .permissions import IsAuthor

class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	permission_classes=[AllowAny,]

class PostCreateView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	permission_classes=[IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class PostDetailView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'
	permission_classes=[AllowAny,]

class PostDeleteView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'
	permission_classes=[IsAuthenticated, IsAdminUser,]

class PostUpdateView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'
	permission_classes=[IsAuthenticated, IsAuthor,]