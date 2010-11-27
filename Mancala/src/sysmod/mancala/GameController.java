package sysmod.mancala;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.util.ArrayList;
import java.util.List;

import javax.sound.midi.ControllerEventListener;
import javax.swing.SwingUtilities;

import de.upb.tools.fca.SetTools;

public class GameController {

	public MancalaGUI gui = new MancalaGUI();
	
	// model objects
	private List<AbstractPit> pits = new ArrayList<AbstractPit>();
	private Player playerOne;
	private Player playerTwo;
	private Turn turn;

	private PropertyChangeListener seedsChangeListener = new PropertyChangeListener() {

		@Override
		public void propertyChange(PropertyChangeEvent evt) {

			System.out.println("Seedchange triggered: " + evt.toString());
			//TODO logic still missing
			updateGUI();

		}

	};

	private PropertyChangeListener turnChangeListener = new PropertyChangeListener() {

		@Override
		public void propertyChange(PropertyChangeEvent evt) {

			System.out.println("Turnchange triggered: " + evt.toString());
			//TODO logic still missing

		}

	};
	
	public GameController(){
		initializePits();
		initializeGUIlisteners();
	}

	private void initializePits() {
		AbstractPit pit = new Pit();
		pit.setPlayer(playerOne);
		pits.add(pit);

		pit.addPropertyChangeListener(AbstractPit.PROPERTY_SEEDS,
				seedsChangeListener);

		AbstractPit newPit;

		for (int i = 2; i <= 14; i++) {
			if (i == 7 || i == 14)
				newPit = new Store();
			else 
				newPit = new Pit();


			if (i <= 7)
				newPit.setPlayer(playerOne);
			else
				newPit.setPlayer(playerTwo);

			pit.setNextPit(newPit);
			pits.add(newPit);
			pit = newPit;
			if (i == 14)
				newPit.setNextPit(pits.get(0));

			// add property change listeners
			pit.addPropertyChangeListener(AbstractPit.PROPERTY_SEEDS,
					seedsChangeListener);
		}

		Pit opit;
		for (int i = 0; i < 6; i++) {
			opit = (Pit) pits.get(i);
			opit.setOppositePit((Pit) pits.get(12 - i));
		}
	}
	
	private void initializeGUIlisteners(){
		gui.getNewgameButton().addActionListener(new ActionListener(){

			@Override
			public void actionPerformed(ActionEvent e) {
				System.out.println("new button yeah!");
				for(int i = 0; i< 14; i++){
					if(i==6||i==13)
						pits.get(i).setSeeds(0);
					else
						pits.get(i).setSeeds(4);
				}
				
			}
			
		});
	}

	private void updateGUI() {

		gui.getPit1().setText(Integer.toString(this.pits.get(0).getSeeds()));
		gui.getPit2().setText(Integer.toString(this.pits.get(1).getSeeds()));
		gui.getPit3().setText(Integer.toString(this.pits.get(2).getSeeds()));
		gui.getPit4().setText(Integer.toString(this.pits.get(3).getSeeds()));
		gui.getPit5().setText(Integer.toString(this.pits.get(4).getSeeds()));
		gui.getPit6().setText(Integer.toString(this.pits.get(5).getSeeds()));
		gui.getPit7().setText(Integer.toString(this.pits.get(7).getSeeds()));
		gui.getPit8().setText(Integer.toString(this.pits.get(8).getSeeds()));
		gui.getPit9().setText(Integer.toString(this.pits.get(9).getSeeds()));
		gui.getPit10().setText(Integer.toString(this.pits.get(10).getSeeds()));
		gui.getPit11().setText(Integer.toString(this.pits.get(11).getSeeds()));
		gui.getPit12().setText(Integer.toString(this.pits.get(12).getSeeds()));

		gui.getPlayer1Store().setText(
				Integer.toString(this.pits.get(6).getSeeds()));
		gui.getPlayer2Store().setText(
				Integer.toString(this.pits.get(13).getSeeds()));

	}
	
	private void makeMove(){
		
	}
	/*
	public void registerMove(int guiPitId) {

		int arrayListId;
		Player player;

		if (guiPitId <= 6) {
			arrayListId = guiPitId - 1;
			player = controller.playerOne;
		} else {
			arrayListId = guiPitId;
			player = controller.playerTwo;
		}
		
		System.out.println(arrayListId);
		player.makeMove((Pit) controller.pits.get(arrayListId));

	}
	*/

	public static void main(String[] args) {
		/*
		controller.initializePits();
		gui = new MancalaGUI();
		controller.updateGUI(gui);
		*/
		final GameController cntrl = new GameController();
		cntrl.gui.getJFrame().setVisible(true);
		SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				cntrl.gui.getJFrame().setVisible(true);
			}
		});
	}
}
