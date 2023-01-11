from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import os.path

from data import Technologist, Operator

Builder.load_file("ui.kv")


class MenuScreen(Screen):
    pass


class OperatorScreen(Screen):
    pass


class TechnologistScreen(Screen):
    pass


class ClientsScreen(Screen):
    # work
    def current_data(self):
        self.data = Technologist.show_client()
        self.ID, self.full_name, self.depart, self.role, self.date, self.sex, self.start, self.end = 'IDсотрудника\n', 'ФИО\n', 'Год рождения\n', 'Пол\n', 'Подразделение\n', 'Должность\n', 'Дата начала работы\n', 'Дата увольнения\n'
        for i in self.data:
            self.ID += f"{i[0]}\n"
            self.full_name += f"{i[1]}\n"
            self.depart += f"{i[2]}\n"
            self.role += f"{i[3]}\n"
            self.date += f"{i[4]}\n"
            self.sex += f"{i[5]}\n"
            self.start += f"{i[6]}\n"
            self.end += f"{i[7]}\n"

    # work
    def show_clients(self):
        self.current_data()
        self.ids['IDman'].text = self.ID
        self.ids['id_fullname_label'].text = self.full_name
        self.ids['id_depart'].text = self.depart
        self.ids['id_role'].text = self.role
        self.ids['id_date_label'].text = self.date
        self.ids['id_sex'].text = self.sex
        self.ids['id_start'].text = self.start
        self.ids['id_end'].text = self.end


# work
class AddClientScreen(Screen):
    def add(self, *args):
        Technologist.add_client(*args)


# work

class DelClientScreen(Screen):
    def delclient(self, category, key):
        Technologist.del_client(category, key)

class Devices(Screen):
    def current_data(self):
        self.data = Technologist.show_devices()
        self.id, self.name, self.model, self.year, self.departament, self.status = 'IDтехники\n', 'Название\n', 'Модель\n', 'Год выпуска\n', 'Подразделение\n', 'Статус\n'
        for i in self.data:
            self.id += f"{i[0]}\n"
            self.name += f"{i[1]}\n"
            self.model += f"{i[2]}\n"
            self.year += f"{i[3]}\n"
            self.departament += f"{i[4]}\n"
            self.status += f"{i[5]}\n"

    def show_info(self):
        self.current_data()
        self.ids['id_device'].text = self.id
        self.ids['name'].text = self.name
        self.ids['model'].text = self.model
        self.ids['year'].text = self.year
        self.ids['dep'].text = self.departament
        self.ids['status'].text = self.status


class AddDevice(Screen):
    def add_device(self, *args):
        Technologist.add_device(*args)


class DelDevice(Screen):
    def deldevice(self, category, key):
        Technologist.del_device(category, key)




class TestApp(App):
    Window.clearcolor = (.98, .89, .85, 1)

    def build(self):
        self.title = "Repair devices"
        sm = ScreenManager()
        sm.add_widget(TechnologistScreen(name='technologist'))
        sm.add_widget(ClientsScreen(name='clients'))
        sm.add_widget(AddClientScreen(name='addclient'))
        sm.add_widget(DelClientScreen(name='delclient'))
        sm.add_widget(Devices(name='tehnika'))
        sm.add_widget(DelDevice(name='deldevice'))
        sm.add_widget(AddDevice(name='adddevice'))
        return sm


if __name__ == '__main__':
    TestApp().run()
'''
Вывести для просмотра стоимость оплаты одной минуты разговора для разных населенных пунктов на заданную дату:
название организации, предоставляющей услуги связи - дата, название населенного пункта, стоимость одной минуты, льготная стоимость одной минуты.
Информация о компании
Поиск стоимости по дате
'''
