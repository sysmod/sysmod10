package sysmod.mancala;

import javax.swing.SwingUtilities;

public class StartMancala {
	public static void main(String[] args) {
		final GameController cntrl = new GameController();
		SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				cntrl.gui.getJFrame().setVisible(true);
			}
		});
	}
}
