package App_toys;



public class Main {
    public static void main(String[] args) {
        ToyBox toyBox = new ToyBox();
        toyBox.addToy(new Toy(1,"Teddy", 20.0));
        toyBox.addToy(new Toy(2, "Barbie", 30.0));
        toyBox.addToy(new Toy(3, "Car", 50));

        Toy prizeToy = toyBox.getPrizeToy();
        if (prizeToy != null) {
            System.out.println("Выигрышная игрушка: " + prizeToy.getName());
        }




   

        


        
    
    }
    
}
