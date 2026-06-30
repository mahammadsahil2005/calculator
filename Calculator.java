/**
 * Simple Calculator Application in Java
 * Supports basic arithmetic operations: addition, subtraction, multiplication, division
 */

import java.util.Scanner;

public class Calculator {
    
    /**
     * Performs addition
     */
    public static double add(double num1, double num2) {
        return num1 + num2;
    }
    
    /**
     * Performs subtraction
     */
    public static double subtract(double num1, double num2) {
        return num1 - num2;
    }
    
    /**
     * Performs multiplication
     */
    public static double multiply(double num1, double num2) {
        return num1 * num2;
    }
    
    /**
     * Performs division
     */
    public static double divide(double num1, double num2) {
        if (num2 == 0) {
            throw new IllegalArgumentException("Cannot divide by zero!");
        }
        return num1 / num2;
    }
    
    /**
     * Displays the menu and gets user choice
     */
    public static void displayMenu() {
        System.out.println("\n========== CALCULATOR ==========");
        System.out.println("1. Addition (+)");
        System.out.println("2. Subtraction (-)");
        System.out.println("3. Multiplication (*)");
        System.out.println("4. Division (/)");
        System.out.println("5. Exit");
        System.out.println("================================");
        System.out.print("Enter your choice (1-5): ");
    }
    
    /**
     * Main method - entry point of the application
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean continueCalculating = true;
        
        System.out.println("Welcome to the Java Calculator!");
        
        while (continueCalculating) {
            displayMenu();
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                case 2:
                case 3:
                case 4:
                    System.out.print("Enter first number: ");
                    double num1 = scanner.nextDouble();
                    
                    System.out.print("Enter second number: ");
                    double num2 = scanner.nextDouble();
                    
                    double result = 0;
                    String operation = "";
                    
                    try {
                        switch (choice) {
                            case 1:
                                result = add(num1, num2);
                                operation = "+";
                                break;
                            case 2:
                                result = subtract(num1, num2);
                                operation = "-";
                                break;
                            case 3:
                                result = multiply(num1, num2);
                                operation = "*";
                                break;
                            case 4:
                                result = divide(num1, num2);
                                operation = "/";
                                break;
                        }
                        System.out.println("\nResult: " + num1 + " " + operation + " " + num2 + " = " + result);
                    } catch (IllegalArgumentException e) {
                        System.out.println("\nError: " + e.getMessage());
                    }
                    break;
                    
                case 5:
                    System.out.println("Thank you for using the Calculator. Goodbye!");
                    continueCalculating = false;
                    break;
                    
                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 5.");
            }
        }
        
        scanner.close();
    }
}
