
import os
import tkinter as tk
from tkinter import filedialog as fd
import mri_quickgifs as mquick

class tsvtofsl_gui():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('TSV to FSL')

        #Create frame for first row of gui
        self.frame_base_one = tk.Frame()

        #Create frame for file loading
        self.frame_tsvload = tk.Frame(self.frame_base_one)
        self.input_file_lbl = tk.Label(self.frame_tsvload, text='Load TSV:')
        self.inputfile_var = tk.StringVar(self.window)
        self.input_file_entry = tk.Entry(self.frame_tsvload, textvariable=self.inputfile_var)
        self.input_file_btn = tk.Button(self.frame_tsvload, text='Select', command=self.gui_open_input)
        #Pack the things into the frame
        self.input_file_lbl.grid(row=0, column=0, sticky='w')
        self.input_file_entry.grid(row=0, column=1, sticky='w')
        self.input_file_btn.grid(row=0, column=2, sticky='w')

        #Create frame for output directory specification
        self.frame_outdirset = tk.Frame(self.frame_base_one)
        self.out_dir_lbl = tk.Label(self.frame_outdirset, text='Load TSV:')
        self.outdir_var = tk.StringVar(self.window)
        self.out_dir_entry = tk.Entry(self.frame_outdirset, textvariable=self.outdir_var)
        self.out_dir_btn = tk.Button(self.frame_outdirset, text='Select', command=self.gui_select_outdir)
        #Pack the things into the frame
        self.out_dir_lbl.grid(row=0, column=0, sticky='e')
        self.out_dir_entry.grid(row=0, column=1, sticky='e')
        self.out_dir_btn.grid(row=0, column=2, sticky='e')

        #Pack the frames into the gui row frame
        self.frame_tsvload.grid(row=0, column=0, sticky='w')
        self.frame_outdirset.grid(row=0, column=1, sticky='e')

        #Create frame for second row of gui
        self.frame_base_two = tk.Frame()

        #Create frame for trial_type list
        self.frame_trialtype = tk.Frame(self.frame_base_two)
        self.trial_type_lbl = tk.Label(self.frame_trialtype, text='trial_type')
        self.trial_types=[]
        self.trial_types_var=tk.StringVar(value=self.trial_types)
        self.trial_types_lbox=tk.Listbox(self.frame_trialtype, listvariable=self.trial_types_var, height=8, selectmode='extended')
        #Pack the items into the frame
        self.trial_type_lbl.grid(row=0, column=0, sticky='n')
        self.trial_types_lbox.grid(row=1, column=0, sticky='n')

        #Create frame for stim_info list
        self.frame_stiminfo = tk.Frame(self.frame_base_two)
        self.stim_info_lbl = tk.Label(self.frame_stiminfo, text='stim_info')
        self.stim_info=[]
        self.stim_info_var=tk.StringVar(self.window, value=self.stim_info)
        self.stim_info_lbox=tk.Listbox(self.frame_stiminfo, listvariable=self.stim_info_var, height=8, selectmode='extended')
        #Pack the items into the frame
        self.stim_info_lbl.grid(row=0, column=0, sticky='n')
        self.stim_info_lbox.grid(row=1, column=0, sticky='n')

        #Create frame for condition setting
        self.frame_condset = tk.Frame(self.frame_base_two)
        self.cond_set_lbl = tk.Label(self.frame_condset, text='Condition Label')
        self.condset_var = tk.StringVar(self.window)
        self.cond_set_entry = tk.Entry(self.frame_condset,textvariable=self.condset_var)
        self.cond_set_btn = tk.Button(self.frame_condset, text='Set Condition', command=self.gui_set_cond)
        #Pack the things into the frame
        self.cond_set_lbl.grid(row=0,column=0,sticky='n')
        self.cond_set_entry.grid(row=1,column=0,sticky='n')
        self.cond_set_btn.grid(row=2,column=0,sticky='n')

        #Create frame for condition list
        self.frame_condlist = tk.Frame(self.frame_base_two)
        self.cond_list_lbl = tk.Label(self.frame_condlist, text='Condition List')
        self.cond_list=[]
        self.cond_list_var = tk.StringVar(self.window, value=self.cond_list)
        self.cond_list_lbox=tk.Listbox(self.frame_condlist, listvariable=self.cond_list_var, height=8, selectmode='extended')
        self.rem_cond_btn=tk.Button(self.frame_condlist, text='Remove\nCondition', command=self.gui_remove_cond)
        #Pack the things into the frame
        self.cond_list_lbl.grid(row=0,column=0,sticky='n')
        self.cond_list_lbox.grid(row=1,column=0,sticky='n')
        self.rem_cond_btn.grid(row=2,column=0,sticky='n')

        #Pack frames into second gui row frame
        self.frame_trialtype.grid(row=0,column=0,sticky='w')
        self.frame_stiminfo.grid(row=0,column=1,sticky='w')
        self.frame_condset.grid(row=0,column=2,sticky='w')
        self.frame_condlist.grid(row=0,column=3,sticky='w')

        #Create frame for third gui row
        self.frame_base_three=tk.Frame()

        #Create frame for write button
        self.frame_writebtn = tk.Frame(self.frame_base_three)
        self.write_out_btn=tk.Button(self.frame_writebtn, text='Write Files', command=self.gui_write_files)
        #Pack the button into the frame
        self.write_out_btn.grid(row=0,column=0,sticky='n')

        #Pack things into the third frame row
        self.frame_writebtn.grid(row=0,column=0,sticky='w')

        #Put all the frames into the GUI window
        self.frame_base_one.pack(fill=tk.X, expand=True)
        self.frame_base_two.pack(fill=tk.X, expand=True)
        self.frame_base_three.pack(fill=tk.X, expand=True)


    def run_loop(self):
        self.window.mainloop()

    def gui_open_input(self):
    	print('hello')

    def gui_write_files(self):
    	print('hello')

    def gui_set_cond(self):
    	print('hello')

    def gui_remove_cond(self):
    	print('hello')

    def gui_select_outdir(self):
    	print('hello')


if __name__ == '__main__':
    obj = tsvtofsl_gui()
    obj.run_loop()