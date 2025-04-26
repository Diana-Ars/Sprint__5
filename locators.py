from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для регистрации
    ENTER_TO_ACC = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]" #кнопка для перехода на страницу с кнопкой Зарегистрироваться
    REG_BUTTON = [By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]"] #кнопка для открытия формы регистрации
    NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input" ) #поле Имя
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") #поле Email
    PASSWORD = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input") #поле Password
    REGISTER_BUTTON = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]" #кнопка для завершения регистрации в форме регистрации
    ERROR_MESSAGE_PASSWORD = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]" #Текст сообщения об ошибке при вводе невалидного пароля

    #Локаторы для авторизации
    ENTER_BUTTON = By.XPATH, '//button[contains(text(), "Войти")]' #Кнопка "Войти" в форме авторизации
    PERSONAL_ACC_BUTTON = By.XPATH, '//p[contains(text(), "Личный Кабинет")]' #Кнопка для входа в Личный Кабинет
    ENTER_IN_REG_FORM = By.XPATH, '//a[contains(text(), "Войти")]' #Кнопка "Войти" в форме регистрации
    RECOVER_PASSWORD = By.XPATH, '//a[contains(text(), "Восстановить пароль")]' #Кнопка "Восстановить пароль" в форме авторизации
    PROFILE_TEXT = By.XPATH, '//a[contains(text(), "Профиль")]' #Ссылка, отображающаяся на странице Личного кабинета
    CONSTRUCTOR_TEXT = By.XPATH, '//h1[contains(text(), "Соберите бургер")]' #Заголовок, отображающийся на странице Конструктора бургеров
    ENTER_TEXT = By.XPATH, '//h2[contains(text(), "Вход")]' #Заголовок, отображающийся на странице авторизации

    #Локаторы для конструктора
    ENTER_CONSTRUCTOR = By.XPATH, '//p[contains(text(), "Конструктор")]' #Кнопка "Конструктор" в шапке сайта
    ENTER_BY_LOGO = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' #Кликабельный логотип в шапке сайта
    LOG_OUT = By.XPATH, '//button[contains(text(), "Выход")]' #Кнопка "Выход" в Личном Кабинете
    ENTER_TO_SOUCES = By.XPATH, '//span[contains(text(), "Соусы")]' #Кнопка "Соусы" в Конструкторе "Соберите бургер"
    SOUCES = By.XPATH, '//h2[text()="Соусы"]/following-sibling::*[self::ul][1]' #Список соусов в Конструкторе "Соберите бургер"
    ENTER_TO_BUNS = By.XPATH, '//span[contains(text(), "Булки")]' #Кнопка "Булки" в Конструкторе "Соберите бургер"
    BUNS = By.XPATH, '//h2[text()="Булки"]/following-sibling::*[self::ul][1]' #Список булок в Конструкторе "Соберите бургер"
    ENTER_TO_FILLING = By.XPATH, '//span[contains(text(), "Начинки")]' #Кнопка "Начинки" в Конструкторе "Соберите бургер"
    FILLINGS = By.XPATH, '//h2[text()="Начинки"]/following-sibling::*[self::ul][1]' #Список начинок в Конструкторе "Соберите бургер"

