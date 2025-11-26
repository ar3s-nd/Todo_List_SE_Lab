package com.example;



import java.util.ArrayList;
import java.util.List;

public class TodoList {
    private final List<Task> tasks = new ArrayList<>();

    public boolean addTask(String desc) {
        tasks.add(new Task(desc));
        return true;
    }

    public boolean removeTask(String desc) {
        return tasks.removeIf(t -> t.getDescription().equals(desc));
    }

    public List<Task> getTasks() {
        return tasks;
    }
}
