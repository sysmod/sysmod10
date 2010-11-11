//--------------------------------------------------------------------
//     SCC (StateChart Compiler)
//          -- a compiler for an extended statechart formalism
//--------------------------------------------------------------------

/*
  Copyright (C) 2003 Thomas Huining Feng
 
 ---------------------------------------------------------------------
  Address:      MSDL, SOCS, McGill Univ., Montreal, Canada
  HomePage:     http://msdl.cs.mcgill.ca/people/tfeng/
  SCC HomePage: http://msdl.cs.mcgill.ca/people/tfeng/?research=scc
  Download:     http://savannah.nongnu.org/files/?group=svm
  CVS:          :pserver:anoncvs@subversions.gnu.org:/cvsroot/svm
                (projects "svm" and "jsvm")
  Email:        hfeng2@cs.mcgill.ca
 ---------------------------------------------------------------------
 
  This file is part of SCC.
 
 ---------------------------------------------------------------------
  SCC is free software; you can redistribute it and/or modify it under
  the terms of the GNU General Public License as published by the Free
  Software Foundation; either version 2 of the License, or (at your
  option) any later version.
 
  SCC is distributed in the hope that it will be useful, but WITHOUT
  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
  or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
  License for more details.
 
  You should have received a copy of the GNU General Public License
  along with SCC; if not, write to the Free Software Foundation, Inc.,
  59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 ---------------------------------------------------------------------
*/


import java.util.Vector;

import java.applet.*;
import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.text.*;
import javax.swing.event.*;
import javax.swing.border.*;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

class NoWrapJTextPane extends JTextPane
{
    public void setSize(Dimension d)
    {
	if (d.width < getParent().getSize().width)
	    d.width = getParent().getSize().width;
	super.setSize(d);
    }
    public boolean getScrollableTracksViewportWidth()
    {
	return false;
    }
}

class StateHierarchyRenderer extends JLabel implements ListCellRenderer
{
    Font fontB = new Font("Monospaced", Font.BOLD, 12);
    Color lightyellow = new Color(255, 255, 96);
    svmapplet applet;

    public StateHierarchyRenderer(svmapplet applet)
    {
	this.applet = applet;
    }
    
    public Component getListCellRendererComponent(JList list, Object value, int index, boolean isSelected, boolean cellHasFocus)
    {
        String s = value.toString();
        setText(s);
	if (isSelected)
	{
	    setBackground(new Color(94,121,173));
	    setBorder(BorderFactory.createRaisedBevelBorder());
	    setForeground(Color.white);
	}
	else
	{
	    String PathName = null;
	    if (list == applet.States)
		PathName = applet.getStatePath(index);
	    setBorder(BorderFactory.createLineBorder(Color.white, 1));
	    if (list == applet.Checkpoints)
	    {
		setForeground(Color.red);
		setHorizontalAlignment(SwingConstants.RIGHT);
	    }
	    else
		setForeground(new Color(1,1,139));
	    if (PathName!=null && applet.Model.isLeafState(PathName) && applet.Model.isInState(PathName))
	    {
		setBackground(lightyellow);
		setBorder(BorderFactory.createLineBorder(Color.white, 1));
	    }
	    else
	    {
		setBorder(BorderFactory.createEmptyBorder(1, 0, 1, 0));
		if (index % 2 == 0)
		    setBackground(new Color(240,240,255));
		else
		    setBackground(Color.white);
	    }
	}
	setOpaque(true);
	setFont(fontB);
	return this;
    }
}

class IntList
{
    public int i;
    public IntList Next=null;
}

public class svmapplet extends Applet implements ActionListener, MouseListener, ListSelectionListener
{
    JTextPane Dump;
    JTextField Input;
    JTextPane StateDisplay;
    JList Events;
    JList States;
    JList Checkpoints;
    Hierarchy StateHierarchy;
    Vector EnabledEvents = new Vector();
    JScrollPane spStates;
    JScrollPane spDump;
    JScrollPane spEvents;
    JScrollPane spCheckpoints;
    JButton CheckpointBtn;
    Style PromptStyle, CommandStyle;
    Class StatechartClass;
    Method CheckpointMethod;
    Method RollbackMethod;
    StateMachine Model;
    boolean DCP$Enabled = false;
    IntList CheckpointIDs = new IntList();

    static String ModelParameter = "Model";

    private void dump(String msg, Style style)
    {
	try
	{
	    Document doc = Dump.getDocument();
	    doc.insertString(doc.getLength(), msg, style);
	    Dump.setCaretPosition(doc.getLength()-msg.length());
	}
	catch (BadLocationException e)
	{
	}
    }

    public static boolean probeAttribute(Class c, String name, Object obj)
    {
	try
	{
	    Field fld = c.getField(name);
	    if (fld.getBoolean(obj))
		return true;
	}
	catch (Exception e)
	{
	}
	return false;
    }

    public void init()
    {
	try
	{
	    StatechartClass = Class.forName(getParameter(ModelParameter));
	    Model = (StateMachine) StatechartClass.newInstance();
	    DCP$Enabled = probeAttribute(StatechartClass, "DCP$Enabled", Model);
	}
	catch(Exception e)
	{
	    promptInvalidModel();
	    return;
	}

	if (DCP$Enabled)
	    try
	    {
		Class dcpClass = Class.forName("svmdcp.Controller.dcp");
		CheckpointMethod = dcpClass.getMethod("checkpoint", new Class[0]);
		RollbackMethod = dcpClass.getMethod("rollback", new Class[] { Integer.TYPE } );
	    }
	    catch (Exception e)
	    {
		DCP$Enabled = false;
	    }

	createWidgets();

	Model.initModel();

	updateEvents();
	updateHierarchy();
	States.setSelectedIndex(0);

	dump(Model.getCurrentState() + " > ", PromptStyle);
    }

    private void updateEvents()
    {
	EventList el = Model.getEnabledEvents();
	EnabledEvents.clear();
	while (el != null)
	{
	    EnabledEvents.add(el.Event);
	    el = el.Next;
	}
	Events.setListData(EnabledEvents);
    }

    private void updateHierarchy()
    {
	StateHierarchy=Model.getHierarchy();
	int index = States.getSelectedIndex();
	Vector v = new Vector();
	Hierarchy h = StateHierarchy;
	while (h != null)
	{
	    String name = "";
	    for (int i=0; i<h.Level; i++)
		name = name + "  ";
	    name=name + (Model.isLeafState(h.PathName) ? "- " : "+ ");
	    v.add(name + h.StateName);
	    h = h.Next;
	}
	States.setListData(v);
	States.setSelectedIndex(index);
    }

    private void updateCheckpoints()
    {
	Vector v = new Vector();
	IntList il = CheckpointIDs.Next;
	while (il != null)
	{
	    v.add(0, new Integer(il.i));
	    il = il.Next;
	}
	Checkpoints.setListData(v);
	Checkpoints.ensureIndexIsVisible(v.size()-1);
    }

    private void checkpoint()
    {
	IntList ID = new IntList();
	try
	{
	    ID.i = ((Integer)CheckpointMethod.invoke(null, new Object[0])).intValue();
	}
	catch (IllegalAccessException e)
	{
	}
        catch (InvocationTargetException e)
        {
        }
	ID.Next = CheckpointIDs.Next;
	CheckpointIDs.Next = ID;
	updateCheckpoints();
    }

    private void rollback(int ID)
    {
	while (CheckpointIDs.Next!=null && CheckpointIDs.Next.i>=ID)
	    CheckpointIDs.Next = CheckpointIDs.Next.Next;
	try
	{
	    RollbackMethod.invoke(null, new Object[] {new Integer(ID)} );
	}
	catch (IllegalAccessException e)
	{
	}
	catch (InvocationTargetException e)
	{
	}
	updateCheckpoints();
    }

    public void actionPerformed (ActionEvent ae)
    {
	if (ae.getSource() == Input)
	{
	    String e = Input.getText();
	    Input.setText("");
	    if (e.compareTo("Checkpoint") == 0)
		checkpoint();
	    else
	    {
		int cp = -1;
		if (e.startsWith("Rollback "))
		    try
		    {
			cp = (new Integer(e.substring(9))).intValue();
			boolean valid = false;
			IntList il = CheckpointIDs.Next;
			while (il != null)
			{
			    if (il.i == cp)
			    {
				valid = true;
				break;
			    }
			    il = il.Next;
			}
			if (!valid)
			    cp = -1;
		    }
		    catch (Exception f)
		    {
		    }
		if (cp >= 0)
		    rollback(cp);
		else
		    Model.handleEvent(e);
		updateEvents();
		updateHierarchy();
	    }
	    dump(e+"\n", CommandStyle);
	    dump(Model.getCurrentState()+" > ", PromptStyle);
	}
	else if (CheckpointBtn!=null && ae.getSource()==CheckpointBtn)
	{
	    checkpoint();
	    dump("Checkpoint\n", CommandStyle);
	    dump(Model.getCurrentState()+" > ", PromptStyle);
	}
    }
    
    public void mousePressed(MouseEvent e) {}
    
    public void mouseReleased(MouseEvent e) {}
    
    public void mouseEntered(MouseEvent e) {}
    
    public void mouseExited(MouseEvent e) {}
    
    public void mouseClicked(MouseEvent e)
    {
	if (e.getClickCount() == 2 && e.getSource() == Events)
	{
	    int idx = Events.getSelectedIndex();
	    if (idx < 0)
		return;
	    String ev = (String)Events.getModel().getElementAt(idx);
	    Model.handleEvent(ev);
	    dump(ev+"\n", CommandStyle);
	    dump(Model.getCurrentState()+" > ", PromptStyle);
	    updateEvents();
	    updateHierarchy();
	}
	else if (e.getClickCount() == 2 && e.getSource() == Checkpoints)
	{
	    int idx = Checkpoints.getSelectedIndex();
	    if (idx < 0)
		return;
	    int cp = ((Integer)Checkpoints.getModel().getElementAt(idx)).intValue();
	    rollback(cp);
	    updateEvents();
            updateHierarchy();
	    dump("Rollback " + cp + "\n", CommandStyle);
	    dump(Model.getCurrentState()+" > ", PromptStyle);
	}
    }

    public String getStatePath(int index)
    {
	Hierarchy h = StateHierarchy;
	for (int i=0; i<index; i++)
	    h = h.Next;
	return h.PathName;
    }

    public void valueChanged(ListSelectionEvent e)
    {
	if (e.getSource() == States)
	{
	    int idx = States.getSelectedIndex();
	    if (idx >= 0)
		StateDisplay.setText(getStatePath(idx));
	}
    }

    private void createWidgets()
    {
	setLayout(new BorderLayout());

	JLabel scclb = new JLabel("SCC Demonstration -- a Preview to Version 0.1", JLabel.CENTER);
	scclb.setForeground(Color.red);
	scclb.setBackground(Color.white);
	scclb.setOpaque(true);
	scclb.setPreferredSize(new Dimension(10, 25));
	
	Dump = new NoWrapJTextPane();
	Dump.setEditable(false);
	Input = new JTextField();
	Events = new JList();
	Events.setPreferredSize(new Dimension(80, 10));
	Events.setCellRenderer(new StateHierarchyRenderer(this));
	States = new JList();
	States.setCellRenderer(new StateHierarchyRenderer(this));
	StateDisplay = new JTextPane();
	StateDisplay.setEditable(false);

	Dump.setBackground(Color.white);
	Input.setBackground(Color.white);
	Events.setBackground(Color.white);
	States.setBackground(Color.white);

	Font fontB = new Font("Monospaced", Font.BOLD, 12);
	Font font = new Font("Monospaced", 0, 12);
	Font fonts = new Font("Monospaced", 0, 12);
	Font fontl = new Font("Serif", Font.BOLD, 15);
	Dump.setFont(fonts);
	Input.setFont(font);
	Events.setFont(fontB);
	States.setFont(fontB);
	StateDisplay.setFont(font);
	scclb.setFont(fontl);

	PromptStyle = Dump.addStyle("prompt", null);
	StyleConstants.setForeground(PromptStyle, Color.blue);
	CommandStyle = Dump.addStyle("command", null);
	StyleConstants.setForeground(CommandStyle, Color.red);
	StyleConstants.setBold(CommandStyle, true);

	spDump = new JScrollPane(Dump);
	spEvents = new JScrollPane(Events);
	spStates = new JScrollPane(States);
	spEvents.setBorder(BorderFactory.createEmptyBorder());

	JLabel eventslb = new JLabel("Events", JLabel.CENTER);
	JLabel dumplb = new JLabel("Output", JLabel.CENTER);
	JLabel inputlb = new JLabel("Command", JLabel.CENTER);
	JLabel stateslb = new JLabel("State Hierarchy", JLabel.CENTER);
	
	Color lightblue = new Color(172,215,229);
	Color pink = new Color(0xFFC0C0);
	eventslb.setBackground(lightblue);
	eventslb.setForeground(Color.blue);
	eventslb.setOpaque(true);
	dumplb.setBackground(lightblue);
	dumplb.setForeground(Color.blue);
	dumplb.setOpaque(true);
	stateslb.setBackground(lightblue);
	stateslb.setForeground(Color.blue);
	stateslb.setOpaque(true);
	inputlb.setBackground(pink);
	inputlb.setForeground(Color.blue);
	inputlb.setOpaque(true);
	StateDisplay.setBackground(lightblue);

	JPanel pl = new JPanel(),
	       pr = new JPanel(),
	      prb = new JPanel(),
	      pll = new JPanel(),
	      prr = new JPanel(),
	      prl = new JPanel();
	pl.setLayout(new BorderLayout());
	pr.setLayout(new BorderLayout());
	prb.setLayout(new BorderLayout());
	pll.setLayout(new BorderLayout());
	prr.setLayout(new BorderLayout());
	prl.setLayout(new BorderLayout());

	prb.add(inputlb, "North");
	prb.add(Input, "Center");
	pl.add(eventslb, "North");
	pl.add(spEvents, "Center");
	prl.add(dumplb, "North");
	prl.add(spDump, "Center");
	prl.add(prb, "South");
	pr.add(prl, "Center");
	pll.add(stateslb, "North");
	pll.add(spStates, "Center");
	pll.add(StateDisplay, "South");
	pll.setPreferredSize(new Dimension(165, 10));
	pll.setBorder(BorderFactory.createEtchedBorder());

	if (DCP$Enabled)
	{
	    Font cpfont = new Font("SansSerif", Font.PLAIN, 9);
	    JPanel prrr = new JPanel();
	    CheckpointBtn = new JButton("check");
	    Insets insets = new Insets(3, 3, 3, 3);
	    CheckpointBtn.setMargin(insets);
	    CheckpointBtn.setPreferredSize(new Dimension(40, 18));
	    CheckpointBtn.setFont(cpfont);
	    CheckpointBtn.addActionListener(this);
	    prrr.setLayout(new BorderLayout());
	    Checkpoints = new JList();
	    Checkpoints.setCellRenderer(new StateHierarchyRenderer(this));
	    Checkpoints.addMouseListener(this);
	    spCheckpoints = new JScrollPane(Checkpoints);
	    spCheckpoints.setBorder(BorderFactory.createEtchedBorder());
	    spCheckpoints.setPreferredSize(new Dimension(40, 20));
	    prrr.add(spCheckpoints, "Center");
	    prrr.add(CheckpointBtn, "South");
	    pr.add(prrr, "East");
	}

	JSplitPane sp = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, pl, pr);
	sp.setDividerSize(4);
	sp.setBorder(BorderFactory.createEtchedBorder());

	JTextPane authorlb = new JTextPane();
	StyledDocument doc = authorlb.getStyledDocument();
	MutableAttributeSet standard = new SimpleAttributeSet();
	StyleConstants.setAlignment(standard, StyleConstants.ALIGN_RIGHT);
	StyleConstants.setItalic(standard, true);
	StyleConstants.setForeground(standard, Color.gray);
	StyleConstants.setFontFamily(standard, "Serif");
	doc.setParagraphAttributes(0, 0, standard, true);
	authorlb.setText("Thomas Huining Feng, MSDL, McGill, Nov. 2003");
	authorlb.setEditable(false);
	authorlb.setBackground(Color.white);
	authorlb.setForeground(Color.red);
	authorlb.setOpaque(true);
	authorlb.setBorder(BorderFactory.createEmptyBorder(4, 0, 4, 0));

	prr.add(sp, "Center");
	prr.add(authorlb, "South");

	JSplitPane sp2 = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, pll, prr);
	sp2.setOneTouchExpandable(true);
	sp2.setBorder(BorderFactory.createEmptyBorder());

	add(scclb, "North");
	add(sp2, "Center");

	Events.addMouseListener(this);
	Input.addActionListener(this);
	States.addListSelectionListener(this);

	setSize(new Dimension(600, 210));

	Input.requestFocus();
    }

    private void promptInvalidModel()
    {
	setLayout(new BorderLayout());

	JLabel scclb = new JLabel("SCC Demonstration -- a Preview to Version 0.1, Thomas", JLabel.CENTER);
	scclb.setForeground(Color.red);
	scclb.setBackground(Color.white);
	scclb.setOpaque(true);

	JLabel invalidlb = new JLabel("ERROR: Model \""+getParameter(ModelParameter)+"\" could not be loaded.", JLabel.CENTER);
	invalidlb.setForeground(Color.blue);
	invalidlb.setBackground(Color.white);
	invalidlb.setOpaque(true);
	invalidlb.setBorder(BorderFactory.createEtchedBorder());

	Font fontlB = new Font("SansSerif", Font.BOLD, 16);
	Font fontl = new Font("SansSerif", Font.BOLD, 14);
	scclb.setFont(fontl);
	invalidlb.setFont(fontlB);

	add(scclb, "North");
	add(invalidlb, "Center");
    }
}
