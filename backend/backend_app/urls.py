from django.urls import path,include
from backend_app import views
from rest_framework.routers import DefaultRouter

member_router =DefaultRouter()
member_router.register('list.do',views.MemberViewSet)

board_router = DefaultRouter()
board_router.register('list.do',views.BoardViewSet)

comment_router = DefaultRouter()
comment_router.register('list.do',views.CommentViewSet)

swing_router = DefaultRouter()
swing_router.register('<member_id>',views.SwingResultViewSet)

urlpatterns = [

    path('member/', include(member_router.urls), name="Member"),
    path('board/', include(board_router.urls), name="Board"),
    path('comment/', include(comment_router.urls) , name="comment"),
    path('swingresult/', include(swing_router.urls), name="Member_swing_result"),

]
