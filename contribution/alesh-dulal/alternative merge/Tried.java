class MergeAlternate{
	public void merge(String[] a, String[] b){
		int len = a.length + b.length;
		String[] result = {};
		int i=0,j=0,k=0;

		for(i=0; i<len; i++){
			if(i%2 == 0){
				result[i] = a[j++];
			}else{
				result[i] = a[k++];
			}
		}
		// return result;
		System.out.println(result);
	}
	public static void main(String[] args){
		String[] a = {"1","2","3"};
		String[] b = {"a", "b", "c"};
		MergeAlternate m = new MergeAlternate();
		m.merge(a,b);
	}
}