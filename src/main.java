
public class main {
	
	public static void main(String[] args) {
		
		Transaction t1 = new Transaction("T1000","1/10/2022","AL1");
		Block genesis = new Block(0, t1);
		Transaction t2 = new Transaction("T800","1/11/2020","AL7");
		Block B1 = new Block(genesis.blockHash(), t2);
		Transaction t3 = new Transaction("QT3435","7/01/2022","MD8");
		Block B2 = new Block(B1.blockHash(), t3);
		Transaction t4 = new Transaction("SD324","14/10/2022","FS2");
		Block B3 = new Block(B2.blockHash(), t4);
		genesis.displayBlockHash();
		B1.displayBlockHash();
		B2.displayBlockHash();
		B3.displayBlockHash();
		System.out.println("\n"+"Number of blocks in the chain: "+Block.noOfBlocks());
	}
}
