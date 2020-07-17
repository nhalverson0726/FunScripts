// CSIS 1400 Nick Halverson Homework 2
// prints a table of numbers with their squares and cubes

import javax.swing.JOptionPane; 

public class NumberTable {
	public static void main(String[] args) {
		dialog = "number\tsquare\tcube\n";
	   
      // print values
	   for(int number=0;number<=10; number++) {
	      int square = number*number;
	      int cube = square *number;
         dialog =+ Integer.toString(number) + "\t" + Integer.toString(square) + "\t" + Integer.toString(cube) + "\n";
		
      }
	}
}
