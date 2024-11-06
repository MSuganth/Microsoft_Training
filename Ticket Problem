import java.util.Scanner;

class ticket {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the Total Quantity: ");
        int quant = scanner.nextInt();
        int total = 0;
        for (int i = 0; i < quant; i++) {
            System.out.print("Enter the Age: ");
            int age = scanner.nextInt();
            
            int price;
            if (age > 60) {
                price = 1 * 30; 
                total += price;
            } else if (age < 12) {
                price = 1 * 20;
                total += price;  
            } else {
                price = 1 * 50;
                total += price;  
            }
            
            
        }

    
        System.out.println("Total Quantity Cost: " + total);
        scanner.close();
    }
}
