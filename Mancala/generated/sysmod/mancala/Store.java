/*
 * generated by Fujaba - CodeGen2
 */
package sysmod.mancala;
import de.upb.tools.sdm.*; // requires Fujaba5/libs/RuntimeTools.jar in classpath


public class Store extends AbstractPit
{



   public void accept (PitVisitor visitor )
   {
      boolean fujaba__Success = false;

      // story pattern successor
      try 
      {
         fujaba__Success = false; 

         // collabStat call
         visitor.visit(this);
         // collabStat call
         if ( visitor.getSeeds() > 0 )
         {
         this.getNextPit().accept(visitor);
         }
         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      return ;
   }

}


