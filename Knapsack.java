import java.util.*;
import java.io.*;

class Knapsack {
	public static int solve(String filename) {
		int w, n;
		int[] values, weights;
		try (Scanner sc = new Scanner(new FileInputStream(filename))) {
			w = sc.nextInt();
			n = sc.nextInt();

			values = new int[n];
			weights = new int[n];
			for (int i = 0; i < n; i++) {
				values[i] = sc.nextInt();
				weights[i] = sc.nextInt();
			}
		} catch (Exception ex) {
			System.out.println("Error");
			return -1;
		}

		return helper(new HashMap<>(), w, n, values, weights);
	}

	private static int helper(Map<Integer, Map<Integer, Integer>> memo, int size, int i,
							  int[] values, int[] weights) {
		if (size == 0 || i == 0) return 0;
		if (memo.containsKey(size) && memo.get(size).containsKey(i)) {
			return memo.get(size).get(i);
		}

		int result;
		if (size < weights[i - 1]) {
			result = helper(memo, size, i-1, values, weights);
		} else {
			result = Math.max(helper(memo, size, i-1, values, weights), 
							helper(memo, size-weights[i-1], i-1, values, weights) + values[i-1]);
		}


		memo.putIfAbsent(size, new HashMap<>());
		memo.get(size).put(i, result);
		return result;
	}

	public static void main(String[] args) {
		int x = Knapsack.solve("knapsack_big.txt");
		System.out.println(x);
	}	
}