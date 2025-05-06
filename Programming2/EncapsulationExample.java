class Person {
    // Private variables (Data hiding)
    private String name;
    private int age;
    // Public constructor
    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }
    // Getter method for name
    public String getName(){
        return name;
    }
    // Setter method for name
    public void setName(String name){
        this.name = name;
    }
    // Getter method for age
    public int getAge(){
        return age;
    }
    // Setter method for age with validation
    public void setAge(int age){
        if (age >= 0) {
            this.age = age;
        }else{
            System.out.println("Age must be positive!");
        }
    }
    // Display method
    public void displayInfo(){
        System.out.println("Person name: " + name + " " + age + " years old!");
    }
}

// Main Class
public class EncapsulationExample {
    public static void main(String[] args) {
        // Creating an object of Person
        Person p1 = new Person("Rhondel", 20);
        Person p2 = new Person("John", 21);
        // Accessing private data using getter methods
        System.out.println("Name: " + p1.getName());
        System.out.println("Name: " + p2.getName());
        System.out.println("Age: " + p1.getAge());
        System.out.println("Age: " + p2.getAge());
        // Updating private data using setter methods
        p1.setAge(26);
        System.out.println("Update age: " + p1.getAge());
        // Display updated information
        p1.displayInfo();
        p2.displayInfo();
    }
}
