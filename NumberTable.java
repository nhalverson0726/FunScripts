// CSIS 1400 Nick Halverson Homework 2
// prints a table of numbers with their squares and cubes

class NumberTable {
	public static void main(String[] args) {
		// print headers
		System.out.printf("%s\t%s\t%s\n", "number", "square", "cube");
	   
      // print values
	   for(int number=0;number<=10; number++) {
	      int square = number*number;
	      int cube = square *number;
         System.out.printf("%d\t%d\t%d\n", number, square, cube);
      }
	}
}



	
