package App_toys;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ToyBox {
    private static List<Toy>toys = new ArrayList<>();
    

    public void addToy (Toy toy){
        toys.add(toy);

    }


    public List<Toy> getToys() {
        return toys;
    }

    public Toy getRandomToy(){
        Random random = new Random();
        double totalFrequency = 0;

        for (Toy toy:toys){
            totalFrequency+=toy.getFrequency();
        }
        double randomFrequency = random.nextDouble()*totalFrequency;
        double frequencySum = 0;
        for (Toy toy: toys){
            frequencySum+=toy.getFrequency();
            if (randomFrequency <= frequencySum){
                return toy;
            }
    
        }
        return null;
    }
    
    
    public Toy getPrizeToy() {
        Toy prizeToy = getRandomToy();
        if (prizeToy != null) {
            toys.remove(prizeToy);
            try {
                FileWriter writer = new FileWriter("prize.txt");
                writer.write(prizeToy.getName());
                writer.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return prizeToy;
    }


}
