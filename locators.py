from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

button_lk = ".//div[@id='root']//nav[@class='AppHeader_header__nav__g5hnF']/a[@href='/account']/p[""@class='AppHeader_header__linkText__3q_va ml-2']"  # Кнопка Личный кабинет
name_registration = ".//fieldset[1]/div[@class='input__container']/div/input[@name='name']"  # Имя на форме регистрации
email_registration = ".//fieldset[2]/div[@class='input__container']/div/input[@name='name']"  # email на форме регистрации
password_registration = ".//input[@name='Пароль']"  # Пароль на форме регистрации
login = ".//form[@class='Auth_form__3qKeq mb-20']/button[.='Войти']"  # кнопка Войти
registration = "Зарегистрироваться"  # ссылка "Зарегистрироваться"
entrance = "Auth_login__3hAey"  # Заголовок Входа
register = "button_button__33qZ0"  # Кнопка регистрации
error_password = "input__error"  # Сообщение об  ошибке пароля
entrance_button = "button_button__33qZ0"  # кнопка входа
name_send = "Марина"  # имя для регистрации
email_send = "marina_zagaynova_6_129@yandex.ru"  # email для авторизации и регистрации
password_send = "123456"  # пароль для регистрации и авторизации
exit_button = "Account_button__14Yp3"  # кнопка выхода
entrance_link = "Auth_link__1fOlj"  # ссылка для входа
restore_password = "Восстановить пароль"  # ссылка восстановления пароля
email_login = ".//input[@name='name']"  # поле ввода email при авторизации
text_main = "text_type_main-large"  # текст на главной странице
constructor = "Конструктор"  # меню для перехода к конструктору
souses = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[2]/span"  # меню соусы в конструкторе
fillings = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[3]/span"  # меню начинки в конструкторе
buns = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div[1]/span"  # меню булок в конструкторе
souses_test = ".//p[text()='Соус с шипами Антарианского плоскоходца']"  # текст для проверки перехода к соусам
fillings_test = ".//p[text()='Филе Люминесцентного тетраодонтимформа']"  # текст для проверки перехода к начинкам
buns_test = ".//p[text()='Краторная булка N-200i']"  # текст для проверки перехода к булкам
