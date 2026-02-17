

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
When 2 todos are added to list, both should show
as incomplete and nothing should be complete yet
"""
todo_list = TodoList()
todo_1 = Todo("Buy eggs")
todo_2 = Todo("Clean bedroom")
todo_list.add(todo_1)
todo_list.add(todo_2)
todo_list.incomplete()  # => [todo_1, todo_2]
todo_list.complete()    # => []

"""
When we add two todos and mark one complete, it should move from incomplete to complete 
"""
todo_list = TodoList()
todo_1 = Todo("Buy eggs")
todo_2 = Todo("Clean bedroom")
todo_list.add(todo_1)
todo_list.add(todo_2)
todo_1.mark_complete()
todo_list.incomplete()  # => [todo_2]
todo_list.complete()    # => [todo_1]

"""
When we give up all todos become complete
"""
todo_list = TodoList()
todo_1 = Todo("Buy eggs")
todo_2 = Todo("Clean bedroom")
todo_list.add(todo_1)
todo_list.add(todo_2)
todo_list.give_up()
todo_list.complete()    # => [todo_1, todo_2]
todo_list.incomplete()  # => []

"""
If one todo is already complete
and I give up on the list
all todos should end up complete
"""
todo_list = TodoList()
todo_1 = Todo("Buy eggs")
todo_2 = Todo("Clean bedroom")
todo_list.add(todo_1)
todo_list.add(todo_2)

todo_1.mark_complete()

todo_list.give_up()

todo_list.incomplete()  # => []
todo_list.complete()    # => [todo_1, todo_2]

```