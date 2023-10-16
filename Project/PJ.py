from tkinter import *
window = Tk()
window.title("Miniproject 2.1.0")
window.wm_iconbitmap("c:/012/.vscode/Project/icon_minecraft.ico")
window.geometry("925x530+250+100")

def menuExit():
    window.destroy() 

bg = PhotoImage(file="c:/012/.vscode/Project/MINIPROJECT.png")
label = Label(window, image=bg) 
label.place(x=0, y=0, relwidth=1, relheight=1)  # ให้ Label มีขนาดเท่ากับหน้าต่าง

text = Label(window, text="MINIPROJECT", font=("Minecraft Ten", 45),bg="lightgray")
text.place(relx=0.52, rely=0.05, anchor="n")  # จัดวางข้อความตรงกลางของหน้าต่าง

def Organizer():
    Organizer = Toplevel(window)
    Organizer.title("Organizer")
    Organizer.geometry("925x530+250+100")

    bg = PhotoImage(file="C:/012/.vscode/Project/M.png")
    label = Label(Organizer,image=bg)
    label.pack(expand=YES)

    def menuExit():
            Organizer.destroy()

    label1 = Label(Organizer,text="Organizer",font=("Minecraft", 20),fg="white",bg="#93908F")
    label1.place(relx=0.43 ,rely=0.035)

    label2 = Label(Organizer,text="หัวหน้ากลุ่ม",font=("Minecraft", 13),fg="white",bg="#93908F")
    label2.place(relx=0.12 ,rely=0.2)  

    label3 = Label(Organizer,text="รองหัวหน้า",font=("Minecraft", 13),fg="white",bg="#93908F")
    label3.place(relx=0.458 ,rely=0.2)

    label4 = Label(Organizer,text="สมาชิก",font=("Minecraft", 13),fg="white",bg="#93908F")
    label4.place(relx=0.83 ,rely=0.2)

    #รูปภาพสมาชิก
    imageAn=PhotoImage(file="C:/012/.vscode/Project/og/o.png")
    label = Label(Organizer, image=imageAn)
    label.pack()
    label.place(x=100, y=160) 
    
    imagePb=PhotoImage(file="C:/012/.vscode/Project/og/p.png")
    label = Label(Organizer, image=imagePb)
    label.pack()
    label.place(x=410, y=160) 

    imageLb=PhotoImage(file="C:/012/.vscode/Project/og/l.png")
    label = Label(Organizer, image=imageLb)
    label.pack()
    label.place(x=735, y=160) 

    #ชื่อสมาชิก
    label5 = Label(Organizer,text="นายอภิวัตร แนมใส\nรหัสนักศึกษา 654234012",font=("Minecraft", 13),fg="white",bg="#93908F")
    label5.place(relx=0.07 ,rely=0.65)  

    label6 = Label(Organizer,text="นายปกรณ์ บุญทวิวัฒน์\nรหัสนักศึกษา 654234027",font=("Minecraft", 13),fg="white",bg="#93908F")
    label6.place(relx=0.4 ,rely=0.65)  

    label7 = Label(Organizer,text="นายลุกมาน บุญแต่ง\nรหัสนักศึกษา 654234038",font=("Minecraft", 13),fg="white",bg="#93908F")
    label7.place(relx=0.76 ,rely=0.65)

    def Organizer2():
        Organizer2 = Toplevel(Organizer)
        Organizer2.title("Sorting")
        Organizer2.geometry("925x530+250+100") 
        bg = PhotoImage(file="C:/012/.vscode/Project/M.png")

        def menuExit():
            Organizer2.destroy()

        label = Label(Organizer2, image=bg) 
        label.place(x=0, y=0, relwidth=1, relheight=1)

        label = Label(Organizer2,text="Organizer",font=("Minecraft", 20),fg="white",bg="#93908F")
        label.place(relx=0.43 ,rely=0.035)

        label = Label(Organizer2,text="สมาชิก",font=("Minecraft", 13),fg="white",bg="#93908F")
        label.place(relx=0.14 ,rely=0.2)  

        label = Label(Organizer2,text="สมาชิก",font=("Minecraft", 13),fg="white",bg="#93908F")
        label.place(relx=0.48 ,rely=0.2)

        label = Label(Organizer2,text="สมาชิก",font=("Minecraft", 13),fg="white",bg="#93908F")
        label.place(relx=0.82 ,rely=0.2)

        #รูปภาพสมาชิก
        imageAn=PhotoImage(file="C:/012/.vscode/Project/og/f.png")
        label = Label(Organizer2, image=imageAn)
        label.pack()
        label.place(x=100, y=160) 
        
        imagePb=PhotoImage(file="C:/012/.vscode/Project/og/n.png")
        label = Label(Organizer2, image=imagePb)
        label.pack()
        label.place(x=410, y=160) 

        imageLb=PhotoImage(file="C:/012/.vscode/Project/og/h.png")
        label = Label(Organizer2, image=imageLb)
        label.pack()
        label.place(x=735, y=160) 

        #ชื่อสมาชิก
        label = Label(Organizer2,text="นายพีรพล มุสลิมีน\nรหัสนักศึกษา 654234008",font=("Minecraft", 13),fg="white",bg="#93908F")
        label.place(relx=0.07 ,rely=0.65)  

        label = Label(Organizer2,text="นายธนวัฒน์ ทองแจ้ง\nรหัสนักศึกษา 654234026",font=("Minecraft", 13),fg="white",bg="#93908F")
        label.place(relx=0.41 ,rely=0.65)  

        label = Label(Organizer2,text="นายฮัยกัลฮูซัยฟี มะเย็ง\nรหัสนักศึกษา 654234044",font=("Minecraft", 13),fg="white",bg="#93908F")
        label.place(relx=0.753 ,rely=0.65)

        #ปุ่ม Exit
        Exit=Button(Organizer2,text="   Exit   ",font=("Minecraft", 14), fg="white", bg="#93908F",command=menuExit)
        Exit.place(relx=0.04,rely=0.85)

        Organizer2.mainloop()
    #ปุ่ม Exit
    Exit=Button(Organizer,text="   Exit   ",font=("Minecraft", 14), fg="white", bg="#93908F",command=menuExit)
    Exit.place(relx=0.04,rely=0.85)    
    #ปุ่ม Next
    Next=Button(Organizer,text="   Next   ",font=("Minecraft", 14), fg="white", bg="#93908F",command=Organizer2)
    Next.place(relx=0.85,rely=0.85)

    Organizer.mainloop()
    
def menuSorting():
    Sorting = Toplevel(window)
    Sorting.title("Sorting")
    Sorting.geometry("925x530+250+100") 
    bg = PhotoImage(file="c:/012/.vscode/Project/M.png")
    label = Label(Sorting, image=bg) 
    label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def menuExit():
        Sorting.destroy()

    def clear_button_clicked():
        entry.delete(0, 'end')
        result.config(text="")    

    def bubble_sort(array, step):
        for i in range(1, len(array)):
            flag = 0
            for j in range(len(array) - i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    flag = 1
                step[0] += 1  # เพิ่มขั้นตอนการทำงาน
                Sorting.after(1000 * step[0], update_result, array.copy(), step[0])
    # ฟังก์ชันสำหรับการเรียงลำดับและแสดงผลลัพธ์
    def bubble_array():
        input_array = list(map(int, entry.get().split()))
        step = [0] # เก็บขั้นตอนการทำงานปัจจุบัน
        result.config(text="")# เคลียร์ป้ายรายการเพื่อเริ่มการทำงานใหม่
        bubble_sort(input_array, step)

    def insertion_sort(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1       
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        return array    

    def insertion_array():
        input_array = list(map(int, entry.get().split()))
        step = [0] # เก็บขั้นตอนการทำงานปัจจุบัน
        result.config(text="")# เคลียร์ป้ายรายการเพื่อเริ่มการทำงานใหม่
        insertion_sort(input_array, step)

    def selection_sort(array, current_step):
        size = len(array)
        for i in range(size - 1):
            min = i
            for j in range(i + 1, size):
                if array[j] < array[min]:
                    min = j
            array[i], array[min] = array[min], array[i]
            current_step[0] += 1
            Sorting.after(1000* current_step[0], update_result, array.copy(), current_step[0])

    def selection_array():
        input_array = list(map(int, entry.get().split()))
        current_step = [0]
        result.config(text="")
        selection_sort(input_array, current_step)

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr

    def merge_array():
        input_array = list(map(int, entry.get().split()))
        sorted_array = merge_sort(input_array)
        result.config(text="จากสูตร mergesort ผลลัพธ์ : " + " ".join(map(str, sorted_array)))     

    # ฟังก์ชันสำหรับอัปเดตผลลัพธ์บนป้ายรายการ
    def update_result(sorted_array, step):
        result.config(text=result.cget("text") + f"ขั้นตอนที่ {step}:อาเรย์ปัจจุบัน: {sorted_array}\n")  

    def click(event):
        entry.config(state=NORMAL)
        entry.delete(0, END)                      

    entry = Entry(Sorting, font=("Helvetica", 15))
    entry.place(relx=0.5, rely=0.05, anchor="n")
    entry.insert(0, "กรุณาใส่ข้อมูล 5 ตัว")
    entry.config(state=DISABLED)
    entry.bind("<Button-1>",click)

    result = Label(Sorting, text="", font=("Helvetica", 12))
    result.place(relx=0.5, rely=0.15, anchor="n") 

    sort_var = StringVar()
    sort_var.set(" ")

    buttonBubble = Button(Sorting, text="  Bubble Sort ", font=("Minecraft", 14), fg="white", bg="#93908F", command=bubble_array)
    buttonBubble.place(relx=0.18, rely=0.8, anchor="n")
    buttonBubble.bind("<Enter>", lambda event, btn=buttonBubble: btn.config(bg="gray"))
    buttonBubble.bind("<Leave>", lambda event, btn=buttonBubble: btn.config(bg="#93908F"))

    buttonInsertion = Button(Sorting, text="  Insertion Sort  ", font=("Minecraft", 14), fg="white", bg="#93908F", command=insertion_array)
    buttonInsertion.place(relx=0.40, rely=0.8, anchor="n")
    buttonInsertion.bind("<Enter>", lambda event, btn=buttonInsertion: btn.config(bg="gray"))
    buttonInsertion.bind("<Leave>", lambda event, btn=buttonInsertion: btn.config(bg="#93908F"))

    buttonSelection = Button(Sorting, text=" Selection Sort ", font=("Minecraft", 14), fg="white", bg="#93908F", command=selection_array)
    buttonSelection.place(relx=0.64, rely=0.8, anchor="n")
    buttonSelection.bind("<Enter>", lambda event, btn=buttonSelection: btn.config(bg="gray"))
    buttonSelection.bind("<Leave>", lambda event, btn=buttonSelection: btn.config(bg="#93908F"))

    buttonMerge = Button(Sorting, text="  Merge Sort  ", font=("Minecraft", 14), fg="white", bg="#93908F", command=merge_array)
    buttonMerge.place(relx=0.85, rely=0.8, anchor="n")
    buttonMerge.bind("<Enter>", lambda event, btn=buttonMerge: btn.config(bg="gray"))
    buttonMerge.bind("<Leave>", lambda event, btn=buttonMerge: btn.config(bg="#93908F"))

    buttonDelSe = Button(Sorting, text="   Reset Data   ", font=("Minecraft", 14), fg="white", bg="#93908F", command=clear_button_clicked)
    buttonDelSe.place(relx=0.64, rely=0.9, anchor="n")
    buttonDelSe.bind("<Enter>", lambda event, btn=buttonDelSe: btn.config(bg="gray"))
    buttonDelSe.bind("<Leave>", lambda event, btn=buttonDelSe: btn.config(bg="#93908F"))

    buttonOutSe = Button(Sorting, text="     Cancel    ", font=("Minecraft", 14), fg="white", bg="#93908F", command=menuExit)
    buttonOutSe.place(relx=0.85, rely=0.9, anchor="n")
    buttonOutSe.bind("<Enter>", lambda event, btn=buttonOutSe: btn.config(bg="gray"))
    buttonOutSe.bind("<Leave>", lambda event, btn=buttonOutSe: btn.config(bg="#93908F"))

    Sorting.mainloop()

def menuSearching():#สร้างหน้าต่างSearching
    Searching = Toplevel(window)
    Searching.title("Searching")
    Searching.geometry("925x530+250+100")
    bg = PhotoImage(file="c:/012/.vscode/Project/M.png")
    label = Label(Searching, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)

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

button1 = Button(window, text="           Sorting           ", font=("Minecraft", 18),fg="white",command=menuSorting, bg="#93908F")
button1.place(relx=0.52, rely=0.5, anchor="n")
button1.bind("<Enter>", lambda event, btn=button1: btn.config(bg="gray"))
button1.bind("<Leave>", lambda event, btn=button1: btn.config(bg="#93908F"))

button2 = Button(window, text="          Searching         ", font=("Minecraft", 18),fg="white",command=menuSearching, bg="#93908F")
button2.place(relx=0.52, rely=0.61, anchor="n")
button2.bind("<Enter>", lambda event, btn=button2: btn.config(bg="gray"))
button2.bind("<Leave>", lambda event, btn=button2: btn.config(bg="#93908F"))

button3 = Button(window, text=" Organizer ", font=("Minecraft", 17),fg="white", bg="#93908F",command=Organizer)
button3.place(relx=0.43, rely=0.75, anchor="n")
button3.bind("<Enter>", lambda event, btn=button3: btn.config(bg="gray"))
button3.bind("<Leave>", lambda event, btn=button3: btn.config(bg="#93908F"))

button4 = Button(window, text=" Quit game ", font=("Minecraft", 17),fg="white",command = menuExit, bg="#93908F")
button4.place(relx=0.62, rely=0.75, anchor="n")
button4.bind("<Enter>", lambda event, btn=button4: btn.config(bg="gray"))
button4.bind("<Leave>", lambda event, btn=button4: btn.config(bg="#93908F"))

window.grid_rowconfigure(2, weight=1)  

window.mainloop()