/*
 * generated by Fujaba - CodeGen2
 */
package sysmod.mancala;
import de.uni_kassel.features.annotation.util.Property; // requires Fujaba5/libs/features.jar in classpath
import de.uni_kassel.features.ReferenceHandler; // requires Fujaba5/libs/features.jar in classpath


public class Turn
{



   private  Turn ()
   {
   }

   public static Turn getInstance ()
   {

      return turnInstance;
   }

   /**
    * <pre>
    *           0..1     has     0..1
    * Turn ------------------------- Player
    *           turn               player
    * </pre>
    */
   public static final String PROPERTY_PLAYER = "player";

   @Property( name = PROPERTY_PLAYER, partner = Player.PROPERTY_TURN, kind = ReferenceHandler.ReferenceKind.TO_ONE,
         adornment = ReferenceHandler.Adornment.NONE)
   private Player player;

   @Property( name = PROPERTY_PLAYER )
   public boolean setPlayer (Player value)
   {
      boolean changed = false;

      if (this.player != value)
      {
      
         Player oldValue = this.player;
         Turn source = this;
         if (this.player != null)
         {
            this.player = null;
            oldValue.setTurn (null);
         }
         this.player = value;

         if (value != null)
         {
            value.setTurn (this);
         }
         changed = true;
      
      }
      return changed;
   }

   @Property( name = PROPERTY_PLAYER )
   public Turn withPlayer (Player value)
   {
      setPlayer (value);
      return this;
   }

   public Player getPlayer ()
   {
      return this.player;
   }

   public static final String PROPERTY_TURN_INSTANCE = "turnInstance";

   @Property( name = PROPERTY_TURN_INSTANCE, kind = ReferenceHandler.ReferenceKind.ATTRIBUTE )
   private static Turn turnInstance = new Turn();


   public void removeYou()
   {
      this.setPlayer (null);
   }
}


