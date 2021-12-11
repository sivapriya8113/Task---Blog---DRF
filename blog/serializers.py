from rest_framework import serializers

from .models import Post, Comment, Like


class PostDetailSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField(read_only=True)
    like = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'comment', 'like']
        read_only_fields = ['author', ]

    def get_comment(self, obj):
        qs = Comment.objects.filter(post__id=obj.id)
        serializer = CommentsSerializer(qs, many=True)
        return serializer.data

    def get_like(self, obj):
        qs = Like.objects.filter(post__id=obj.id)
        print("&&&&&&&&", qs)
        serializer = LikeSerializer(qs, many=True)
        return serializer.data


class PostSerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content']
        read_only_fields = ['author', ]


class CommentsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment_text', 'post']
        read_only_fields = ['user', ]

    def to_representation(self, instance):
        representation = super(CommentsSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        representation['post'] = instance.post.title
        return representation


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['user', ]

