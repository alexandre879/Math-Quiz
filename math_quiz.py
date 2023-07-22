from tkinter import *
import random

root = Tk()
root.title('გამოიცანი-რიცხვი')
root.geometry('550x450')
image = PhotoImage(file='C:\\Users\\Alexi\\Desktop\\PP\\fff.png')
root.iconphoto(False, image)
root.configure(bg='#F0F0F0')

def main_page():
    score = 0

    def check_data():
        nonlocal attempts, score
        my_number = guess_entry.get().strip()

        if my_number == '':
            result_label.config(text='შეიტანეთ რიცხვი!', fg='red')
        elif not my_number.isdigit() or int(my_number) < 1 or int(my_number) > 100:
            result_label.config(text='თქვენ უნდა შეიტანოთ ნატურალური რიცხვი 1-დან 100-მდე!', fg='red')
        elif attempts > max_attempts:
            attempts += 1
            check_button.config(state='disabled')
            result_label.config(text=f'თქვენ წააგეთ!\nრიცხვი იყო ({computer_number})\nთავიდან დაიწყეთ თამაში.', fg='red')
            new_game_button.config(state='normal')
        elif int(my_number) > computer_number:
            attempts += 1
            result_label.config(text='თქვენს მიერ არჩეული რიცხვი არის მეტი, ჩემს რიცხვთან შედარებით, კიდევ ერთხელ ცადეთ.', fg='orange')
        elif int(my_number) < computer_number:
            attempts += 1
            result_label.config(text='თქვენს მიერ არჩეული რიცხვი არის ნაკლები, ჩემს რიცხვთან შედარებით, კიდევ ერთხელ ცადეთ.', fg='orange')
        else:
            attempts += 1
            result_label.config(text=f'გილოცავთ!\n🎉🎉🎉\nთქვენ გმაოიცანით რიცხვი\n{attempts} ცდაში', fg='green')
            score += 1
            score_label.config(text=f'ქულა: {score}')
            new_game_button.config(state='normal')
            check_button.config(state='disabled')
        attempts_label.config(text=f'ცდა: {attempts}')



    def start_new_game():
        nonlocal computer_number, attempts, attempts_label
        computer_number = random.randint(1, 100)
        attempts = 0
        result_label.config(text='')
        guess_entry.delete(0, 'end')
        new_game_button.config(state='disabled')
        check_button.config(state='normal')
        attempts_label.config(text=f'ცდა: {attempts}')

    def switch_to_second_page():
        main_page_frame.pack_forget()
        second_page_frame.pack()

    def switch_to_main_page():
        second_page_frame.pack_forget()
        main_page_frame.pack()

    def generate_math_quiz():
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(['+', '-', 'x', 'ხარისხად', '-ის განაყოფის მთელი ნაწილი', '%'])
        result = 0
        result_2 = ''
        

        if operator == '+':
            result = a + b
            math_quiz_label.config(text=f"რამდენი იქნება {a} {operator} {b}?")
        elif operator == '-':
            result = a - b
            math_quiz_label.config(text=f"რამდენი იქნება {a} {operator} {b}?")
        elif operator == 'x':
            result = a * b
            math_quiz_label.config(text=f"რამდენი იქნება {a} {operator} {b}?")
        elif operator == 'ხარისხად':
            result = (a ** b)
            math_quiz_label.config(text=f"რამდენი იქნება {a} {operator} {b}?")
        elif operator == '-ის განაყოფის მთელი ნაწილი':
            result = a // b
            math_quiz_label.config(text=f"რამდენი იქნება {a}-ის {b}-ზე გაყოფის მთელი ნაწილი?")
        elif operator == '%':
            result = a % b
            math_quiz_label.config(text=f"რა იქნება {a}-ის {b}-ზე გაყოფის ნაშთი")

        math_quiz_entry.delete(0, 'end')
        math_quiz_result.set(result)

    def check_math_quiz():
        nonlocal score
        user_answer = math_quiz_entry.get().strip()

        if not (user_answer.isdigit() or (user_answer.startswith('-') and user_answer[1:].isdigit())):
            math_quiz_result_label.config(text='შეიტანეთ რიცხვი!', fg='red')
        elif user_answer.strip() == '':
            math_quiz_result_label.config(text='თქვენ უნდა შეიტანოთ ნამდვილი რიცხვები 1-დან 100-მდე :)')
        elif float(user_answer) == math_quiz_result.get():
            math_quiz_result_label.config(text='პასუხი სწორია!', fg='green')
            score += 1
            score_label.config(text=f'ქულა: {score}')
        else:
            math_quiz_result_label.config(text='პასუხი არასწორია! კიდევ ერთხელ ცადეთ.', fg='red')



    computer_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    main_page_frame = Frame(root, bg='#F0F0F0')
    main_page_frame.pack()

  
    title_label = Label(main_page_frame, text='[გამოიცანი რიცხვი]', bg='#F0F0F0', fg='#333333', font=('Arial', 16, 'bold'))
    guess_label = Label(main_page_frame, text='გამოიცანი რიცხვი 1-დან 100-მდე 7 ცდაში', bg='#F0F0F0', fg='#333333', font=('Arial', 12))
    guess_entry = Entry(main_page_frame, width=30, font=('Arial', 12))
    result_label = Label(main_page_frame, text='', bg='#F0F0F0', fg='#333333', font=('Arial', 12), wraplength=250)
    check_button = Button(main_page_frame, text='შემოწმება', command=check_data, bg='#4CAF50', fg='white', font=('Arial', 12), relief='raised')
    new_game_button = Button(main_page_frame, text='ხელახლა თამაში', command=start_new_game, bg='#4CAF50', fg='white', font=('Arial', 12), relief='raised', state='disabled')
    second_page_button = Button(main_page_frame, text='შემდეგ გვერდზე გადასვლა', command=switch_to_second_page, bg='#4CAF50', fg='white', font=('Arial', 12), relief='raised')

    title_label.pack(pady=10)
    guess_label.pack(pady=10)
    guess_entry.pack(pady=5)
    result_label.pack(pady=10)
    check_button.pack()
    new_game_button.pack(pady=10)
    second_page_button.pack(pady=10)

    attempts_label = Label(main_page_frame, text=f'ცდა: {attempts}', bg='#F0F0F0', fg='#333333', font=('Arial', 12))
    attempts_label.pack() 

    second_page_frame = Frame(root, bg='#F0F0F0')

    second_page_label = Label(second_page_frame, text='არითმეტიკული კითხვები', bg='#F0F0F0', fg='#333333', font=('Arial', 16, 'bold'))
    main_page_button = Button(second_page_frame, text='წინა გვერდზე გადასვლა', command=switch_to_main_page, bg='#4CAF50', fg='white', font=('Arial', 12), relief='raised')
    second_page_main_label = Label(second_page_frame, text='(გამოიცანი პასუხები!!!)', bg='#F0F0F0', fg='#333333', font=('Arial', 12))

    math_quiz_label = Label(second_page_frame, text='', bg='#F0F0F0', fg='#333333', font=('Arial', 12))
    math_quiz_result = IntVar()
    math_quiz_entry = Entry(second_page_frame, width=30, font=('Arial', 12))
    math_quiz_result_label = Label(second_page_frame, text='', bg='#F0F0F0', fg='#333333', font=('Arial', 12))
    generate_quiz_button = Button(second_page_frame, text='დაგენერირება მათემატიკური კითხვების', command=generate_math_quiz, bg='#4CAF50', fg='white', font=('Arial', 12), relief='raised')
    check_quiz_button = Button(second_page_frame, text='შეამოწმე პასუხი', command=check_math_quiz, bg='#4CAF50', fg='white', font=('Arial', 12), relief='raised')
    score_label = Label(main_page_frame, text='ქულა: 0', bg='#F0F0F0', fg='#333333', font=('Arial', 12))


    second_page_label.pack(pady=10)
    second_page_main_label.pack(pady=10)
    main_page_button.pack(pady=10)
    score_label.pack()

    math_quiz_label.pack(pady=10)
    math_quiz_entry.pack(pady=5)
    math_quiz_result_label.pack(pady=10)
    generate_quiz_button.pack(pady=5)
    check_quiz_button.pack(pady=5)

    second_page_frame.pack_forget()


    root.mainloop()

main_page()