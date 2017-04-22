from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.http import Http404
from .models import Todo
from rest_framework import viewsets,status
from .serializers import TodoSerializer,UserSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response


class TodoViewSet(viewsets.ModelViewSet):
    """
    查看、编辑Todo的界面
    """
    queryset = Todo.objects.order_by('-pubtime')
    serializer_class = TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户的界面
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class TodoListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(flag=1).order_by('-pubtime').order_by('-priority')
    serializer_class = TodoSerializer



class FinishedListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(flag=0).order_by('-pubtime')
    serializer_class = TodoSerializer


# api_view的方法

# @api_view(['GET', 'POST'])
# def todo_list(request, format=None):
#     """
#     展示或创建todo.
#     """
#     if request.method == 'GET':
#         todo = Todo.objects.filter(flag=1)
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def ftodo_list(request, format=None):
#     """
#     展示或创建todo.
#     """
#     if request.method == 'GET':
#         todo = Todo.objects.filter(flag=0)
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def todo_detail(request, pk, format=None):
#     try:
#         todo = Todo.objects.get(tid=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# 没有用REST的方法


# def todolist(request):
#     todolist = Todo.objects.filter(flag=1)
#     finishtodos = Todo.objects.filter(flag=0)
#     return render(request, 'todo/simpleTodo.html',
#                           {'todolist': todolist,
#                            'finishtodos': finishtodos})


def todolist(request):
    return render(request, 'todo/simpleTodo.html')


# def todoback(request, id=''):
#     todo = Todo.objects.get(tid=id)
#     if todo.flag == '0':
#         todo.flag = '1'
#         todo.save()
#         return HttpResponseRedirect('/todos/')
#     todolist = Todo.objects.filter(flag=1)
#     return render(request, 'todo/simpleTodo.html', {'todolist': todolist})

# def tododelete(request, id=''):
#     try:
#         todo = Todo.objects.get(tid=id)
#     except Exception:
#         raise Http404
#     if todo:
#         todo.delete()
#         return HttpResponseRedirect('/todos/')
#     todolist = Todo.objects.filter(flag=1)
#     return render(reqeust, 'todo/simpleTodo.html', {'todolist': todolist})

# def addTodo(request):
#     if request.method == 'POST':
#         atodo = request.POST['todo']
#         priority = request.POST['priority']
#         user = User.objects.get(id='1')
#         todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
#         todo.save()
#         todolist = Todo.objects.filter(flag='1')
#         finishtodos = Todo.objects.filter(flag=0)
#         return render(request, 'todo/showtodo.html',
#                               {'todolist': todolist, 
#                                'finishtodos': finishtodos})
#     else:
#         todolist = Todo.objects.filter(flag=1)
#         finishtodos = Todo.objects.filter(flag=0)
#         return render(request, 'todo/simpleTodo.html',
#                               {'todolist': todolist, 
#                                'finishtodos': finishtodos})
# def todofinish(request, id=''):
#     todo = Todo.objects.get(tid=id)
#     if todo.flag == '1':
#         todo.flag = '0'
#         todo.save()
#         return HttpResponseRedirect('/todos/')
#     todolist = Todo.objects.filter(flag=1)
#     return render(request, 'todo/simpleTodo.html',
#                            {'todolist': todolist})

def todochange(request, id=''):
    todo = Todo.objects.get(tid=id)
    if todo.flag == '1':
        todo.flag = '0'
        todo.save()
    elif todo.flag == '0':
        todo.flag = '1'
        todo.save()
    return HttpResponse("You're looking at question ")


#PUT权限问题没解决
def update(request, id=''):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(tid=id)
        except Exception:
            return HttpResponseRedirect('/todos/')
        atodo = request.POST['todo']
        priority = request.POST['priority']
        todo.todo = atodo
        todo.priority = priority
        todo.save()
        return HttpResponseRedirect('/todos/')
    else:
        try:
            todo = Todo.objects.get(tid=id)
        except Exception:
            raise Http404
        return render(request, 'todo/updatetodo.html', {'todo': todo})




# def updatetodo(request, id=''):
#     if request.method == 'POST':
#         try:
#             todo = Todo.objects.get(tid=id)
#         except Exception:
#             return HttpResponseRedirect('/todos/')
#         atodo = request.POST['todo']
#         priority = request.POST['priority']
#         todo.todo = atodo
#         todo.priority = priority
#         todo.save()
#         return HttpResponseRedirect('/todos/')
#     else:
#         try:
#             todo = Todo.objects.get(tid=id)
#         except Exception:
#             raise Http404
#         return render(request, 'todo/updatetodo.html', {'todo': todo})

