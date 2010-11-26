package sysmod.mancala;

import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.util.ArrayList;
import java.util.List;

import javax.swing.SwingUtilities;

public class GameController {
	private List<AbstractPit> pits = new ArrayList<AbstractPit>();
	private Player playerOne;
	private Player playerTwo;
	
	private PropertyChangeListener seedsChangeListener = new PropertyChangeListener() {

		@Override
		public void propertyChange(PropertyChangeEvent evt) {
			
			
		}
		
	};
	
	private PropertyChangeListener turnChangeListener = new PropertyChangeListener() {

		@Override
		public void propertyChange(PropertyChangeEvent evt) {
			
			
		}
		
	};
	
	private void initializePits(){
		AbstractPit pit = new Pit();
		pit.setPlayer(playerOne);
		pits.add(pit);
		
		pit.addPropertyChangeListener(AbstractPit.PROPERTY_SEEDS, seedsChangeListener);
		
		AbstractPit newPit;
		
		for(int i = 2; i<=14; i++){
			if(i==7 || i==14)
				newPit = new Store();
			else
				newPit = new Pit();
			
			if(i<=7)
				newPit.setPlayer(playerOne);
			else
				newPit.setPlayer(playerTwo);
			
			pit.setNextPit(newPit);
			pits.add(newPit);
			pit = newPit;
			if(i==14)
				newPit.setNextPit(pits.get(0));
			
			//add property change listeners
			pit.addPropertyChangeListener(AbstractPit.PROPERTY_SEEDS, seedsChangeListener);
		}
		
		Pit  opit;
		for(int i=0; i<6;i++){
			opit = (Pit) pits.get(i);
			opit.setOppositePit((Pit) pits.get(12-i));
		}
	}
	
	public static void main(String[] args){
		
		// sets up the gameboard
		GameController controller = new GameController();
		controller.initializePits();
		//TODO bind gameboard status with gui text
		// launches the gui
		SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				MancalaGUI gui = new MancalaGUI();
				gui.getJFrame().setVisible(true);
			}
		});
		
		/*controller.pits.get(10).setSeeds(221);
		controller.pits.get(2).setSeeds(666);
		System.out.println(controller.pits.size());
		System.out.println(controller.pits.get(13).getClass());
		System.out.println(((Pit)controller.pits.get(10)).getOppositePit().getSeeds());*/
	}
}
