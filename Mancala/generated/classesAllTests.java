/*
 * generated by Fujaba - CodeGen2
 */
import junit.framework.TestSuite;
import de.upb.tools.sdm.*; // requires Fujaba5/libs/RuntimeTools.jar in classpath
import junit.framework.Test;


public class classesAllTests
{



   public static Test suite ()
   {
      boolean fujaba__Success = false;
      TestSuite suite = null;

      // add all tests to suite
      // story pattern usecasestep
      try 
      {
         fujaba__Success = false; 

         // create object suite
         suite = new TestSuite ( );

         // collabStat call
         suite.setName ("classesAllTests");
         // collabStat call
         suite.addTestSuite (Ulno_makes_a_move_from_house_1Test.class);
         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      return suite;
   }

   public void removeYou()
   {
   }
}


