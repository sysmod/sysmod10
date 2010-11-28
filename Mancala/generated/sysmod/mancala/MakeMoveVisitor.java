/*
 * generated by Fujaba - CodeGen2
 */
package sysmod.mancala;
import de.uni_kassel.features.annotation.util.Property; // requires Fujaba5/libs/features.jar in classpath
import de.uni_kassel.features.ReferenceHandler; // requires Fujaba5/libs/features.jar in classpath
import de.upb.tools.sdm.*; // requires Fujaba5/libs/RuntimeTools.jar in classpath


public class MakeMoveVisitor implements PitVisitor
{



   /**
    * <pre>
    *           0..1     is first     0..1
    * MakeMoveVisitor ------------------------> AbstractPit
    *           makeMoveVisitor2               firstPit
    * </pre>
    */
   public static final String PROPERTY_FIRST_PIT = "firstPit";

   @Property( name = PROPERTY_FIRST_PIT, kind = ReferenceHandler.ReferenceKind.TO_ONE,
         adornment = ReferenceHandler.Adornment.NONE)
   private AbstractPit firstPit;

   @Property( name = PROPERTY_FIRST_PIT )
   public boolean setFirstPit (AbstractPit value)
   {
      boolean changed = false;

      if (this.firstPit != value)
      {
      
         AbstractPit oldValue = this.firstPit;
         this.firstPit = value;
         changed = true;
      
      }
      return changed;
   }

   @Property( name = PROPERTY_FIRST_PIT )
   public MakeMoveVisitor withFirstPit (AbstractPit value)
   {
      setFirstPit (value);
      return this;
   }

   public AbstractPit getFirstPit ()
   {
      return this.firstPit;
   }

   /**
    * <pre>
    *           0..1     is last     0..1
    * MakeMoveVisitor ------------------------> AbstractPit
    *           makeMoveVisitor               lastPit
    * </pre>
    */
   public static final String PROPERTY_LAST_PIT = "lastPit";

   @Property( name = PROPERTY_LAST_PIT, kind = ReferenceHandler.ReferenceKind.TO_ONE,
         adornment = ReferenceHandler.Adornment.NONE)
   private AbstractPit lastPit;

   @Property( name = PROPERTY_LAST_PIT )
   public boolean setLastPit (AbstractPit value)
   {
      boolean changed = false;

      if (this.lastPit != value)
      {
      
         AbstractPit oldValue = this.lastPit;
         this.lastPit = value;
         changed = true;
      
      }
      return changed;
   }

   @Property( name = PROPERTY_LAST_PIT )
   public MakeMoveVisitor withLastPit (AbstractPit value)
   {
      setLastPit (value);
      return this;
   }

   public AbstractPit getLastPit ()
   {
      return this.lastPit;
   }

   public static final String PROPERTY_SEEDS = "seeds";

   @Property( name = PROPERTY_SEEDS, kind = ReferenceHandler.ReferenceKind.ATTRIBUTE )
   private int seeds;

   @Property( name = PROPERTY_SEEDS )
   public void setSeeds (int value)
   {
      this.seeds = value;
   }

   public MakeMoveVisitor withSeeds (int value)
   {
      setSeeds (value);
      return this;
   }

   @Property( name = PROPERTY_SEEDS )
   public int getSeeds ()
   {
      return this.seeds;
   }

   public boolean visit (Pit pit )
   {
      boolean fujaba__Success = false;
      Turn turn = null;
      Player player = null;
      Player oppositePlayer = null;
      Pit oppositePit = null;
      Store store = null;

      if ( firstPit == null )
      {
         // First visited pit, get seeds number and remove seeds from pit
         // story pattern storypatternwiththis
         try 
         {
            fujaba__Success = false; 

            // check object pit is really bound
            JavaSDM.ensure ( pit != null );
            // assign attribute this
            this.setSeeds (pit.getSeeds());
            // assign attribute pit
            pit.setSeeds (0);
            // create link is first from this to pit
            this.setFirstPit (pit);

            fujaba__Success = true;
         }
         catch ( JavaSDMException fujaba__InternalException )
         {
            fujaba__Success = false;
         }


      }
      else
      {
         // Remove seed from visitor and add to pit
         // story pattern storypatternwiththis
         try 
         {
            fujaba__Success = false; 

            // check object pit is really bound
            JavaSDM.ensure ( pit != null );
            // assign attribute this
            this.setSeeds (seeds-1);
            // assign attribute pit
            pit.setSeeds (pit.getSeeds() + 1);
            fujaba__Success = true;
         }
         catch ( JavaSDMException fujaba__InternalException )
         {
            fujaba__Success = false;
         }


      }
      if ( !( seeds==0 ) )
      {
         return false;

      }
      // All seeds given out, this is last pit
      // story pattern storypatternwiththis
      try 
      {
         fujaba__Success = false; 

         // check object pit is really bound
         JavaSDM.ensure ( pit != null );
         // create object turn
         turn = Turn.getInstance();

         // create object player
         player = Turn.getInstance().getPlayer();

         // create link is last from this to pit
         this.setLastPit (pit);

         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      // Give turn to opposite player
      // story pattern successor
      try 
      {
         fujaba__Success = false; 

         // check object player is really bound
         JavaSDM.ensure ( player != null );
         // check object turn is really bound
         JavaSDM.ensure ( turn != null );
         // check link has from turn to player
         JavaSDM.ensure (player.equals (turn.getPlayer ()));

         // search to-one link opposite from player to oppositePlayer
         oppositePlayer = player.getOpposite ();

         // check object oppositePlayer is really bound
         JavaSDM.ensure ( oppositePlayer != null );

         // check isomorphic binding between objects player and oppositePlayer
         JavaSDM.ensure ( !player.equals (oppositePlayer) );


         // destroy link has from turn to player
         turn.setPlayer (null);
         // create link has from turn to oppositePlayer
         turn.setPlayer (oppositePlayer);

         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      // If seeds equals 1 (this was previously empty pit) and player owns this pit then take all seeds from opposite pit and place them in store
      // story pattern successor
      try 
      {
         fujaba__Success = false; 

         // check object pit is really bound
         JavaSDM.ensure ( pit != null );
         // check object player is really bound
         JavaSDM.ensure ( player != null );
         // check link owns from pit to player
         JavaSDM.ensure (player.equals (pit.getPlayer ()));

         // attribute condition seeds == 1
         JavaSDM.ensure ( pit.getSeeds () == 1 );

         // search to-one link opposite of from pit to oppositePit
         oppositePit = pit.getOppositePit ();

         // check object oppositePit is really bound
         JavaSDM.ensure ( oppositePit != null );

         // check isomorphic binding between objects pit and oppositePit
         JavaSDM.ensure ( !pit.equals (oppositePit) );

         // attribute condition seeds > 0
         JavaSDM.ensure ( oppositePit.getSeeds () > 0 );


         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      if ( !( fujaba__Success ) )
      {
         return true;

      }
      // Add seeds to store
      // story pattern successor
      try 
      {
         fujaba__Success = false; 

         // create object store
         store = player.getStore();

         // assign attribute store
         store.setSeeds (store.getSeeds() + pit.getSeeds() +oppositePit.getSeeds());
         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      // Remove seeds from pits
      // story pattern successor
      try 
      {
         fujaba__Success = false; 

         // check object oppositePit is really bound
         JavaSDM.ensure ( oppositePit != null );
         // check object pit is really bound
         JavaSDM.ensure ( pit != null );
         // check isomorphic binding between objects pit and oppositePit
         JavaSDM.ensure ( !pit.equals (oppositePit) );

         // assign attribute pit
         pit.setSeeds (0);
         // assign attribute oppositePit
         oppositePit.setSeeds (0);
         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      return true;
   }

   public boolean visit (Store store )
   {
      boolean fujaba__Success = false;
      Player player = null;

      // story pattern successor
      try 
      {
         fujaba__Success = false; 

         // create object player
         player = Turn.getInstance().getPlayer();

         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      // Skip other player's store
      // story pattern Successor of successor
      try 
      {
         fujaba__Success = false; 

         // check object player is really bound
         JavaSDM.ensure ( player != null );
         // check object store is really bound
         JavaSDM.ensure ( store != null );
         // check link owns from store to player
         JavaSDM.ensure (player.equals (store.getPlayer ()));

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
      // Remove seed from visitor and place into store
      // story pattern storypatternwiththis
      try 
      {
         fujaba__Success = false; 

         // check object store is really bound
         JavaSDM.ensure ( store != null );
         // assign attribute this
         this.setSeeds (seeds-1);
         // assign attribute store
         store.setSeeds (store.getSeeds() + 1);
         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      if ( !( seeds == 0 ) )
      {
         return false;

      }
      // No more seeds, this is last pit
      // story pattern storypatternwiththis
      try 
      {
         fujaba__Success = false; 

         // check object store is really bound
         JavaSDM.ensure ( store != null );
         // create link is last from this to store
         this.setLastPit (store);

         fujaba__Success = true;
      }
      catch ( JavaSDMException fujaba__InternalException )
      {
         fujaba__Success = false;
      }

      return true;
   }

   public void removeYou()
   {
      this.setFirstPit (null);
      this.setLastPit (null);
   }
}


