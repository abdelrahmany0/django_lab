from rest_framework.response import Response
from rest_framework import status
from book.models import Book
from .serializers import BookSerializer, UserSerializer
from rest_framework.decorators import api_view


@api_view(["GET"])
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def show(request, id):
    if Book.objects.filter(pk=id).exists():
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            data={"message": "Book not found"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            data={"success": True, "message": "Book created successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        data={"success": False, "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["DELETE"])
def delete(request, id):
    if Book.objects.filter(pk=id).exists():
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(
            data={"message": "Book deleted successfully"},
            status=status.HTTP_200_OK
        )

    else:
        return Response(data={"success": False, "errors": "couldn't delete book!!!"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)