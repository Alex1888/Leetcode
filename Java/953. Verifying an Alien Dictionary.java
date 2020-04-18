class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int mapping[] = new int[26];
        for(int i=0; i<order.length(); i++){
            mapping[order.charAt(i) - 'a'] = i;
        }
        
        for(int i=0; i<words.length-1; i++){
            if(bigger(words[i], words[i+1], mapping))
                return false;
        }
        
        return true;
    }
    
    public boolean bigger(String s1, String s2, int mapping[]){
        int l1 = s1.length(), l2 = s2.length();
        int m = Math.min(l1, l2);
        for(int i=0; i<m; i++){
            if(s1.charAt(i) != s2.charAt(i)){
                return mapping[s1.charAt(i) - 'a'] > mapping[s2.charAt(i) - 'a'];
            }
        }
        
        return l1 > l2;
    }
}
