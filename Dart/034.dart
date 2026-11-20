// Create a simple to-do application that allows user to add, remove, and view their task.
import 'dart:io';

void main(){

  Map<String, dynamic> task_dictionary = {};

  while(true){
    print("\nEnter 1 to 'Add New Task'\nEnter 2 to 'View Tasks'\nEnter 3 to 'Remove Task'\nEnter 0 to close the application.\n");
    int choice = int.parse(stdin.readLineSync()!);

    if (choice == 0){
      break;
    }

    else{
        switch(choice){
          case 1: print("Enter the task number: ");
            String task_number = stdin.readLineSync()!;
            
            print("Enter the task: ");
            String task = stdin.readLineSync()!;

            task_dictionary[task_number] = task;

          case 2: 
            print("Enter 1 to View All Task\nEnter 2 to Search\n");
            var option = int.parse(stdin.readLineSync()!);
            
            if(option == 1){
              task_dictionary.forEach((key, value) => print("Task $key:\t $value"));
            }

            else if(option == 2){
              print("\n\nSearch with task number");
              String search_value = stdin.readLineSync()!;

              print("\nSearch Result\n");

              if(task_dictionary[search_value] != null){
                print("Task $search_value:\t ${task_dictionary[search_value]}");
              }

              else{
                print("Task not found!");
              }
            }

          case 3:
            print("Enter Task Number to romove the task");
            String task_num = stdin.readLineSync()!;

            if(task_dictionary.containsKey(task_num)){
              task_dictionary.remove(task_num);
              print("\nTask $task_num is removed successfully");
            }
            else{
              print("Task not found!");
            }

          default: print("Invalid Choice!");
        }
    }
  }
}