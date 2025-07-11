from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, User
from .serializers import ArticleSerializer

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.TEACHER

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [User.Role.ADMIN, User.Role.SUPERADMIN]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsTeacher()]
        elif self.action in ['approve', 'reject']:
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, status=Article.Status.SUBMITTED)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        article = self.get_object()
        article.status = Article.Status.APPROVED
        article.reviewed_by = request.user
        article.save()
        return Response({'status': 'approved'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        article = self.get_object()
        article.status = Article.Status.REJECTED
        article.reviewed_by = request.user
        article.save()
        return Response({'status': 'rejected'})
