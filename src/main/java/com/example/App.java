package com.example;



import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TodoList todo = new TodoList();

        while (true) {
            System.out.println("\n--- TO-DO CLI APP ---");
            System.out.println("1. Add Task");
            System.out.println("2. Remove Task");
            System.out.println("3. List Tasks");
            System.out.println("0. Exit");
            System.out.print("Choice: ");

            String choice = sc.nextLine().trim();

            switch (choice) {
                case "1":
                    System.out.print("Enter task: ");
                    String addTask = sc.nextLine();
                    todo.addTask(addTask);
                    System.out.println("Task added.");
                    break;

                case "2":
                    System.out.print("Enter task to remove: ");
                    String remTask = sc.nextLine();
                    if (todo.removeTask(remTask))
                        System.out.println("Task removed.");
                    else
                        System.out.println("Task not found.");
                    break;

                case "3":
                    System.out.println("\nYour Tasks:");
                    todo.getTasks().forEach(t ->
                            System.out.println("- " + t.getDescription())
                    );
                    break;

                case "0":
                    System.out.println("Bye!");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice.");
            }
        }
    
    }
}
