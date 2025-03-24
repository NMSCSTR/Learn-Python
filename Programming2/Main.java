class Student {
    private String name;
    private int age;

    // Constructor
    public Student(String name, int age) {
        this.name = name;
        setAge(age);  
    }

    // Getter method for name
    public String getName() {
        return name;
    }

    // Setter method for name
    public void setName(String name) {
        this.name = name;
    }

    // Getter method for age
    public int getAge() {
        return age;
    }

    // Setter method for age with validation
    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        } else {
            System.out.println("Invalid age! Setting to default (18).");
            this.age = 18;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student("Alice", 20);
        System.out.println("Student Name: " + student.getName());
        System.out.println("Student Age: " + student.getAge());

        student.setAge(-5); // Invalid age
        System.out.println("Updated Age: " + student.getAge());
    }
}
