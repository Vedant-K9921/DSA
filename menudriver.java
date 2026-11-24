import java.util.Scanner; // Needed for user input

public class menudriver {
    public static void main(String[] args) {
        // 1. Variables & Data Types
        String greeting = "Welcome";
        int number = 5;

        // 2. User Input
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = input.nextLine();
        System.out.println(greeting + ", " + name + "!"+number);
    }
}
