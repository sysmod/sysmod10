package sysmod.mancala;

import java.awt.BorderLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;

public class MancalaGUI extends JFrame {
	private List<JButton> pits = new ArrayList<JButton>();
	private JButton playerStore;
	private JButton opponentStore;

	MancalaGUI() {
		super();
		this.setSize(600, 400);
		this.setTitle("Mancala");

		initializeItems();

		setVisible(true);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	void initializeItems() {
		getContentPane().setLayout(new GridBagLayout());
		GridBagConstraints c = new GridBagConstraints();
		JButton pit;
		for (int i = 0; i < 12; i++) {
			pit = new JButton("Pit " + (i + 1));
			pits.add(pit);
			if (i < 6) {
				c.gridy = 2;
				c.gridx = i;
				getContentPane().add(pit, c);
			} else {
				c.gridy = 0;
				c.gridx = 11 - i;
				getContentPane().add(pit, c);
			}
		}

		playerStore = new JButton("Player");
		c.gridx = 5;
		c.gridy = 1;
		getContentPane().add(playerStore, c);

		opponentStore = new JButton("Opponent");
		c.gridx = 0;
		c.gridy = 1;
		getContentPane().add(opponentStore, c);
	}

	public static void main(String[] args) {
		new MancalaGUI();
	}
}
