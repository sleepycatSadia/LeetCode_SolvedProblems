
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Solution {
    public boolean isValid(String s) {
    Stack<Character> st =new Stack<Character>();
    char[] c =s.toCharArray();
    for (int i = 0; i < c.length; i++) { 
      if (c[i]=='('||c[i]=='{'||c[i]=='['){
        st.push(c[i]); 
      }else if (c[i]==')'||c[i]=='}'||c[i]==']'){
        if (st.isEmpty()){
            return false;
        }else{
          char start = st.pop();
          char end=c[i];
          if((start=='(' && end==')')||(start=='{'&& end=='}')||(start=='['&& end==']')){
              
          }else{ 
            return false;
          }
        }
      }

    }
    if (st.isEmpty()==true){
        return true;
    }else{
        return false;
    }
    }
}

