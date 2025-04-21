import graphene
from graphene_django import DjangoObjectType
from .models import Todo

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ("id", "text", "done", "created_at", "updated_at")

class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)

    def resolve_all_todos(root, info):
        return Todo.objects.all()

class CreateTodo(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(root, info, text):
        todo = Todo(text=text)
        todo.save()
        return CreateTodo(todo=todo)

class ToggleTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    todo = graphene.Field(TodoType)

    def mutate(root, info, id):
        todo = Todo.objects.get(id=id)
        todo.done = not todo.done
        todo.save()
        return ToggleTodo(todo=todo)

class DeleteTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return DeleteTodo(success=True)
        except Todo.DoesNotExist:
            return DeleteTodo(success=False)

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    toggle_todo = ToggleTodo.Field()
    delete_todo = DeleteTodo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation) 