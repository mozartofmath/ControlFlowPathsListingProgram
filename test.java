public class MyClass{

    public static void main(){
        int a = 10;
        int b;
        if(a%2 == 0){
            System.out.println(a + " is odd");
            if (a%4 == 0){
                System.out.println("4 is a factor of "+a);
            }
            else{
                System.out.println("4 is not a factor of "+a);
            }
        }
        else{
            System.out.println(a + " is even");
            if (a%3 == 0){
                System.out.println("3 is a factor of "+a);
            }
            else{
                System.out.println("3 is not a factor of "+a);
                int b = a;
                while(1){
                    b+=1;
                    if(b == 20){
                        break;
                    }
                }
            }

        }
    }

}