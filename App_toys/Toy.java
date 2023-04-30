package App_toys;



/**
 * Toys
 */
public class Toy {
    private int id;
    private String name;
    private double frequency;


    
    public Toy(int id, String name, double frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    // Геттеры и сеттеры для свойств класса
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    public void setName(String name) {
        this.name = name;
    }
   

    public double getFrequency() {
        return frequency;
    }

    public void setFrequency(double frequency) {
        this.frequency = frequency;
    }

    
   
    
   
}









