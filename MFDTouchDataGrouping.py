import tkinter
from tkinter import END, filedialog

mainWindow = tkinter.Tk()

results = tkinter.Text(mainWindow, height=18, width=40, state='normal')
results.grid(row=1, column=1, sticky='nswe', rowspan=1)
results.config(border=2, relief='sunken')

file = filedialog.askopenfilename(title="Search", filetypes=(("text files", "*.txt"), ("all files", "*.*")))

distance = []
time = []
trigger_distance = []
trigger_time = []
results_list = []
peak_g = []
average_g = []
Speed_max = []
average_decel = []
peak_decel = []
speed_at_trigger = []
corrected_distance = []
ams_distance = []
mfdd = []
centre_line = []

with open(file, 'r') as f:
    lines = f.readlines()

for line in lines:
    if "Time" in line:
        # if ":" in line[6:]:
        #     pass
        if "Clock" in line:
            pass
        elif "Trigger" in line:
            trigger_time.append(line[24:].strip("\n")) 
        elif "Acceleration" in line:
            time.append(line[29:].strip("\n"))
        elif "(s)" in line:
            time.append(line[24:].strip("\n"))
        else:
            pass
    elif "Distance" in line:
        if "AMS" in line:
            ams_distance.append(line[19:].strip("\n"))
        elif "Acceleration" in line:
            distance.append(line[33:].strip("\n"))
        elif "Trigger" in line:
            trigger_distance.append(line[28:].strip("\n"))
        elif "Corrected" in line:
            corrected_distance.append(line[25:].strip("\n"))
        else:
            distance.append(line[28:].strip("\n"))
    elif "Maximum Speed" in line:
        Speed_max.append(line[23:].strip("\n"))
    elif "Peak Acceleration" in line:
        peak_g.append(line[24:].strip("\n"))
    elif "Peak Deceleration" in line:
        peak_decel.append(line[24:].strip("\n"))
    elif "Average Deceleration" in line:
        average_decel.append(line[27:].strip("\n"))
    elif "Average Acceleration" in line:
        average_g.append(line[27:].strip("\n"))
    elif "Speed at Trigger" in line:
        speed_at_trigger.append(line[26:].strip("\n"))
    elif "MFDD" in line:
        if "Percentage" in line:
            pass
        elif "Speed" in line:
            pass
        else:
            mfdd.append(line[11:].strip("\n"))
    elif "Centre Line Deviation" in line:
        centre_line.append(line[28:].strip("\n"))

results = tkinter.Text(mainWindow, height=18, width=40, state='normal')
results.grid(row=1, column=1, sticky='nswe', rowspan=1)
results.config(border=2, relief='sunken')

results_list.append("You may need to press off of the window")
results_list.append("to be able to copy and paste")

results_list.append("\nTime")
if not time:
    results_list.append("None")
else:
    for j in time:
        results_list.append(j)
        
results_list.append("\nDistance")
if not distance:
    results_list.append("None")
else:
    for i in distance:
        results_list.append(i)

results_list.append("\nSpeed Max (km/h)")
if not Speed_max:
    results_list.append("None")
else:
    for d in Speed_max:
        results_list.append(d)

results_list.append("\nAverage G")
if not average_g:
    results_list.append("None")
else:
    for b in average_g:
        results_list.append(b)

results_list.append("\nPeak G")
if not peak_g:
    results_list.append("None")
else:
    for a in peak_g:
        results_list.append(a)

results_list.append("\nTrigger time")
if not trigger_time:
    results_list.append("None")
else:
    for l in trigger_time:
        results_list.append(l)

results_list.append("\nTrigger Distance")
if not trigger_distance:
    results_list.append("None")
else:
    for k in trigger_distance:
        results_list.append(k)

results_list.append("\nPeak Deceleration")
if not peak_decel:
    results_list.append("None")
else:
    for y in peak_decel:
        results_list.append(y)

results_list.append("\nAverage Deceleration")
if not average_decel:
    results_list.append("None")
else:
    for z in average_decel:
        results_list.append(z)

results_list.append("\nSpeed at Trigger")
if not speed_at_trigger:
    results_list.append("None")
else:
    for x in speed_at_trigger:
        results_list.append(x)

results_list.append("\nCorrected Distance")
if not corrected_distance:
    results_list.append("None")
else:
    for w in corrected_distance:
        results_list.append(w)

results_list.append("\nAMS Distance")
if not ams_distance:
    results_list.append("None")
else:
    for v in ams_distance:
        results_list.append(v)

results_list.append("\nMFDD")
if not mfdd:
    results_list.append("None")
else:
    for s in mfdd:
        results_list.append(s)

results_list.append("\nCentre line deviation")
if not centre_line:
    results_list.append("None")
else:
    for p in centre_line:
        results_list.append(p)

for m in results_list:
    results.insert(END, m + '\n')

mainWindow.mainloop()