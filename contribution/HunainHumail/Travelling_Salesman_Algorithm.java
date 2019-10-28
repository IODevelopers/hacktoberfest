/*
 * Hunain Humail
 * hunainhumail786@gmail.com
 */

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.text.*;

public class GreedyTSP {
    
    static ArrayList<Edge> edges = new ArrayList<Edge>();
    static ArrayList<Edge> tourEdges = new ArrayList<Edge>();
    static double greedyDistance = 0.0;
    
    public static void main (String[] args) {
	
	int n = 0;
	long seed = 0;
	DecimalFormat df = new DecimalFormat("0.00");
	
	if (args.length != 2) {
	    System.out.println("Usage: java GreedyTSP n seed");
	    System.exit(0);
	}
	
	try {
	    n = Integer.parseInt(args[0]);
	    seed = Long.parseLong(args[1]);
	}
	
	catch (NumberFormatException e) {
	    System.out.println("Command line args must be integers");
	    System.exit(0);
	}
	
	if ((n < 1) || (n > 1013)) {
	    System.out.println("Number of vertices must be between 1 and 13");
	    System.exit(0);
	}
	

	// create graph, vertices, adjacency matrix, and paths
	Graph g = new Graph(n, seed);

	long startTime = System.currentTimeMillis();
	
	// get graph edges with quicksort
	double[][] adjMatrix = g.getAdjacencyMatrix();
	edges = generateEdges(adjMatrix);
	edges = quicksort(0, edges.size() - 1, edges);

	// Begin Greedy TSP
	ArrayList<Integer> visited = new ArrayList<Integer>();
	visited = greedyTSP(edges, visited, 0);
	visited.add(0);
		
	// Create greedy graph based on results of TSP
	double[][] greedyMatrix = generateGreedyMatrix(visited, adjMatrix);
	
	 // Gather edges that are used for tour and add up distance
	for (int i = 0; i < edges.size(); i++) {
	    for (int j = 0; j < visited.size() - 1; j++) {
		if (((visited.get(j) == edges.get(i).getLeft()) &&
		     (visited.get(j+1) == edges.get(i).getRight()))) {
		    if (edges.get(i).getRight() != edges.get(i).getLeft()) {
			tourEdges.add(edges.get(i));
			greedyDistance += edges.get(i).getDist();
		    }
		}
	    }
	}
	
	long endTime = System.currentTimeMillis();
	    
	// Begin output
	if (n <= 10) {
	    // Print vertices
	    System.out.println(g.getVerticesString(g.getVertices()));
	
	    // Print adjacency matrix
	    System.out.println("Adjacency matrix of graph weights:\n\n" + g.getMatrixString() + "\n");
	
	    // Print greedy graph
	    System.out.println("Greedy graph:\nAdjacency matrix of graph weights:\n");
	    
	    for (int i = 0; i < greedyMatrix.length; i++) {
		System.out.print("      " + i);
	    } 
	    
	    for (int i = 0; i < greedyMatrix.length; i++) {
		System.out.print("\n\n" + i + "   ");
		for (int j = 0; j < greedyMatrix[i].length; j++) {
		    System.out.print(df.format(greedyMatrix[i][j]) + "   ");
		}
	    }
	    System.out.println("\n");
	    
	    // Print out edges
	    for (int i = 0; i < tourEdges.size(); i++) {
		System.out.println(tourEdges.get(i).toString());
	    }
	}
	
	// Print optimal path
	System.out.print("\nDistance using greedy: " + df.format(greedyDistance) + " for path " );
	for (int i = 0; i < visited.size(); i++) {
	    System.out.print(" " + visited.get(i));
	}
	
	System.out.println("\nRuntime for greedy TSP   : " + (endTime - startTime) + " milliseconds");
    }
    
    public static ArrayList<Edge> generateEdges(double[][] matrix) {
	ArrayList<Edge> edges = new ArrayList<Edge>();
	
	for (int i = 0; i < matrix.length; i++) {
	    for (int j = 0; j < matrix[0].length; j++) {
		edges.add(new Edge(i, j, matrix[i][j]));
	    }
	}
	
	return edges;
    }
    
    public static double[][] generateGreedyMatrix(ArrayList<Integer> visited, double[][] oldMatrix) {
	int n = visited.size() - 1;
	double[][] newMatrix = new double[n][n];
	// row, column coordinates
	int r, c = 0;
	
	// add to the greedy matrix if and only if an edge is in the greedy path 
	for (int i = 0; i < visited.size() - 1; i++) {
	    r = visited.get(i);
	    c = visited.get(i+1);
	    newMatrix[r][c] = oldMatrix[r][c];
	    newMatrix[c][r] = oldMatrix[c][r];
	}
	
	return newMatrix;
    }
    
    // Based on http://www.vogella.com/articles/JavaAlgorithmsQuicksort/article.html
    // and pseudocode from Roxanne Canosa
    public static ArrayList<Edge> quicksort(int low, int high, ArrayList<Edge> edges) {
	if (edges.size() <= 1) {
	    return edges;
	}
		
	// get a pivot element
	int pivotIndex = low + (high-low) / 2;
	Edge pivot = edges.get(pivotIndex);
    	
	int i = low, j = high;
	// split into sublists
	while (i <= j) {
	     
	    // sort based on distance
	    // if distance ties, sort based on left vertex
	    // if distance + left ties, sort based on right vertex
	    while ((edges.get(i).getDist() < pivot.getDist()) ||
		   ((edges.get(i).getDist() == pivot.getDist()) &&
		    (edges.get(i).getLeft() < pivot.getLeft())) ||
		   ((edges.get(i).getDist() == pivot.getDist()) &&
		    (edges.get(i).getLeft() == pivot.getLeft()) &&
		    (edges.get(i).getRight() < pivot.getRight()))) {
    		i++;
	    }
	    while ((edges.get(j).getDist() > pivot.getDist()) ||
		   ((edges.get(j).getDist() == pivot.getDist()) &&
		    (edges.get(j).getLeft() > pivot.getLeft())) ||
		   ((edges.get(j).getDist() == pivot.getDist()) &&
		    (edges.get(j).getLeft() == pivot.getLeft()) &&
		    (edges.get(j).getRight() > pivot.getRight()))) {
    		j--;
	    }
       
	     // if a value on the left is larger and a value on the right is smaller, exchange them
	     // afterwards, adjust i and j again
	    if (i <= j) {
		Edge temp = edges.get(i);
		edges.set(i, edges.get(j));
		edges.set(j, temp);
		i++;
		j--;
	    }
	}
	
	// sort sublists too
	if (low < j) {
	    edges = quicksort(low, j, edges);
	}
	if (i < high) {
	    edges = quicksort(i, high, edges);
	}
	
	return edges;
    }
    
    public static ArrayList<Integer> greedyTSP(ArrayList<Edge> edges, ArrayList<Integer> visited, int current) {
    
	visited.add(current);
	
	for (int i = 0; i < edges.size(); i++) {
	    if ((edges.get(i).getLeft() == current) &&
		(visited.contains(edges.get(i).getRight()) == false)) {
		visited = greedyTSP(edges, visited, edges.get(i).getRight());
		break;
	    }
	    else if ((edges.get(i).getRight() == current) &&
		(visited.contains(edges.get(i).getLeft()) == false)) {
		visited = greedyTSP(edges, visited, edges.get(i).getLeft());
		break;
	    }
	}
	
	return visited;
    }
}