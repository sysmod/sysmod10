package sysmod.mancala;

import java.awt.BorderLayout;
import javax.swing.SwingConstants;
import java.awt.Point;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.JDialog;
import java.awt.Dimension;
import javax.swing.JTextArea;
import javax.swing.JButton;

import java.awt.Color;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Font;
import java.awt.Rectangle;
import java.awt.SystemColor;
import javax.swing.BorderFactory;
import javax.swing.JTextPane;
import java.awt.Insets;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.JComboBox;
import javax.swing.border.BevelBorder;

public class MancalaGUI {

	private JFrame jFrame = null;  //  @jve:decl-index=0:visual-constraint="33,27"
	private JPanel jContentPane = null;
	private JDialog teamDialog = null; // @jve:decl-index=0:visual-constraint="19,332"
	private JPanel aboutContentPane = null;
	private JTextArea aboutText = null;
	private JLabel aboutTitle = null;
	private JPanel Gameboard = null;
	private JButton pit12 = null;
	private JButton pit11 = null;
	private JButton pit1 = null;
	private JButton pit10 = null;
	private JButton pit9 = null;
	private JButton pit8 = null;
	private JButton pit7 = null;
	private JButton pit2 = null;
	private JButton pit3 = null;
	private JButton pit4 = null;
	private JButton pit5 = null;
	private JButton pit6 = null;
	private JButton player1store = null;
	private JButton player2store = null;
	private JLabel title = null;
	private JLabel player2label = null;
	private JLabel player1label = null;
	private JPanel rightPanel = null;
	private JButton helpButton = null;
	private JButton teamButton = null;
	private JDialog helpDialog = null; // @jve:decl-index=0:visual-constraint="336,331"
	private JPanel help = null;
	private JLabel helpTitle = null;
	private JTextPane helpText = null;
	private JButton newgameButton = null;
	private JDialog newgameDialog = null;  //  @jve:decl-index=0:visual-constraint="643,314"
	private JPanel newgameContent = null;
	private JLabel newgameLabel1 = null;
	private JLabel newgameLabel = null;
	private JTextField newgamePlayer1 = null;
	private JLabel newgameOpponent = null;
	private JTextField newgamePlayer2 = null;
	private JComboBox newgameOpponentType = null;
	private JPanel panelDown = null;
	private JLabel player1Name = null;
	private JLabel player1Score = null;
	private JLabel player2Name = null;
	private JLabel player2Score = null;
	private JLabel playerSpace = null;
	/**
	 * This method initializes jFrame
	 * 
	 * @return javax.swing.JFrame
	 */
	JFrame getJFrame() {
		if (jFrame == null) {
			jFrame = new JFrame();
			jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			jFrame.setBounds(new Rectangle(0, 0, 600, 300));
			jFrame.setMinimumSize(new Dimension(600, 300));
			jFrame.setMaximumSize(new Dimension(600, 300));
			jFrame.setContentPane(getJContentPane());
			jFrame.setTitle("Mancala");
		}
		return jFrame;
	}

	/**
	 * This method initializes jContentPane
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getJContentPane() {
		if (jContentPane == null) {
			title = new JLabel();
			title.setText("Mancala");
			title.setHorizontalAlignment(SwingConstants.CENTER);
			title.setFont(new Font("Dialog", Font.BOLD, 24));
			jContentPane = new JPanel();
			jContentPane.setLayout(new BorderLayout());
			jContentPane.add(title, BorderLayout.NORTH);
			jContentPane.add(getRightPanel(), BorderLayout.EAST);
			jContentPane.add(getPanelDown(), BorderLayout.SOUTH);
			jContentPane.add(getGameboard(), BorderLayout.CENTER);
		}
		return jContentPane;
	}

	/**
	 * This method initializes teamDialog
	 * 
	 * @return javax.swing.JDialog
	 */
	private JDialog getTeamDialog() {
		if (teamDialog == null) {
			teamDialog = new JDialog(getJFrame(), true);
			teamDialog.setTitle("Mancala Team");
			teamDialog.setFont(new Font("Dialog", Font.PLAIN, 14));
			teamDialog.setMinimumSize(new Dimension(300, 200));
			teamDialog.setMaximumSize(new Dimension(300, 200));
			teamDialog.setBounds(new Rectangle(0, 0, 300, 200));
			teamDialog.setContentPane(getAboutContentPane());
		}
		return teamDialog;
	}

	/**
	 * This method initializes aboutContentPane
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getAboutContentPane() {
		if (aboutContentPane == null) {
			aboutTitle = new JLabel();
			aboutTitle.setText("Mancala Team");
			aboutTitle.setFont(new Font("Dialog", Font.BOLD, 14));
			aboutContentPane = new JPanel();
			aboutContentPane.setLayout(new BorderLayout());
			aboutContentPane.add(getAboutText(), BorderLayout.CENTER);
			aboutContentPane.add(aboutTitle, BorderLayout.NORTH);
		}
		return aboutContentPane;
	}

	/**
	 * This method initializes aboutText
	 * 
	 * @return javax.swing.JTextArea
	 */
	private JTextArea getAboutText() {
		if (aboutText == null) {
			aboutText = new JTextArea();
			aboutText.setSize(100, 70);
			aboutText.setName("About");
			aboutText.setBackground(SystemColor.activeCaptionBorder);
			aboutText.setText(" - Martin Loginov \n - Hans Mäesalu \n - Peeter Jürviste \n - Mari Rüütli \n - Sven Aller");
			aboutText.setEditable(false);
		}
		return aboutText;
	}

	/**
	 * This method initializes Gameboard
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getGameboard() {
		if (Gameboard == null) {
			GridBagConstraints gridBagConstraints22 = new GridBagConstraints();
			gridBagConstraints22.gridx = 3;
			gridBagConstraints22.gridwidth = 3;
			gridBagConstraints22.gridy = 4;
			player1label = new JLabel();
			player1label.setText("Player 1");
			player1label.setHorizontalAlignment(SwingConstants.CENTER);
			player1label.setFont(new Font("Dialog", Font.BOLD, 16));
			GridBagConstraints gridBagConstraints13 = new GridBagConstraints();
			gridBagConstraints13.gridx = 3;
			gridBagConstraints13.gridwidth = 3;
			gridBagConstraints13.gridy = 0;
			player2label = new JLabel();
			player2label.setText("Player 2");
			player2label.setHorizontalAlignment(SwingConstants.CENTER);
			player2label.setFont(new Font("Dialog", Font.BOLD, 16));
			GridBagConstraints gridBagConstraints12 = new GridBagConstraints();
			gridBagConstraints12.gridx = 0;
			gridBagConstraints12.gridy = 2;
			GridBagConstraints gridBagConstraints10 = new GridBagConstraints();
			gridBagConstraints10.gridx = 8;
			gridBagConstraints10.anchor = GridBagConstraints.NORTH;
			gridBagConstraints10.gridy = 2;
			GridBagConstraints gridBagConstraints9 = new GridBagConstraints();
			gridBagConstraints9.gridx = 7;
			gridBagConstraints9.gridy = 3;
			GridBagConstraints gridBagConstraints8 = new GridBagConstraints();
			gridBagConstraints8.gridx = 6;
			gridBagConstraints8.gridy = 3;
			GridBagConstraints gridBagConstraints7 = new GridBagConstraints();
			gridBagConstraints7.gridx = 5;
			gridBagConstraints7.gridy = 3;
			GridBagConstraints gridBagConstraints6 = new GridBagConstraints();
			gridBagConstraints6.gridx = 3;
			gridBagConstraints6.gridy = 3;
			GridBagConstraints gridBagConstraints5 = new GridBagConstraints();
			gridBagConstraints5.gridx = 2;
			gridBagConstraints5.gridy = 3;
			GridBagConstraints gridBagConstraints4 = new GridBagConstraints();
			gridBagConstraints4.gridx = 7;
			gridBagConstraints4.gridy = 1;
			GridBagConstraints gridBagConstraints3 = new GridBagConstraints();
			gridBagConstraints3.gridx = 6;
			gridBagConstraints3.gridy = 1;
			GridBagConstraints gridBagConstraints21 = new GridBagConstraints();
			gridBagConstraints21.gridx = 5;
			gridBagConstraints21.gridy = 1;
			GridBagConstraints gridBagConstraints11 = new GridBagConstraints();
			gridBagConstraints11.gridx = 3;
			gridBagConstraints11.gridy = 1;
			GridBagConstraints gridBagConstraints2 = new GridBagConstraints();
			gridBagConstraints2.gridx = 1;
			gridBagConstraints2.gridy = 3;
			GridBagConstraints gridBagConstraints1 = new GridBagConstraints();
			gridBagConstraints1.gridx = 2;
			gridBagConstraints1.gridy = 1;
			GridBagConstraints gridBagConstraints = new GridBagConstraints();
			gridBagConstraints.gridx = 1;
			gridBagConstraints.gridy = 1;
			Gameboard = new JPanel();
			Gameboard.setLayout(new GridBagLayout());
			Gameboard.setEnabled(false);
			Gameboard.setBackground(SystemColor.activeCaptionBorder);
			Gameboard.setBorder(BorderFactory.createBevelBorder(BevelBorder.RAISED));
			Gameboard.add(getPit12(), gridBagConstraints);
			Gameboard.add(getPit11(), gridBagConstraints1);
			Gameboard.add(getPit1(), gridBagConstraints2);
			Gameboard.add(getPit10(), gridBagConstraints11);
			Gameboard.add(getPit9(), gridBagConstraints21);
			Gameboard.add(getPit8(), gridBagConstraints3);
			Gameboard.add(getPit7(), gridBagConstraints4);
			Gameboard.add(getPit2(), gridBagConstraints5);
			Gameboard.add(getPit3(), gridBagConstraints6);
			Gameboard.add(getPit4(), gridBagConstraints7);
			Gameboard.add(getPit5(), gridBagConstraints8);
			Gameboard.add(getPit6(), gridBagConstraints9);
			Gameboard.add(getPlayer1Store(), gridBagConstraints10);
			Gameboard.add(getPlayer2Store(), gridBagConstraints12);
			Gameboard.add(player2label, gridBagConstraints13);
			Gameboard.add(player1label, gridBagConstraints22);
		}
		return Gameboard;
	}

	/**
	 * This method initializes player1store
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPlayer1Store() {
		if (player1store == null) {
			player1store = new JButton();
			player1store.setPreferredSize(new Dimension(60, 26));
			player1store.setHorizontalAlignment(SwingConstants.CENTER);
			player1store.setFont(new Font("Dialog", Font.BOLD, 14));
			player1store.setEnabled(false);
		}
		return player1store;
	}

	/**
	 * This method initializes player2store
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPlayer2Store() {
		if (player2store == null) {
			player2store = new JButton();
			player2store.setPreferredSize(new Dimension(60, 26));
			player2store.setHorizontalAlignment(SwingConstants.CENTER);
			player2store.setFont(new Font("Dialog", Font.BOLD, 14));
			player2store.setEnabled(false);
		}
		return player2store;
	}

	/**
	 * This method initializes pit12
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit12() {
		if (pit12 == null) {
			pit12 = new JButton();
			pit12.setFont(new Font("Dialog", Font.BOLD, 14));
			pit12.setPreferredSize(new Dimension(60, 26));
		}
		return pit12;
	}

	/**
	 * This method initializes pit11
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit11() {
		if (pit11 == null) {
			pit11 = new JButton();
			pit11.setFont(new Font("Dialog", Font.BOLD, 14));
			pit11.setPreferredSize(new Dimension(60, 26));
		}
		return pit11;
	}

	/**
	 * This method initializes pit1
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit1() {
		if (pit1 == null) {
			pit1 = new JButton();
			pit1.setFont(new Font("Dialog", Font.BOLD, 14));
			pit1.setPreferredSize(new Dimension(60, 26));
		}
		return pit1;
	}

	/**
	 * This method initializes pit2
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit2() {
		if (pit2 == null) {
			pit2 = new JButton();
			pit2.setFont(new Font("Dialog", Font.BOLD, 14));
			pit2.setPreferredSize(new Dimension(60, 26));
		}
		return pit2;
	}

	/**
	 * This method initializes pit3
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit3() {
		if (pit3 == null) {
			pit3 = new JButton();
			pit3.setFont(new Font("Dialog", Font.BOLD, 14));
			pit3.setPreferredSize(new Dimension(60, 26));
		}
		return pit3;
	}

	/**
	 * This method initializes pit4
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit4() {
		if (pit4 == null) {
			pit4 = new JButton();
			pit4.setFont(new Font("Dialog", Font.BOLD, 14));
			pit4.setPreferredSize(new Dimension(60, 26));
		}
		return pit4;
	}

	/**
	 * This method initializes pit5
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit5() {
		if (pit5 == null) {
			pit5 = new JButton();
			pit5.setFont(new Font("Dialog", Font.BOLD, 14));
			pit5.setPreferredSize(new Dimension(60, 26));
		}
		return pit5;
	}

	/**
	 * This method initializes pit6
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit6() {
		if (pit6 == null) {
			pit6 = new JButton();
			pit6.setFont(new Font("Dialog", Font.BOLD, 14));
			pit6.setPreferredSize(new Dimension(60, 26));
		}
		return pit6;
	}

	/**
	 * This method initializes pit7
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit7() {
		if (pit7 == null) {
			pit7 = new JButton();
			pit7.setFont(new Font("Dialog", Font.BOLD, 14));
			pit7.setPreferredSize(new Dimension(60, 26));
		}
		return pit7;
	}

	/**
	 * This method initializes pit8
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit8() {
		if (pit8 == null) {
			pit8 = new JButton();
			pit8.setFont(new Font("Dialog", Font.BOLD, 14));
			pit8.setPreferredSize(new Dimension(60, 26));
		}
		return pit8;
	}

	/**
	 * This method initializes pit9
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit9() {
		if (pit9 == null) {
			pit9 = new JButton();
			pit9.setFont(new Font("Dialog", Font.BOLD, 14));
			pit9.setPreferredSize(new Dimension(60, 26));
		}
		return pit9;
	}

	/**
	 * This method initializes pit10
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPit10() {
		if (pit10 == null) {
			pit10 = new JButton();
			pit10.setFont(new Font("Dialog", Font.BOLD, 14));
			pit10.setPreferredSize(new Dimension(60, 26));
			}
		return pit10;
	}

	/**
	 * This method initializes rightPanel
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getRightPanel() {
		if (rightPanel == null) {
			GridBagConstraints gridBagConstraints16 = new GridBagConstraints();
			gridBagConstraints16.gridx = 0;
			gridBagConstraints16.gridy = 1;
			GridBagConstraints gridBagConstraints15 = new GridBagConstraints();
			gridBagConstraints15.gridx = 0;
			gridBagConstraints15.gridy = 3;
			GridBagConstraints gridBagConstraints14 = new GridBagConstraints();
			gridBagConstraints14.gridx = 0;
			gridBagConstraints14.gridy = 2;
			rightPanel = new JPanel();
			rightPanel.setLayout(new GridBagLayout());
			rightPanel.setSize(130, 300);
			rightPanel.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0));
			rightPanel.setPreferredSize(new Dimension(140, 78));
			rightPanel.add(getHelpButton(), gridBagConstraints14);
			rightPanel.add(getTeamButton(), gridBagConstraints15);
			rightPanel.add(getNewgameButton(), gridBagConstraints16);
		}
		return rightPanel;
	}

	/**
	 * This method initializes helpButton
	 * 
	 * @return javax.swing.JButton
	 */
	private JButton getHelpButton() {
		if (helpButton == null) {
			helpButton = new JButton();
			helpButton.setText("Help");
			helpButton.setPreferredSize(new Dimension(120, 26));
			helpButton.setFont(new Font("Dialog", Font.BOLD, 14));
			helpButton.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					JDialog helpDialog = getHelpDialog();
					helpDialog.pack();
					Point loc = getJFrame().getLocation();
					loc.translate(20, 50);
					helpDialog.setLocation(loc);
					helpDialog.setVisible(true);
				}
			});
		}
		return helpButton;
	}

	/**
	 * This method initializes teamButton
	 * 
	 * @return javax.swing.JButton
	 */
	private JButton getTeamButton() {
		if (teamButton == null) {
			teamButton = new JButton();
			teamButton.setText("Team");

			teamButton.setPreferredSize(new Dimension(120, 26));
			teamButton.setFont(new Font("Dialog", Font.BOLD, 14));
			teamButton.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					JDialog aboutDialog = getTeamDialog();
					aboutDialog.pack();
					Point loc = getJFrame().getLocation();
					loc.translate(260, 80);
					aboutDialog.setLocation(loc);
					aboutDialog.setVisible(true);
				}
			});
		}
		return teamButton;
	}

	/**
	 * This method initializes helpDialog
	 * 
	 * @return javax.swing.JDialog
	 */
	private JDialog getHelpDialog() {
		if (helpDialog == null) {
			helpDialog = new JDialog(getJFrame());
			helpDialog.setTitle("Mancala Help");
			helpDialog.setBounds(new Rectangle(0, 0, 300, 200));
			helpDialog.setMinimumSize(new Dimension(300, 200));
			helpDialog.setMaximumSize(new Dimension(300, 200));
			helpDialog.setContentPane(getHelp());
		}
		return helpDialog;
	}

	/**
	 * This method initializes help
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getHelp() {
		if (help == null) {
			helpTitle = new JLabel();
			helpTitle.setText("Mancala Help");
			helpTitle.setFont(new Font("Dialog", Font.BOLD, 14));
			help = new JPanel();
			help.setLayout(new BorderLayout());
			help.add(helpTitle, BorderLayout.NORTH);
			help.add(getHelpText(), BorderLayout.CENTER);
		}
		return help;
	}

	/**
	 * This method initializes helpText
	 * 
	 * @return javax.swing.JTextPane
	 */
	private JTextPane getHelpText() {
		if (helpText == null) {
			helpText = new JTextPane();
			helpText.setText("... uf khjg jkhg kjhg kjhg bjhg kujhg bjhg \nkjgh kjhg jkh kjh kjhg kjhv kjhv kjhv kjhv ");
			helpText.setBackground(SystemColor.activeCaptionBorder);
		}
		return helpText;
	}

	/**
	 * This method initializes newgameButton
	 * 
	 * @return javax.swing.JButton
	 */
	public JButton getNewgameButton() {
		if (newgameButton == null) {
			newgameButton = new JButton();
			newgameButton.setText("New game");
			newgameButton.setFont(new Font("Dialog", Font.BOLD, 14));
			newgameButton.setPreferredSize(new Dimension(120, 26));
			newgameButton.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					JDialog newnameDialog = getNewgameDialog();
					newnameDialog.pack();
					Point loc = getJFrame().getLocation();
					loc.translate(20, 50);
					newnameDialog.setLocation(loc);
					newnameDialog.setVisible(true);
				}
			});
		}
		return newgameButton;
	}

	/**
	 * This method initializes newgameDialog	
	 * 	
	 * @return javax.swing.JDialog	
	 */
	private JDialog getNewgameDialog() {
		
		if (newgameDialog == null) {
			newgameDialog = new JDialog(getJFrame());
			newgameDialog.setTitle("New Game");
			newgameDialog.setSize(new Dimension(252, 141));
			newgameDialog.setBounds(new Rectangle(0, 0, 300, 200));
			newgameDialog.setMinimumSize(new Dimension(300, 200));
			newgameDialog.setMaximumSize(new Dimension(300, 200));
			newgameDialog.setContentPane(getNewgameContent());
		}
		
		
		return newgameDialog;
	}

	/**
	 * This method initializes newgameContent	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getNewgameContent() {
		if (newgameContent == null) {
			GridBagConstraints gridBagConstraints26 = new GridBagConstraints();
			gridBagConstraints26.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints26.gridy = 1;
			gridBagConstraints26.weightx = 1.0;
			gridBagConstraints26.gridx = 1;
			GridBagConstraints gridBagConstraints19 = new GridBagConstraints();
			gridBagConstraints19.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints19.gridy = 1;
			gridBagConstraints19.weightx = 1.0;
			gridBagConstraints19.gridx = 1;
			GridBagConstraints gridBagConstraints18 = new GridBagConstraints();
			gridBagConstraints18.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints18.gridy = 1;
			gridBagConstraints18.weightx = 1.0;
			gridBagConstraints18.gridx = 1;
			GridBagConstraints gridBagConstraints25 = new GridBagConstraints();
			gridBagConstraints25.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints25.gridy = 1;
			gridBagConstraints25.weightx = 1.0;
			gridBagConstraints25.gridx = 2;
			GridBagConstraints gridBagConstraints24 = new GridBagConstraints();
			gridBagConstraints24.gridx = 3;
			gridBagConstraints24.gridy = 1;
			newgameOpponent = new JLabel();
			newgameOpponent.setText("");
			GridBagConstraints gridBagConstraints23 = new GridBagConstraints();
			gridBagConstraints23.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints23.gridy = 0;
			gridBagConstraints23.weightx = 1.0;
			gridBagConstraints23.gridx = 1;
			GridBagConstraints gridBagConstraints20 = new GridBagConstraints();
			gridBagConstraints20.gridx = 0;
			gridBagConstraints20.gridy = 0;
			newgameLabel = new JLabel();
			newgameLabel.setText("Your name:");
			newgameLabel.setHorizontalAlignment(SwingConstants.RIGHT);
			GridBagConstraints gridBagConstraints17 = new GridBagConstraints();
			gridBagConstraints17.gridx = 0;
			gridBagConstraints17.gridy = 1;
			newgameLabel1 = new JLabel();
			newgameLabel1.setText("Select opponent");
			newgameLabel1.setHorizontalAlignment(SwingConstants.RIGHT);
			newgameContent = new JPanel();
			newgameContent.setLayout(new GridBagLayout());
			newgameContent.add(newgameLabel1, gridBagConstraints17);
			newgameContent.add(newgameLabel, gridBagConstraints20);
			newgameContent.add(getNewgamePlayer1(), gridBagConstraints23);
			newgameContent.add(newgameOpponent, gridBagConstraints24);
			newgameContent.add(getNewgamePlayer2(), gridBagConstraints25);

			newgameContent.add(getNewgameOpponentType(), gridBagConstraints26);
		}
		return newgameContent;
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
			newgamePlayer1.setText("Anonymous1");
			player1Name.setText(newgamePlayer1.getText() + ": ");
			newgamePlayer1.addFocusListener(new java.awt.event.FocusAdapter() {
				public void focusLost(java.awt.event.FocusEvent e) {
					System.out.println("Player 1: " + newgamePlayer1.getText()); // TODO Auto-generated Event stub focusLost()
					player1Name.setText(newgamePlayer1.getText() + ": ");
				}
			});
			
		}
		return newgamePlayer1;
	}

	/**
	 * This method initializes newgamePlayer2	
	 * 	
	 * @return javax.swing.JTextField	
	 */
	private JTextField getNewgamePlayer2() {
		if (newgamePlayer2 == null) {
			newgamePlayer2 = new JTextField();
			newgamePlayer2.setSize(60, 12);
			newgamePlayer2.setText("Computer");
			player2Name.setText(newgamePlayer2.getText() + ": ");
			newgamePlayer2.addFocusListener(new java.awt.event.FocusAdapter() {
				public void focusLost(java.awt.event.FocusEvent e) {
					System.out.println("Player 2: " + newgamePlayer2.getText()); // TODO Auto-generated Event stub focusLost()
					player2Name.setText(newgamePlayer2.getText() + ": ");
				}
			});
		}
		return newgamePlayer2;
	}

	/**
	 * This method initializes newgameOpponentType	
	 * 	
	 * @return javax.swing.JComboBox	
	 */
	private JComboBox getNewgameOpponentType() {
		if (newgameOpponentType == null) {
			String combolabels[] = {"Human", "Computer"};
			newgameOpponentType = new JComboBox(combolabels);
			newgameOpponentType.addItemListener(new java.awt.event.ItemListener() {
				public void itemStateChanged(java.awt.event.ItemEvent e) {
					if (newgameOpponentType.getSelectedIndex() == 1) System.out.println("Mängib arvuti"); // TODO Auto-generated Event stub itemStateChanged()
				}
			});
		}
		return newgameOpponentType;
	}

	/**
	 * This method initializes panelDown	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getPanelDown() {
		if (panelDown == null) {
			GridBagConstraints gridBagConstraints32 = new GridBagConstraints();
			gridBagConstraints32.gridx = 2;
			gridBagConstraints32.gridy = 0;
			playerSpace = new JLabel();
			playerSpace.setText(" - ");
			playerSpace.setFont(new Font("Dialog", Font.BOLD, 14));
			GridBagConstraints gridBagConstraints31 = new GridBagConstraints();
			gridBagConstraints31.gridx = 4;
			gridBagConstraints31.gridy = 0;
			player2Score = new JLabel();
			player2Score.setText("0");
			player2Score.setHorizontalAlignment(SwingConstants.CENTER);
			player2Score.setFont(new Font("Dialog", Font.BOLD, 14));
			player2Score.setHorizontalTextPosition(SwingConstants.CENTER);
			GridBagConstraints gridBagConstraints30 = new GridBagConstraints();
			gridBagConstraints30.gridx = 3;
			gridBagConstraints30.gridy = 0;
			player2Name = new JLabel();
			player2Name.setText("Player2: ");
			player2Name.setHorizontalAlignment(SwingConstants.CENTER);
			player2Name.setFont(new Font("Dialog", Font.BOLD, 14));
			player2Name.setHorizontalTextPosition(SwingConstants.CENTER);
			GridBagConstraints gridBagConstraints29 = new GridBagConstraints();
			gridBagConstraints29.gridx = 1;
			gridBagConstraints29.gridy = 0;
			player1Score = new JLabel();
			player1Score.setText("0");
			player1Score.setHorizontalAlignment(SwingConstants.CENTER);
			player1Score.setFont(new Font("Dialog", Font.BOLD, 14));
			player1Score.setHorizontalTextPosition(SwingConstants.CENTER);
			GridBagConstraints gridBagConstraints28 = new GridBagConstraints();
			gridBagConstraints28.gridx = 0;
			gridBagConstraints28.gridy = 0;
			player1Name = new JLabel();
			player1Name.setText("Player1: ");
			player1Name.setHorizontalAlignment(SwingConstants.CENTER);
			player1Name.setFont(new Font("Dialog", Font.BOLD, 14));
			player1Name.setHorizontalTextPosition(SwingConstants.CENTER);
			panelDown = new JPanel();
			panelDown.setLayout(new GridBagLayout());
			panelDown.setBorder(BorderFactory.createBevelBorder(BevelBorder.RAISED));
			panelDown.add(player1Name, gridBagConstraints28);
			panelDown.add(player1Score, gridBagConstraints29);
			panelDown.add(player2Name, gridBagConstraints30);
			panelDown.add(player2Score, gridBagConstraints31);
			panelDown.add(playerSpace, gridBagConstraints32);
		}
		return panelDown;
	}

}
