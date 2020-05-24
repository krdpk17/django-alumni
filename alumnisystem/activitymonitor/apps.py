from django.apps import AppConfig


class ActivitymonitorConfig(AppConfig):
    name = 'activitymonitor'

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User
        registry.register(User)
        from accounts.models import UserProfile
        registry.register(UserProfile)
        from boards.models import Board, Topic, Post
        registry.register(Board)
        registry.register(Topic)
        registry.register(Post)