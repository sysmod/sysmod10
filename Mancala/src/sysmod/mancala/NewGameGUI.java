package sysmod.mancala;

import javax.swing.JPanel;
import java.awt.Frame;
import java.awt.BorderLayout;
import javax.swing.JDialog;
import java.awt.GridBagLayout;
import javax.swing.JLabel;
import java.awt.GridBagConstraints;
import javax.swing.JTextField;
import javax.swing.JRadioButton;

public class NewGameGUI extends JDialog {

	private static final long serialVersionUID = 1L;
	private JPanel jContentPane = null;
	private JLabel newgameLabel = null;
	private JTextField newgamePlayer1 = null;
	private JLabel newgameLabel1 = null;
	private JRadioButton newgameHuman = null;
	private JTextField newgamePlayer2 = null;
	private JRadioButton newgameComputer = null;

	/**
	 * @param owner
	 */
	public NewGameGUI(Frame owner) {
		super(owner);
		initialize();
	}

	/**
	 * This method initializes this
	 * 
	 * @return void
	 */
	private void initialize() {
		this.setSize(300, 200);
		this.setTitle("New Game");
		this.setContentPane(getJContentPane());
	}

	/**
	 * This method initializes jContentPane
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getJContentPane() {
		if (jContentPane == null) {
			GridBagConstraints gridBagConstraints5 = new GridBagConstraints();
			gridBagConstraints5.gridx = 1;
			gridBagConstraints5.gridy = 2;
			GridBagConstraints gridBagConstraints4 = new GridBagConstraints();
			gridBagConstraints4.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints4.gridy = 1;
			gridBagConstraints4.weightx = 1.0;
			gridBagConstraints4.gridx = 2;
			GridBagConstraints gridBagConstraints3 = new GridBagConstraints();
			gridBagConstraints3.gridx = 1;
			gridBagConstraints3.gridy = 1;
			GridBagConstraints gridBagConstraints2 = new GridBagConstraints();
			gridBagConstraints2.gridx = 0;
			gridBagConstraints2.gridy = 1;
			newgameLabel1 = new JLabel();
			newgameLabel1.setText("Opponent:");
			GridBagConstraints gridBagConstraints1 = new GridBagConstraints();
			gridBagConstraints1.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints1.gridy = 0;
			gridBagConstraints1.weightx = 1.0;
			gridBagConstraints1.gridx = 1;
			GridBagConstraints gridBagConstraints = new GridBagConstraints();
			gridBagConstraints.gridx = 0;
			gridBagConstraints.gridy = 0;
			newgameLabel = new JLabel();
			newgameLabel.setText("Your name:");
			jContentPane = new JPanel();
			jContentPane.setLayout(new GridBagLayout());
			jContentPane.add(newgameLabel, gridBagConstraints);
			jContentPane.add(getNewgamePlayer1(), gridBagConstraints1);
			jContentPane.add(newgameLabel1, gridBagConstraints2);
			jContentPane.add(getNewgameHuman(), gridBagConstraints3);
			jContentPane.add(getNewgamePlayer2(), gridBagConstraints4);
			jContentPane.add(getNewgameComputer(), gridBagConstraints5);
		}
		return jContentPane;
	}

	/**
	 * This method initializes newgamePlayer1	
	 * 	
	 * @return javax.swing.JTextField	
	 */
	private JTextField getNewgamePlayer1() {
		if (newgamePlayer1 == null) {
			newgamePlayer1 = new JTextField();
			newgamePlayer1.setSize(60, 12);
			newgamePlayer1.setHorizontalAlignment(JTextField.LEFT);
			newgamePlayer1.setText("anonymous");
		}
		return newgamePlayer1;
	}

	/**
	 * This method initializes newgameHuman	
	 * 	
	 * @return javax.swing.JRadioButton	
	 */
	private JRadioButton getNewgameHuman() {
		if (newgameHuman == null) {
			newgameHuman = new JRadioButton();
			newgameHuman.setName("");
			newgameHuman.setText("Human with name ");
		}
		return newgameHuman;
	}

	/**
	 * This method initializes newgamePlayer2	
	 * 	
	 * @return javax.swing.JTextField	
	 */
	private JTextField getNewgamePlayer2() {
		if (newgamePlayer2 == null) {
			newgamePlayer2 = new JTextField();
			newgamePlayer2.setText("anonymous2");
		}
		return newgamePlayer2;
	}

	/**
	 * This method initializes newgameComputer	
	 * 	
	 * @return javax.swing.JRadioButton	
	 */
	private JRadioButton getNewgameComputer() {
		if (newgameComputer == null) {
			newgameComputer = new JRadioButton();
			newgameComputer.setText("Computer");
		}
		return newgameComputer;
	}

}
