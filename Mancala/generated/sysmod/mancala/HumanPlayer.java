/*
 * generated by Fujaba - CodeGen2
 */
package sysmod.mancala;
import de.upb.tools.sdm.*; // requires Fujaba5/libs/RuntimeTools.jar in classpath


public class HumanPlayer extends Player
{



   public boolean makeMove (Pit pit )
   {
      boolean fujaba__Success = false;
      MakeMoveVisitor visitor = null;

      // Make sure that player owns pit and create make move visitor
      // story pattern storypatternwiththis
      try 
      {
         fujaba__Success = false; 

         // check object pit is really bound
         JavaSDM.ensure ( pit != null );
         // check link owns from pit to this
         JavaSDM.ensure (this.equals (pit.getPlayer ()));

         // create object visitor
         visitor = new MakeMoveVisitor ( );

         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      if ( !( fujaba__Success ) )
      {
         return false;

      }
      // Visit given pit
      // story pattern successor
      try 
      {
         fujaba__Success = false; 

         // collabStat call
         pit.accept(visitor);
         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      return true;
   }

}


