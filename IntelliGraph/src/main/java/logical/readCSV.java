
package logical;

import java.io.BufferedReader;
import java.io.FileReader;
import graphResources.inicio;
import java.io.FileNotFoundException;
import java.io.IOException;


public class readCSV 
{   
    
    String lineaTextCSV;
    BufferedReader buffered;
    String[] datos;

    public readCSV(String nombre) throws FileNotFoundException, IOException {
        this.buffered = new BufferedReader(new FileReader(nombre));
        
        while((lineaTextCSV = buffered.readLine()) != null)
        {
            datos = lineaTextCSV.split(",");
            
        }
        System.out.println(datos.length);
        for(int i = 0; i< datos.length; i++)
        {
            System.out.println(datos[i]);
        }
    }
    
    
    
    
    
}
