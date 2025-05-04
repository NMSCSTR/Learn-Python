// Base class with private and protected members
class Person {
    private String name = "Private Name";
    protected String job = "Protected Job";

    private void privateMethod() {
        System.out.println("Inside private method");
    }

    protected void protectedMethod() {
        System.out.println("Inside protected method");
    }

    public void showAccess() {
        // Accessing both private and protected within the same class
        System.out.println("Name: " + name); // OK
        System.out.println("Job: " + job);   // OK
        privateMethod();                    // OK
        protectedMethod();                  // OK
    }
}

// Subclass in same package
class Employee extends Person {
    public void accessParentMembers() {
        // System.out.println("Name: " + name);  // ❌ Error: private member not accessible
        System.out.println("Job: " + job);      // ✅ OK: protected member is accessible

        // privateMethod();   // ❌ Error: private method not accessible
        protectedMethod();   // ✅ OK: protected method is accessible
    }
}

public class AccessModifiersExample {
    public static void main(String[] args) {
        Person p = new Person();
        Employee e = new Employee();

        System.out.println("Accessing from Person:");
        p.showAccess();  // Can access everything inside its own class

        System.out.println("\nAccessing from Employee:");
        e.accessParentMembers();  // Can access protected members, but not private
    }
}
