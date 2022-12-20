from tkinter import *


window = Tk()
window.title("ИСО exam")
window.geometry('450x450')

first_click = True

main_label = Label(window, text="Введите значения", font=("Arial Bold", 20), fg="black")
main_label.grid(column=0, row=0)

time_label = Label(window, text="Замеренное время(мин) для одного человека", font=("Arial Bold", 15))
time_label.grid(column=0, row=2)

time_entry = Entry(window, width=15, font=("Arial Italic", 20), )
time_entry.grid(column=0, row=3, pady=10)
time_entry.focus()

intensity_label = Label(window, text="Число людей", font=("Arial Bold", 15))
intensity_label.grid(column=0, row=4)

intensity_entry = Entry(window, width=15, font=("Arial Bold", 20))
intensity_entry.grid(column=0, row=5, pady=10)

time2_label = Label(window, text="Сколько времени был тест", font=("Arial Bold", 15))
time2_label.grid(column=0, row=6)

time2_entry = Entry(window, width=15, font=("Arial Italic", 20), )
time2_entry.grid(column=0, row=7, pady=10)


def clicked():
    global first_click
    global main_label
    

    def destroy_all():
        relative_pass_ability_label.destroy()
        absolute_pass_ability_label.destroy()
        probability_denial_label.destroy()
        average_count_of_clients_of_toilets_label.destroy()
        probability_denial_label.destroy()
        average_amount_of_queue_label.destroy()
        average_time_on_toilet_label.destroy()

    def rounder(x):
        return round(x, 4)


    
    try:
        time_service = float(time_entry.get())
        input_quantity = float(intensity_entry.get())
    except:
        main_label.destroy()
        main_label = Label(window, text="Неверный ввод", font=("Arial Bold", 20), fg="red")
        main_label.grid(column=0, row=0)
        return 

    window.geometry('450x820')

    main_label.destroy()
    
   

    main_label = Label(window, text="Успешно", font=("Arial Bold", 20), fg="green")
    main_label.grid(column=0, row=0)

    result_label = Label(window, text="Результаты", font=("Arial Bold", 20))
    result_label.grid(column=0, row=9, pady=5)

    try:
      # интенсивность потока
      intensity = 1 / time_service
      intensity = rounder(intensity)
      intensity_label = Label(window, text="Интенсивность потока: " + str(intensity))
      intensity_label.grid(column=0, row=10, pady=5, sticky="w")

      # интенсивность нагрузки
      nagruzka = intensity / time_service
      nagruzka = rounder(nagruzka)
      nagruzka_label = Label(window, text="Интенсивность нагрузки: " + str(nagruzka))
      nagruzka_label.grid(column=0, row=11, pady=5, sticky="w")

      # вероятность что канал свободен
      probability_free = intensity / (input_quantity + intensity)
      probability_free = rounder(probability_free)
      probability_free_label = Label(window, text="Вероятность что канал свободен: " + str(probability_free))
      probability_free_label.grid(column=0, row=12, pady=5, sticky="w")


      # коэфицент загрузки системы
      coef_intensity_system = input_quantity / intensity
      coef_intensity_system = rounder(coef_intensity_system)
      coef_intensity_system_label = Label(window, text="Коэфицент загрузки системы: " + str(coef_intensity_system))
      coef_intensity_system_label.grid(column=0, row=13, pady=5, sticky="w")

      # относительная пропускная способность
      relative_pass_ability = intensity / (input_quantity + intensity)
      relative_pass_ability = rounder(relative_pass_ability)
      relative_pass_ability_label = Label(window, text="Относительная пропускная способность: " + str(relative_pass_ability))
      relative_pass_ability_label.grid(column=0, row=14, pady=5, sticky="w")

      # абсолютная пропускная способность
      absolute_pass_ability = input_quantity * relative_pass_ability
      absolute_pass_ability = rounder(absolute_pass_ability)
      absolute_pass_ability_label = Label(window, text="Абсолютная пропускная способность: " + str(absolute_pass_ability))
      absolute_pass_ability_label.grid(column=0, row=15, pady=5, sticky="w")

      # вероятность отказа
      probability_denial: float = 1 - relative_pass_ability
      probability_denial = rounder(probability_denial)
      probability_denial_label = Label(window, text="Вероятность отказа: " + str(probability_denial))
      probability_denial_label.grid(column=0, row=16, pady=5, sticky="w")

      # среднее время простоя
      average_time_of_idle = probability_denial * time_service
      average_time_of_idle = rounder(average_time_of_idle)
      average_time_of_idle_label = Label(window, text="Среднее время простоя: " + str(average_time_of_idle))
      average_time_of_idle_label.grid(column=0, row=17, pady=5, sticky="w")

      # среднее число обслуживаемых заявок
      average_count_of_clients = intensity * time_service
      average_count_of_clients = rounder(average_count_of_clients)
      average_count_of_clients_label = Label(window, text="Среднее число обслуживаемых заявок: " + str(average_count_of_clients))
      average_count_of_clients_label.grid(column=0, row=18, pady=5, sticky="w")

      # среднее число находящихся на обслуживании
      average_count_of_clients_of_toilets = (coef_intensity_system * (1 - (1 + 1) * coef_intensity_system ** (1) + 1 * coef_intensity_system ** (1 + 1)))/((1 - coef_intensity_system) * (1 - coef_intensity_system ** (1+1)))
      average_count_of_clients_of_toilets = rounder(average_count_of_clients_of_toilets)
      average_count_of_clients_of_toilets_label = Label(window, text="Среднее число находящихся на обслуживании: " + str(average_count_of_clients_of_toilets))
      average_count_of_clients_of_toilets_label.grid(column=0, row=19, pady=5, sticky="w")

      # средняя время в деле
      average_time_on_toilet = average_count_of_clients_of_toilets / (input_quantity * (1 - probability_denial))
      average_time_on_toilet = rounder(average_time_on_toilet)
      average_time_on_toilet_label = Label(window, text="Средняя время на станции(мин): " + str(average_time_on_toilet))
      average_time_on_toilet_label.grid(column=0, row=20, pady=5, sticky="w")

      # среднее нахождение в очереди
      average_time_on_queue = (average_time_on_toilet - 1) / intensity
      average_time_on_queue = rounder(average_time_on_queue)
      average_time_on_queue_label = Label(window, text="Среднее нахождение в очереди(cек): " + str(average_time_on_queue))
      average_time_on_queue_label.grid(column=0, row=21, pady=5, sticky="w")

      # длина очереди
      average_amount_of_queue = input_quantity * (1 - probability_denial) * average_time_on_queue
      average_amount_of_queue = rounder(average_amount_of_queue)
      average_amount_of_queue_label = Label(window, text="Среднее число людей на станции: " + str(average_amount_of_queue))
      average_amount_of_queue_label.grid(column=0, row=22, pady=5, sticky="w")

      
  
    except:
      main_label.destroy()
      main_label = Label(window, text="Данные невозможны", fg="red", font=("Arial Bold", 20))
      main_label.grid(column=0, row=0, pady=5)
      return

    return







btn = Button(window, text="Рассчитать", command=clicked, fg="black", bg="white", font=("Arial Bold", 20))
btn.grid(column=0, row=8, pady=5)



window.mainloop()
