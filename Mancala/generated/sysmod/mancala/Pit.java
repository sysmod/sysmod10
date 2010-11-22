/*
 * generated by Fujaba - CodeGen2
 */
package sysmod.mancala;
import de.upb.tools.sdm.*; // requires Fujaba5/libs/RuntimeTools.jar in classpath
import de.uni_kassel.features.annotation.util.Property; // requires Fujaba5/libs/features.jar in classpath
import de.uni_kassel.features.ReferenceHandler; // requires Fujaba5/libs/features.jar in classpath


public class Pit extends AbstractPit
{



   public boolean move ()
   {
      boolean fujaba__Success = false;
      AbstractPit element = null;

      // story pattern storypatternwiththis
      try 
      {
         fujaba__Success = false; 

         // create object element
         element = this;

         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      // story pattern storypatternwithparams
      try 
      {
         fujaba__Success = false; 

         // collabStat call
         for ( int i = 1;i <= this.getSeeds();++i )
         {
         element = element.getNextPit(); element.addSeed();
         }
         // collabStat call
         this.setSeeds(0);
         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      return true;
   }

   /**
    * <pre>
    *           0..1     opposite of     0..1
    * Pit ------------------------- Pit
    *           oppositePit               oppositePit
    * </pre>
    */
   public static final String PROPERTY_OPPOSITE_PIT = "oppositePit";

   @Property( name = PROPERTY_OPPOSITE_PIT, partner = Pit.PROPERTY_OPPOSITE_PIT, kind = ReferenceHandler.ReferenceKind.TO_ONE,
         adornment = ReferenceHandler.Adornment.NONE)
   private Pit oppositePit;

   @Property( name = PROPERTY_OPPOSITE_PIT )
   public boolean setOppositePit (Pit value)
   {
      boolean changed = false;

      if (this.oppositePit != value)
      {
      
         Pit oldValue = this.oppositePit;
         Pit source = this;
         if (this.oppositePit != null)
         {
            this.oppositePit = null;
            oldValue.setOppositePit (null);
         }
         this.oppositePit = value;

         if (value != null)
         {
            value.setOppositePit (this);
         }
         changed = true;
      
      }
      return changed;
   }

   @Property( name = PROPERTY_OPPOSITE_PIT )
   public Pit withOppositePit (Pit value)
   {
      setOppositePit (value);
      return this;
   }

   public Pit getOppositePit ()
   {
      return this.oppositePit;
   }

   public void removeYou()
   {
      this.setOppositePit (null);
      super.removeYou ();
   }
}


