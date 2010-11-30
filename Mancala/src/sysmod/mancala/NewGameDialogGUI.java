package sysmod.mancala;

import javax.swing.JPanel;
import java.awt.Frame;
import javax.swing.JDialog;
import java.awt.GridBagLayout;
import javax.swing.JLabel;
import java.awt.GridBagConstraints;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JRadioButton;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class NewGameDialogGUI extends JDialog {

	private static final long serialVersionUID = 1L;
	private JPanel jContentPane = null;
	private JTextField playerOneName;
	private JTextField playerTwoName;
	private JLabel playerOneNameText;
	private JLabel playerTwoNameText;
	private JRadioButton playAgainstComputer;
	private JRadioButton playAgainstHuman;
	private ButtonGroup playerChoice;
	private JButton startButton;
	private Boolean computerPlayerSelected = null;
	private JDialog thisDialog;
	private ChangeListener selectionChangeListener = new ChangeListener() {

		@Override
		public void stateChanged(ChangeEvent e) {
			if (playAgainstHuman.isSelected()) {
				playerTwoNameText.setEnabled(true);
				playerTwoName.setEnabled(true);

			} else {
				playerTwoNameText.setEnabled(false);
				playerTwoName.setEnabled(false);
			}

		}

	};

	/**
	 * @param owner
	 */
	public NewGameDialogGUI(Frame owner) {
		super(owner);
		thisDialog = this;
		this.setLocation(owner.getX(), owner.getY());
		initialize();
	}

	public JTextField getPlayerOneName() {
		return playerOneName;
	}

	public JTextField getPlayerTwoName() {
		return playerTwoName;
	}

	public Boolean getComputerPlayerSelected() {
		return computerPlayerSelected;
	}

	/**
	 * This method initializes this new game dialog window
	 * 
	 * @return void
	 */
	private void initialize() {
		// this.setSize(300, 200);
		this.setTitle("New Game");
		this.setContentPane(getJContentPane());
		this.pack();
		this.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		this.setModalityType(JDialog.DEFAULT_MODALITY_TYPE);
		this.setVisible(true);
	}

	/**
	 * This method initializes jContentPane
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getJContentPane() {
		if (jContentPane == null) {
			jContentPane = new JPanel();
			jContentPane.setLayout(new GridBagLayout());
			GridBagConstraints gc = new GridBagConstraints();

			playerOneNameText = new JLabel("Player 1 name:");
			gc.gridx = 0;
			gc.gridy = 0;
			jContentPane.add(playerOneNameText, gc);

			playerOneName = new JTextField(15);
			gc.gridx = 1;
			gc.gridy = 0;
			jContentPane.add(playerOneName, gc);

			playerChoice = new ButtonGroup();
			playAgainstHuman = new JRadioButton("Play against human");
			playAgainstHuman.setSelected(true);
			playAgainstHuman.addChangeListener(selectionChangeListener);
			playerChoice.add(playAgainstHuman);
			gc.gridx = 0;
			gc.gridy = 1;
			jContentPane.add(playAgainstHuman, gc);

			playerTwoNameText = new JLabel("Player 2 name:");
			gc.gridx = 0;
			gc.gridy = 2;
			jContentPane.add(playerTwoNameText, gc);

			playerTwoName = new JTextField(15);
			gc.gridx = 1;
			gc.gridy = 2;
			jContentPane.add(playerTwoName, gc);

			playAgainstComputer = new JRadioButton("Play against computer");
			playerChoice.add(playAgainstComputer);
			playAgainstComputer.addChangeListener(selectionChangeListener);
			gc.gridx = 0;
			gc.gridy = 3;
			jContentPane.add(playAgainstComputer, gc);

			startButton = new JButton("Start new game!");
			gc.gridx = 0;
			gc.gridwidth = 2;
			gc.gridy = 4;
			jContentPane.add(startButton, gc);
			startButton.addActionListener(new ActionListener() {

				@Override
				public void actionPerformed(ActionEvent e) {
					if (playAgainstComputer.isSelected())
						computerPlayerSelected = true;
					else
						computerPlayerSelected = false;

					thisDialog.dispose();
				}
			});
		}
		return jContentPane;
	}

}
