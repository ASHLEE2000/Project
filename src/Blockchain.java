
public class Blockchain {
	protected String productID;
	protected String MDate;
	protected String PLine;
	
}

class Transaction extends Blockchain{
	Transaction(String pid, String MD, String Pline){
		productID=pid;
		MDate=MD;
		PLine=Pline;
	}
	
	public String getPID() {
		return productID;
	}
	
	public String MD() {
		return MDate;
	}
	
	public String PLine() {
		return PLine;
	}
}