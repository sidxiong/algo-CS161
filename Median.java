import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;

public class Median {
	private PriorityQueue<Integer> pqLeft;
	private PriorityQueue<Integer> pqRight;

	public Median() {
		this.pqLeft = new PriorityQueue<>((a, b) -> b.compareTo(a));
		this.pqRight = new PriorityQueue<>();
	}

	private void update(int x) {
		if (pqLeft.size() == 0 && pqRight.size() == 0) {
			pqLeft.offer(x);
		} else if (pqLeft.size() == 0 || x <= pqLeft.peek()) {
			pqLeft.offer(x);
		} else {
			pqRight.offer(x);
		}

		while (pqLeft.size() - pqRight.size() > 1) {
			pqRight.offer(pqLeft.poll());
		}
		while (pqRight.size() - pqLeft.size() > 1) {
			pqLeft.offer(pqRight.poll());
		}
	}

	private int get() {
		if (pqLeft.size() >= pqRight.size()) {
			return pqLeft.peek();
		} else {
			return pqRight.peek();
		}
	}

	public int updateAndGet(int x) {
		update(x);
		return get();
	}



    public static void main(String[] args) {
    	Median m = new Median();
    	List<Integer> medians = new ArrayList<>(10000);

    	try (BufferedReader br = 
    			new BufferedReader(new FileReader(args[0]))) {

    		String line;
    		while ((line = br.readLine()) != null) {
    			int x = Integer.valueOf(line);
    			medians.add(m.updateAndGet(x));
			}
    	} catch (Exception ex) {
    		return;
    	}

    	System.out.println("LOG: medians size: " + medians.size());
    	
    	int result = 0; 
    	for (int median : medians) {
    		result += median;
    		if (result > 10000) {
    			result %= 10000;
    		}
    	}
    	System.out.println(result);
    }
}
