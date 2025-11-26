package com.example;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Test;
public class TodoTest {

    @Test
    public void testAddTask() {
        TodoList list = new TodoList();
        assertTrue(list.addTask("Read book"));
    }

    @Test
    public void testRemoveTask() {
        TodoList list = new TodoList();
        list.addTask("Task A");
        assertTrue(list.removeTask("Task A"));
    }

    @Test
    public void testListTasks() {
        TodoList list = new TodoList();
        list.addTask("Task X");
        assertEquals(1, list.getTasks().size());
    }
}
