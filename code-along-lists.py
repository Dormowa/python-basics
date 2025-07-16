# Create an empty list
todo_list = []
print("Your to-do list:", todo_list)

# Append itemd to the list
todo_list.append("Buy groceries")
todo_list.append("Finish homework")
todo_list.append("Call mom")
print("Updated list:", todo_list)

# Insert an item at a specified location
todo_list.insert(1, "Pay bills")
print("After inserting a task:", todo_list)

# View items using indexing and slicing
print("First task:", todo_list[0])
print("Last two tasks:", todo_list[-2:])

# Mark a task as done (pop it out)
done_task = todo_list.pop(2)
print("You completed:", done_task)
print("To-do list after removal:", todo_list)

# Modify an existing task
todo_list[0] = "Buy groceries and snacks"
print("After modifying a task:", todo_list)

# Print tasks one by one
print("Here’s what you still need to do:")
for task in todo_list:
 print("-", task)
