# num = [6, 5, 4, 8, 2]                                 bb sort
# for i in range(len(num)):
#     for j in range(0, len(num) - i - 1):
#         if num[j] > num[j + 1]:
#             num[j], num[j + 1] = num[j + 1], num[j]
#     print(num)
# ------------------------------------------------------------------------------

# array = [6, 5, 4, 8, 2]                                 is sort

# for i in range(1, len(array)):
#     k = array[i]
#     j = i - 1       
#     while j >= 0 and k < array[j]:
#         array[j + 1] = array[j]
#         j = j - 1
#         array[j + 1] = k
#         print(array)   
    
# ---------------------------------------------------------------------------------     

# array = [6, 5, 4, 8, 2]                               slt sort 

# for i in range(len(array) - 1):
#     min = i
#     for j in range(i + 1, len(array)):
#         if array[j] < array[min]:
#             min = j
#     array[i], array[min] = array[min], array[i] 

#     print(array)
from tkinter import *

def menuExit():
    Searching.destroy()

def add_number():
    input_text = entry1.get()
    if input_text.strip():
        number = int(input_text)
        data.append(number)
        entry1.delete(0, END)  # Clear the input field
        update_displayed_numbers()  # Update the displayed numbers

def clear_data():
    global data
    data = []
    update_displayed_numbers()  # Clear the displayed numbers
    entry3.delete(0, END)  # Clear the result Entry
    entry2.delete(0, END)  # Clear the search Entry

def update_displayed_numbers():
    displayed_numbers.config(text="Numbers: " + ", ".join(map(str, data)))

def sequential_search():
    target = int(entry2.get())
    found = False
    for i in range(len(data)):
        if data[i] == target:
            entry3.delete(0, END)  # Clear the result Entry
            entry3.insert(0, f"พบ {target} ที่ตำแหน่ง {i}")
            found = True
            break
    if not found:
        entry3.delete(0, END)  # Clear the result Entry
        entry3.insert(0, f"{target} ไม่พบในรายการ")

def binary_search():
    target = int(entry2.get())
    found = False
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            entry3.delete(0, END)  # Clear the result Entry
            entry3.insert(0, f"ค้นพบค่า {target} ที่ตำแหน่ง {mid}")
            found = True
            break
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if not found:
        entry3.delete(0, END)  # Clear the result Entry
        entry3.insert(0, f"ไม่พบค่า {target} ในฐานข้อมูล")

def clear_button_clicked():
    entry2.delete(0, END)  # Clear the search Entry
    entry3.delete(0, END)  # Clear the result Entry
    clear_data()

data = []  # รายการข้อมูลที่ใช้ในการค้นหา

Searching = Tk()
Searching.title("Searching")
Searching.geometry("925x530+250+100")

# สร้างพื้นหลัง
bg = PhotoImage(file="c:/012/.vscode/Project/M.png")
label = Label(Searching, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)

# สร้างวัตถุต่างๆ
entry1 = Entry(Searching, font=("Helvetica", 18))
entry1.place(x=250, y=100)

entry2 = Entry(Searching, font=("Helvetica", 18))
entry2.place(x=250, y=160)

entry3 = Entry(Searching, font=("Helvetica", 18))
entry3.place(x=250, y=220)

add_button = Button(Searching, text="เพิ่มตัวเลข", font=14, command=add_number)
add_button.place(x=550, y=100)

displayed_numbers = Label(Searching, font=("Helvetica", 14))
displayed_numbers.place(x=250, y=260)

buttonSeq = Button(Searching, text="Sequential Search", font=("Minecraft", 14), command=sequential_search, fg="white", bg="#93908F")
buttonSeq.place(relx=0.39, rely=0.8, anchor="n")
buttonSeq.bind("<Enter>", lambda event, btn=buttonSeq: btn.config(bg="gray"))
buttonSeq.bind("<Leave>", lambda event, btn=buttonSeq: btn.config(bg="#93908F"))

buttonBin = Button(Searching, text="Binary Search", font=("Minecraft", 14), command=binary_search, fg="white", bg="#93908F")
buttonBin.place(relx=0.65, rely=0.8, anchor="n")
buttonBin.bind("<Enter>", lambda event, btn=buttonBin: btn.config(bg="gray"))
buttonBin.bind("<Leave>", lambda event, btn=buttonBin: btn.config(bg="#93908F"))

buttonDelSe = Button(Searching, text="Reset Data", font=("Minecraft", 14), fg="white", bg="#93908F", command=clear_button_clicked)
buttonDelSe.place(relx=0.355, rely=0.9, anchor="n")
buttonDelSe.bind("<Enter>", lambda event, btn=buttonDelSe: btn.config(bg="gray"))
buttonDelSe.bind("<Leave>", lambda event, btn=buttonDelSe: btn.config(bg="#93908F"))

buttonCancel = Button(Searching, text="Cancel", font=("Minecraft", 14), command=menuExit, fg="white", bg="#93908F")
buttonCancel.place(relx=0.69, rely=0.9, anchor="n")
buttonCancel.bind("<Enter>", lambda event, btn=buttonCancel: btn.config(bg="gray"))
buttonCancel.bind("<Leave>", lambda event, btn=buttonCancel: btn.config(bg="#93908F"))

Searching.mainloop()
