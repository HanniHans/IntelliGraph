
package logical;

import java.io.BufferedReader;
import java.io.FileReader;
import graphResources.inicio;
import java.io.FileNotFoundException;
import java.io.IOException;


public class readCSV 
{   
    inicio init = new inicio();
    String lineaTextCSV;
    String nombre = init.getNombre();
    BufferedReader buffered;
    String[] datos;

    public readCSV() throws FileNotFoundException, IOException {
        this.buffered = new BufferedReader(new FileReader(nombre));
        
        while((lineaTextCSV = buffered.readLine()) != null)
        {
            datos = lineaTextCSV.split(",");
            
        }
        
    }
    
    
    
}
