package sysmod.mancala;

import java.awt.BorderLayout;

import javax.swing.SwingConstants;
import java.awt.Point;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.JDialog;
import javax.swing.JScrollPane;

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
import javax.swing.JScrollBar;
import java.awt.Dialog;

public class MancalaGUI {

	private JFrame jFrame = null;  //  @jve:decl-index=0:visual-constraint="33,17"
	private JPanel jContentPane = null;
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
	private JDialog helpDialog = null;  //  @jve:decl-index=0:visual-constraint="333,451"
	private JPanel help = null;
	private JLabel helpTitle = null;
	private JButton newgameButton = null;
	private JLabel player1Name = null;
	private JPanel leftPanel = null;
	private JPanel rightPanelScore = null;
	private JLabel player2Space = null;
	private JLabel player2Score = null;
	private JTextArea helpText = null;
	private JScrollBar scrollbar = null;
	private JLabel player1Label = null;
	private JLabel player1Space = null;
	private JPanel leftPanelScore = null;
	private JLabel player1Score = null;
	private JLabel player2Label = null;
	private JLabel player2Space1 = null;
	private JLabel player2Score1 = null;
	private JLabel status = null;
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
			jFrame.setMinimumSize(new Dimension(800, 400));
			jFrame.setMaximumSize(new Dimension(800, 400));
			jFrame.setPreferredSize(new Dimension(800, 400));
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
			title.setForeground(new Color(0, 0, 102));
			title.setFont(new Font("Dialog", Font.BOLD, 24));
			jContentPane = new JPanel();
			jContentPane.setLayout(new BorderLayout());
			jContentPane.setBackground(new Color(204, 204, 255));
			jContentPane.add(title, BorderLayout.NORTH);
			jContentPane.add(getRightPanel(), BorderLayout.EAST);
			jContentPane.add(getLeftPanel(), BorderLayout.WEST);
			jContentPane.add(getGameboard(), BorderLayout.CENTER);
		}
		return jContentPane;
	}

	/**
	 * This method initializes Gameboard
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getGameboard() {
		if (Gameboard == null) {
			GridBagConstraints gridBagConstraints110 = new GridBagConstraints();
			gridBagConstraints110.gridx = 3;
			gridBagConstraints110.gridy = 2;
			status = new JLabel();
			status.setText("");
			status.setHorizontalAlignment(SwingConstants.CENTER);
			status.setHorizontalTextPosition(SwingConstants.CENTER);
			status.setFont(new Font("Dialog", Font.BOLD, 14));
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
			Gameboard.setBackground(Color.white);
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
			Gameboard.add(status, gridBagConstraints110);
		}
		return Gameboard;
	}

	public JLabel getTitle() {
		return title;
	}

	/**
	 * This method initializes player1store
	 * 
	 * @return javax.swing.JButton
	 */
	JButton getPlayer1Store() {
		if (player1store == null) {
			player1store = new JButton();
			player1store.setPreferredSize(new Dimension(60, 35));
			player1store.setHorizontalAlignment(SwingConstants.CENTER);
			player1store.setFont(new Font("Dialog", Font.BOLD, 14));
			player1store.setForeground(new Color(0, 0, 102));
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
			player2store.setPreferredSize(new Dimension(60, 35));
			player2store.setHorizontalAlignment(SwingConstants.CENTER);
			player2store.setFont(new Font("Dialog", Font.BOLD, 14));
			player2store.setForeground(new Color(0, 0, 102));
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
			pit12.setForeground(new Color(0, 0, 102));
			pit12.setPreferredSize(new Dimension(60, 35));
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
			pit11.setForeground(new Color(0, 0, 102));
			pit11.setPreferredSize(new Dimension(60, 35));
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
			pit1.setForeground(new Color(0, 0, 102));
			pit1.setPreferredSize(new Dimension(60, 35));
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
			pit2.setForeground(new Color(0, 0, 102));
			pit2.setPreferredSize(new Dimension(60, 35));
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
			pit3.setForeground(new Color(0, 0, 102));
			pit3.setPreferredSize(new Dimension(60, 35));
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
			pit4.setForeground(new Color(0, 0, 102));
			pit4.setPreferredSize(new Dimension(60, 35));
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
			pit5.setForeground(new Color(0, 0, 102));
			pit5.setPreferredSize(new Dimension(60, 35));
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
			pit6.setForeground(new Color(0, 0, 102));
			pit6.setPreferredSize(new Dimension(60, 35));
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
			pit7.setForeground(new Color(0, 0, 102));
			pit7.setPreferredSize(new Dimension(60, 35));
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
			pit8.setForeground(new Color(0, 0, 102));
			pit8.setPreferredSize(new Dimension(60, 35));
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
			pit9.setForeground(new Color(0, 0, 102));
			pit9.setPreferredSize(new Dimension(60, 35));
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
			pit10.setForeground(new Color(0, 0, 102));
			pit10.setPreferredSize(new Dimension(60, 35));
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
			GridBagConstraints gridBagConstraints37 = new GridBagConstraints();
			gridBagConstraints37.gridx = 0;
			gridBagConstraints37.gridy = 0;
			GridBagConstraints gridBagConstraints15 = new GridBagConstraints();
			gridBagConstraints15.gridx = 0;
			gridBagConstraints15.gridy = 3;
			GridBagConstraints gridBagConstraints14 = new GridBagConstraints();
			gridBagConstraints14.gridx = 0;
			gridBagConstraints14.gridy = 2;
			rightPanel = new JPanel();
			rightPanel.setLayout(new GridBagLayout());
			rightPanel.setSize(130, 300);
			rightPanel.setBorder(BorderFactory
					.createBevelBorder(BevelBorder.RAISED));
			rightPanel.setPreferredSize(new Dimension(140, 78));
			rightPanel.setBackground(new Color(204, 204, 255));
			rightPanel.add(getHelpButton(), gridBagConstraints14);
			rightPanel.add(getTeamButton(), gridBagConstraints15);
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
					JOptionPane.showMessageDialog(null, "Mancala Team 2010:\n - Martin Loginov \n - Hans M�esalu \n - Peeter J�rviste \n - Mari R��tli \n - Sven Aller", "Mancala Team 2010", JOptionPane.INFORMATION_MESSAGE);   
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
			JScrollPane scrollingArea = new JScrollPane(helpText);

			helpDialog.add(scrollingArea, BorderLayout.CENTER);
		}
		return helpDialog;
	}

	/**
	 * This method initializes helpText
	 * 
	 * @return javax.swing.JTextArea
	 */
	private JTextArea getHelpText() {
		if (helpText == null) {
			helpText = new JTextArea();
			helpText.setText("oiu asd�oiu �lio �iah �ioh �i u ou ouyouysgdiufygasduifoyasdf ouytasd fiasuyd iouysdt fioausdytf asudfsduh jksdfhgsdfg ipusdyfg uisdh ludy glduifyg sdliugysd liugdyh lgidjkh glsdiukfjgh sdliukgsdh ifljkgsh figlusdkyf hglidjkfy ghsdilukjgy sdhfghg liuiuh olui guklyjhg uklgkjhgfkujhfgdkjhfgdkfjv ljhv lxjhxcljvhxljvhxliuvjxchvl lijkhxc vljxhvlxikj lijkxchv lizxjkh vlzxiukjvh zxljkvhzx lvjkxh lvizxjkh vzxlijkvh zxlcjvzxh lvjzxkh cvcxjkyhg kjhm lijkg hmng jhmg kjhg kujh gkjh gb,jh g,jhg j,mg ,jmg bj,h g kuhg ukyg kujhg kuyjtg kuyjhg kjhg kjh gkujhg kjhg kujhg kjhmg kjh gkhgykh fgvhkgvkyhg gykhggkh gkjhgjhglujhgluyjgkujhgkjhgkuyjhgkjh");
			helpText.setBackground(new Color(238, 238, 238));
			helpText.setLineWrap(true);
			helpText.setWrapStyleWord(true);
		}
		return helpText;
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
					System.out.println("Start a new game"); // TODO Auto-generated Event stub mouseClicked()
					player1Label.setText(player1label.getText());
					player2Label.setText(player2label.getText());
				}
			});
		}
		return newgameButton;
	}

	/**
	 * This method initializes leftPanel
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getLeftPanel() {
		if (leftPanel == null) {
			GridBagConstraints gridBagConstraints19 = new GridBagConstraints();
			gridBagConstraints19.gridx = 0;
			gridBagConstraints19.gridy = 1;
			player1Space = new JLabel();
			player1Space.setText(": ");
			player1Label = new JLabel();
			player1Label.setText("Player1");
			GridBagConstraints gridBagConstraints16 = new GridBagConstraints();
			gridBagConstraints16.gridx = 0;
			gridBagConstraints16.gridy = 5;
			GridBagConstraints gridBagConstraints35 = new GridBagConstraints();
			gridBagConstraints35.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints35.gridy = 3;
			gridBagConstraints35.weightx = 1.0;
			gridBagConstraints35.gridx = 0;
			GridBagConstraints gridBagConstraints27 = new GridBagConstraints();
			gridBagConstraints27.fill = GridBagConstraints.VERTICAL;
			gridBagConstraints27.gridy = 1;
			gridBagConstraints27.weightx = 1.0;
			gridBagConstraints27.gridx = 0;
			leftPanel = new JPanel();
			leftPanel.setLayout(new GridBagLayout());
			leftPanel.setBorder(BorderFactory.createBevelBorder(BevelBorder.RAISED));
			leftPanel.setBackground(new Color(204, 204, 255));
			leftPanel.setPreferredSize(new Dimension(140, 78));
			leftPanel.add(getNewgameButton(), gridBagConstraints16);
			leftPanel.add(getLeftPanelScore(), gridBagConstraints19);
		}
		return leftPanel;
	}
	
	public JLabel getPlayer1label() {
		return player1label;
	}

	public void setPlayer1label(JLabel player1label) {
		this.player1label = player1label;
	}

	public JLabel getPlayer2label() {
		return player2label;
	}

	public void setPlayer2label(JLabel player2label) {
		this.player2label = player2label;
	}
	
	public JLabel getPlayer1Label() {
		return player1Label;
	}

	public void setPlayer1Label(JLabel player1Label) {
		this.player1Label = player1label;
	}

	public JLabel getPlayer2Label() {
		return player2Label;
	}

	public void setPlayer2Label(JLabel player2Label) {
		this.player2Label = player2Label;
	}

	/**
	 * This method initializes leftPanelScore	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getLeftPanelScore() {
		if (leftPanelScore == null) {
			GridBagConstraints gridBagConstraints25 = new GridBagConstraints();
			gridBagConstraints25.gridx = 2;
			gridBagConstraints25.gridy = 1;
			player2Score1 = new JLabel();
			player2Score1.setText("0");
			GridBagConstraints gridBagConstraints24 = new GridBagConstraints();
			gridBagConstraints24.gridx = 1;
			gridBagConstraints24.gridy = 1;
			player2Space1 = new JLabel();
			player2Space1.setText(": ");
			GridBagConstraints gridBagConstraints23 = new GridBagConstraints();
			gridBagConstraints23.gridx = 0;
			gridBagConstraints23.gridy = 1;
			player2Label = new JLabel();
			player2Label.setText("Player2");
			GridBagConstraints gridBagConstraints20 = new GridBagConstraints();
			gridBagConstraints20.gridx = 2;
			gridBagConstraints20.gridy = 0;
			player1Score = new JLabel();
			player1Score.setText("0");
			GridBagConstraints gridBagConstraints18 = new GridBagConstraints();
			gridBagConstraints18.gridx = 1;
			gridBagConstraints18.gridy = 0;
			GridBagConstraints gridBagConstraints17 = new GridBagConstraints();
			gridBagConstraints17.gridx = 0;
			gridBagConstraints17.gridy = 0;
			leftPanelScore = new JPanel();
			leftPanelScore.setLayout(new GridBagLayout());
			leftPanelScore.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0));
			leftPanelScore.setBackground(new Color(204, 204, 255));
			leftPanelScore.add(player1Label, gridBagConstraints17);
			leftPanelScore.add(player1Space, gridBagConstraints18);
			leftPanelScore.add(player1Score, gridBagConstraints20);
			leftPanelScore.add(player2Label, gridBagConstraints23);
			leftPanelScore.add(player2Space1, gridBagConstraints24);
			leftPanelScore.add(player2Score1, gridBagConstraints25);
		}
		return leftPanelScore;
	}

	public void disablePits(int player) {
		if (player == 0) {
			getPit1().setEnabled(false);
			getPit2().setEnabled(false);
			getPit3().setEnabled(false);
			getPit4().setEnabled(false);
			getPit5().setEnabled(false);
			getPit6().setEnabled(false);
			getPit7().setEnabled(false);
			getPit8().setEnabled(false);
			getPit9().setEnabled(false);
			getPit10().setEnabled(false);
			getPit11().setEnabled(false);
			getPit12().setEnabled(false);
		} else if (player == 1){
			
		}
	}

}
