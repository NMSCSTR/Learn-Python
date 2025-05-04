

class Student {
    // Private variables (Data hiding)
    public String name;
    private int age;
    // Public constructor
    public Student(String name, int age){
        this.name = name;
        this.age =age;
    }
    // Getter method for name'
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
        if(this.age > 0){
            this.age = age;
        }else{
            System.out.println("Enter a valid age!");
        }
    }
    // Display method
    public void displayInfo(){
        System.out.println("Student name: " + name + " " + age + " years old!");
    }
}

// Main Class
public class EncapsulationExample {
    public static void main(String[] args) {
        // Creating an object of Student
        Student s1 = new Student("John",19);
        Student s2 = new Student("Lando",23);
        // Accessing private data using getter methods
        
        System.out.println(s1.name);
        System.out.println(s2.name);
        // Updating private data using setter methods
        // Display updated information

        s1.displayInfo();
    }
}
