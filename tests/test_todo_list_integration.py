from lib.todo_list import TodoList
from lib.todo import Todo

def test_empty_todo_list_returns_empty_lists():
    todo_list = TodoList()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == []

def test_after_adding_two_todos_incomplete_returns_both():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Clean room")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    assert todo_list.incomplete() == [todo_1, todo_2]

def test_after_adding_two_todos_complete_returns_empty_list():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Clean room")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    assert todo_list.complete() == []

def test_after_adding_two_todos_and_marking_one_complete_splits_lists():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Clean room")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    todo_1.mark_complete()

    assert todo_list.incomplete() == [todo_2]
    assert todo_list.complete() == [todo_1]

def test_give_up_marks_everything_complete():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Clean room")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    todo_list.give_up()

    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo_1, todo_2]

def test_give_up_when_some_already_complete():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Clean room")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    todo_1.mark_complete()

    todo_list.give_up()

    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo_1, todo_2]