class Student {
    // Private variables (Data hiding)
    private String name;
    private int age;

    // Public constructor
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
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
        if (age > 0) {  // Ensuring a valid age
            this.age = age;
        } else {
            System.out.println("Age must be positive.");
        }
    }

    // Display method
    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

// Main Class
public class EncapsulationExample {
    public static void main(String[] args) {
        // Creating an object of Student
        Student s1 = new Student("Alice", 20);
        

        // Accessing private data using getter methods
        System.out.println("Student Name: " + s1.getName());
        System.out.println("Student Age: " + s1.getAge());

        // Updating private data using setter methods
        s1.setName("Bob");
        s1.setAge(25);

        // Display updated information
        s1.displayInfo();
    }
}
