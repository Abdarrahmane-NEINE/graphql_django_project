# Todo List GraphQL API

A headless GraphQL API for a Todo-List service built with Django and Graphene.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

The GraphQL endpoint will be available at `http://localhost:8000/graphql/`

## Example GraphQL Operations

### Query all todos
```graphql
query {
  allTodos {
    id
    text
    done
    createdAt
    updatedAt
  }
}
```

### Create a todo
```graphql
mutation {
  createTodo(text: "Buy groceries") {
    todo {
      id
      text
      done
    }
  }
}
```

### Toggle todo status
```graphql
mutation {
  toggleTodo(id: "1") {
    todo {
      id
      text
      done
    }
  }
}
```

### Delete a todo
```graphql
mutation {
  deleteTodo(id: "1") {
    success
  }
}
```
