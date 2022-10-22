import java.util.Arrays;

public class Block {

	/*  
	 String[] l1 = {"ab0","b","c"};
	void displayHash(){
	System.out.println(Arrays.hashCode(l1));
	}
	*/
	
	private int previousHash;  //given
	private String a;
	private String b;
	private String c;
	//Transaction t;	//passed on
	
	private int thisBlockHash;	//to be calculated
	private static int noOfBlocks;
	
	//Creation of blocks
	public Block(int pH, Transaction t) {
		previousHash=pH;
		a= t.getPID();
		b= t.MD();
		c=t.PLine();
		int[] tCTBH = {t.hashCode(), previousHash};
		thisBlockHash= tCTBH.hashCode();
		noOfBlocks++;
	}
	
	public int blockHash() {
		return thisBlockHash;
	}
	
	public void displayBlockHash() {
		System.out.println("Transaction data in this block:"+a+"\n"+b+"\n"+c);
		System.out.println("Hash of previous block:  "+previousHash);
		System.out.println("Hash of current block:  "+thisBlockHash+"\n");
	}
	
	public static int noOfBlocks() {
		return noOfBlocks;
	}
}

