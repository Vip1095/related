from django.shortcuts import render

# Create your views here.
# forward compatibility
# Books.objects.all().values('book_name', 'written_by__author_name')

# Backward using related name
# Author.objects.all().values('author_name', 'authors__book_name')



# f I want to access books and their Author Info then the serializer become


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = "__all__"
# class BookSerializer(serializers.ModelSerializer):
#     writen_by = AuthorSerializer(many=False, read_only=True)
#     class Meta:
#         model = Book
#         fields = "__all__"


# But what if we want to access Book info from Author?

# class AuthorSerializer(serializers.ModelSerializer):
#    authors = BookSerializer(many=True, read_only=True)
#     class Meta:
#         model = Author
#         fields = "__all__"