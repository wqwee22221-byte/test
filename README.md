*Test case#1: invalid date for login*
- Открыть страницу https://onlypult.com/login
- найти поле вводе Email (class="form-group form-group-lg field-loginform-email required has-error")
- Введи валидный email(сгенрируй какой-нибудь не валидный такого вида:"zxczxczxc123123123123@asd.com"
- Найди поле Password (.input-group input-group-lg)
- Введи любые символы, где число сиволов не меньше 6
- Нажми кнопку Login (.btn btn-primary btn-lg btn-block mb-3)
ОР: остались на странице https://onlypult.com/login,  под полем Password отображается текст с ошибка "Sorry, incorrect e-mail or password."     

