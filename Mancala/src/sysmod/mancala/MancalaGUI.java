package sysmod.mancala;

import java.awt.event.KeyEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Event;
import java.awt.BorderLayout;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.KeyStroke;
import java.awt.Point;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JMenuItem;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JFrame;
import javax.swing.JDialog;
import java.awt.Dimension;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Font;
import java.awt.Rectangle;
import java.awt.SystemColor;
import java.awt.Color;

public class MancalaGUI {

	private JFrame jFrame = null;
	private JPanel jContentPane = null;
	private JMenuBar jJMenuBar = null;
	private JMenu helpMenu = null;
	private JMenuItem aboutMenuItem = null;
	private JDialog aboutDialog = null;  //  @jve:decl-index=0:visual-constraint="66,453"
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
	private JLabel player1store = null;
	private JLabel player2store = null;
	private JLabel title = null;
	/**
	 * This method initializes jFrame
	 * 
	 * @return javax.swing.JFrame
	 */
	private JFrame getJFrame() {
		if (jFrame == null) {
			jFrame = new JFrame();
			jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			jFrame.setJMenuBar(getJJMenuBar());
			jFrame.setSize(800, 300);
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
			title.setFont(new Font("Dialog", Font.BOLD, 18));
			jContentPane = new JPanel();
			jContentPane.setLayout(new BorderLayout());
			jContentPane.add(getGameboard(), BorderLayout.CENTER);
			jContentPane.add(title, BorderLayout.NORTH);
		}
		return jContentPane;
	}

	/**
	 * This method initializes jJMenuBar	
	 * 	
	 * @return javax.swing.JMenuBar	
	 */
	private JMenuBar getJJMenuBar() {
		if (jJMenuBar == null) {
			jJMenuBar = new JMenuBar();
			jJMenuBar.add(getHelpMenu());
		}
		return jJMenuBar;
	}

	/**
	 * This method initializes jMenu	
	 * 	
	 * @return javax.swing.JMenu	
	 */
	private JMenu getHelpMenu() {
		if (helpMenu == null) {
			helpMenu = new JMenu();
			helpMenu.setText("Help");
			helpMenu.add(getAboutMenuItem());
		}
		return helpMenu;
	}

	/**
	 * This method initializes jMenuItem	
	 * 	
	 * @return javax.swing.JMenuItem	
	 */
	private JMenuItem getAboutMenuItem() {
		if (aboutMenuItem == null) {
			aboutMenuItem = new JMenuItem();
			aboutMenuItem.setText("About");
			aboutMenuItem.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					JDialog aboutDialog = getAboutDialog();
					aboutDialog.pack();
					Point loc = getJFrame().getLocation();
					loc.translate(20, 20);
					aboutDialog.setLocation(loc);
					aboutDialog.setVisible(true);
				}
			});
		}
		return aboutMenuItem;
	}

	/**
	 * This method initializes aboutDialog	
	 * 	
	 * @return javax.swing.JDialog
	 */
	private JDialog getAboutDialog() {
		if (aboutDialog == null) {
			aboutDialog = new JDialog(getJFrame(), true);
			aboutDialog.setTitle("About Mancala");
			aboutDialog.setFont(new Font("Dialog", Font.PLAIN, 14));
			aboutDialog.setMinimumSize(new Dimension(300, 200));
			aboutDialog.setMaximumSize(new Dimension(300, 200));
			aboutDialog.setBounds(new Rectangle(0, 0, 300, 200));
			aboutDialog.setContentPane(getAboutContentPane());
		}
		return aboutDialog;
	}

	/**
	 * This method initializes aboutContentPane
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getAboutContentPane() {
		if (aboutContentPane == null) {
			aboutTitle = new JLabel();
			aboutTitle.setText("About Mancala");
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
			aboutText.setBackground(Color.white);
			aboutText.setText("Team: \n- Martin Loginov \n- Hans Mäesalu \n- Peeter Jürviste \n- Mari Rüütli \n- Sven Aller");
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
			GridBagConstraints gridBagConstraints12 = new GridBagConstraints();
			gridBagConstraints12.gridx = 0;
			gridBagConstraints12.gridy = 2;
			player2store = new JLabel();
			player2store.setText("0");
			player2store.setPreferredSize(new Dimension(60, 26));
			player2store.setHorizontalAlignment(SwingConstants.CENTER);
			player2store.setFont(new Font("Dialog", Font.BOLD, 14));
			GridBagConstraints gridBagConstraints10 = new GridBagConstraints();
			gridBagConstraints10.gridx = 8;
			gridBagConstraints10.gridy = 2;
			player1store = new JLabel();
			player1store.setText("0");
			player1store.setPreferredSize(new Dimension(60, 26));
			player1store.setHorizontalAlignment(SwingConstants.CENTER);
			player1store.setFont(new Font("Dialog", Font.BOLD, 14));
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
			Gameboard.add(player1store, gridBagConstraints10);
			Gameboard.add(player2store, gridBagConstraints12);
		}
		return Gameboard;
	}

	/**
	 * This method initializes pit12	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit12() {
		if (pit12 == null) {
			pit12 = new JButton();
			pit12.setText("3");
			pit12.setFont(new Font("Dialog", Font.BOLD, 14));
			pit12.setPreferredSize(new Dimension(60, 26));
			pit12.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit12;
	}

	/**
	 * This method initializes pit11	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit11() {
		if (pit11 == null) {
			pit11 = new JButton();
			pit11.setText("3");
			pit11.setFont(new Font("Dialog", Font.BOLD, 14));
			pit11.setPreferredSize(new Dimension(60, 26));
			pit11.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit11;
	}

	/**
	 * This method initializes pit1	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit1() {
		if (pit1 == null) {
			pit1 = new JButton();
			pit1.setText("3");
			pit1.setFont(new Font("Dialog", Font.BOLD, 14));
			pit1.setPreferredSize(new Dimension(60, 26));
			pit1.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit1;
	}

	/**
	 * This method initializes pit10	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit10() {
		if (pit10 == null) {
			pit10 = new JButton();
			pit10.setText("3");
			pit10.setFont(new Font("Dialog", Font.BOLD, 14));
			pit10.setPreferredSize(new Dimension(60, 26));
			pit10.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit10;
	}

	/**
	 * This method initializes pit9	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit9() {
		if (pit9 == null) {
			pit9 = new JButton();
			pit9.setText("3");
			pit9.setFont(new Font("Dialog", Font.BOLD, 14));
			pit9.setPreferredSize(new Dimension(60, 26));
			pit9.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit9;
	}

	/**
	 * This method initializes pit8	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit8() {
		if (pit8 == null) {
			pit8 = new JButton();
			pit8.setText("3");
			pit8.setFont(new Font("Dialog", Font.BOLD, 14));
			pit8.setPreferredSize(new Dimension(60, 26));
			pit8.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit8;
	}

	/**
	 * This method initializes pit7	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit7() {
		if (pit7 == null) {
			pit7 = new JButton();
			pit7.setText("3");
			pit7.setFont(new Font("Dialog", Font.BOLD, 14));
			pit7.setPreferredSize(new Dimension(60, 26));
			pit7.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit7;
	}

	/**
	 * This method initializes pit2	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit2() {
		if (pit2 == null) {
			pit2 = new JButton();
			pit2.setText("3");
			pit2.setFont(new Font("Dialog", Font.BOLD, 14));
			pit2.setPreferredSize(new Dimension(60, 26));
			pit2.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit2;
	}

	/**
	 * This method initializes pit3	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit3() {
		if (pit3 == null) {
			pit3 = new JButton();
			pit3.setText("3");
			pit3.setFont(new Font("Dialog", Font.BOLD, 14));
			pit3.setPreferredSize(new Dimension(60, 26));
			pit3.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit3;
	}

	/**
	 * This method initializes pit4	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit4() {
		if (pit4 == null) {
			pit4 = new JButton();
			pit4.setText("3");
			pit4.setFont(new Font("Dialog", Font.BOLD, 14));
			pit4.setPreferredSize(new Dimension(60, 26));
			pit4.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit4;
	}

	/**
	 * This method initializes pit5	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit5() {
		if (pit5 == null) {
			pit5 = new JButton();
			pit5.setText("3");
			pit5.setFont(new Font("Dialog", Font.BOLD, 14));
			pit5.setPreferredSize(new Dimension(60, 26));
			pit5.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit5;
	}

	/**
	 * This method initializes pit6	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getPit6() {
		if (pit6 == null) {
			pit6 = new JButton();
			pit6.setText("3");
			pit6.setFont(new Font("Dialog", Font.BOLD, 14));
			pit6.setPreferredSize(new Dimension(60, 26));
			pit6.addMouseListener(new java.awt.event.MouseAdapter() {
				public void mouseClicked(java.awt.event.MouseEvent e) {
					System.out.println("mouseClicked()"); // TODO Auto-generated Event stub mouseClicked()
				}
			});
		}
		return pit6;
	}

	/**
	 * Launches this application
	 */
	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				MancalaGUI application = new MancalaGUI();
				application.getJFrame().setVisible(true);
			}
		});
	}

}
