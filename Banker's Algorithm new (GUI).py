import tkinter as tk


def find_safe_sequence():
    proc_no = int(proc_entry.get())
    res_no = int(res_entry.get())
    allocation = []
    for i in range(proc_no):
        row = list(map(int, alloc_entries[i].get().split()))
        allocation.append(row)
    # Get for max matrix
    max = []
    for i in range(proc_no):
        row = list(map(int, max_entries[i].get().split()))
        max.append(row)
    Available = list(map(int, avail_entry.get().split()))
    f = [0]*proc_no
    ans = [0]*proc_no
    ind = 0
    for k in range(proc_no):
        f[k] = 0
    need = [[ 0 for i in range(res_no)]for i in range(proc_no)]
    for i in range(proc_no):
        for j in range(res_no):
            need[i][j] = max[i][j] - allocation[i][j]
    y = 0
    for k in range(5):
        for i in range(proc_no):
            if (f[i] == 0):
                flag = 0
                for j in range(res_no):
                    if (need[i][j] > Available[j]):
                        flag = 1
                        break
                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(res_no):
                        Available[y] += allocation[i][y]
                    f[i] = 1
    if ind != proc_no:
        result_label.config(text="No safe sequence.")
    else:
        sequence = "The Safe Sequence is: "
        
        empty_label = tk.Label(window,text="")
        empty_label.pack()

        for i in range(proc_no - 1):
            sequence += f"P{ans[i]} -> "
        sequence += f"P{ans[proc_no - 1]}"
        result_label.config(text=sequence)

window = tk.Tk()
window.title("Deadlocks Prevention By Nada Sameh")
window.geometry("400x600")
#window.configure(bg='#add8e6')

empty_label = tk.Label(window,text="")
empty_label.pack()

proc_label = tk.Label(window, text="The number of processes: ")
proc_label.pack()
proc_label.configure(font=('Arial', 12, 'bold'), fg='dark blue')
proc_entry = tk.Entry(window)
proc_entry.pack()

empty_label = tk.Label(window,text="")
empty_label.pack()


res_label = tk.Label(window, text="The number of resources: ")
res_label.pack()
res_label.configure(font=('Arial', 12, 'bold'), fg='dark blue')
res_entry = tk.Entry(window)
res_entry.pack()

empty_label = tk.Label(window,text="")
empty_label.pack()


alloc_label = tk.Label(window, text="Allocation matrix: ")
alloc_label.pack()
alloc_label.configure(font=('Arial', 12, 'bold'), fg='dark blue')
alloc_entries = []
for i in range(5):
    row = tk.Entry(window)
    row.pack()
    alloc_entries.append(row)

empty_label = tk.Label(window,text="")
empty_label.pack()

max_label = tk.Label(window, text="Maximum demand matrix: ")
max_label.pack()
max_label.configure(font=('Arial', 12, 'bold'), fg='dark blue')
max_entries = []
for i in range(5):
    row = tk.Entry(window)
    row.pack()
    max_entries.append(row)

empty_label = tk.Label(window,text="")
empty_label.pack()

avail_label = tk.Label(window, text="Available resources: ")
avail_label.pack()
avail_label.configure(font=('Arial', 12, 'bold'), fg='dark blue')
avail_entry = tk.Entry(window)
avail_entry.pack()

empty_label = tk.Label(window,text="")
empty_label.pack()

button = tk.Button(window, text="Find Safe Sequence", command=find_safe_sequence, font=('Arial', 16), fg='dark orange')
button.pack()

empty_label = tk.Label(window,text="")
empty_label.pack()

result_label = tk.Label(window)
result_label.pack()
result_label.configure(font=('Arial', 12, 'bold'), fg='dark green')

window.mainloop()
