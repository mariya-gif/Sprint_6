import allure
import pytest

from url import MAIN_URL


ORDER_DATA = [
    {
        "name": "Мария",
        "surname": "Иванова",
        "address": "Москва, ул. Ленина, 10",
        "metro_search": "спор",
        "metro_station": "Спортивная",
        "phone": "+79161234567",
        "rent_period": "сутки",
        "color": "black",
        "comment": "Позвонить у подъезда",
    },
    {
        "name": "Пётр",
        "surname": "Сидоров",
        "address": "Санкт-Петербург, Невский пр., 1",
        "metro_search": "аэро",
        "metro_station": "Аэропорт",
        "phone": "+79997654321",
        "rent_period": "трое суток",
        "color": "grey",
        "comment": "",
    },
]

ENTRY_POINTS = ["top", "bottom"]


class TestOrder:
    @allure.title("Заказ: вход={entry_point}, данные №{data_index} — форма, успех, лого")
    @pytest.mark.parametrize("entry_point", ENTRY_POINTS)
    @pytest.mark.parametrize("data_index, order_data", list(enumerate(ORDER_DATA)))
    def test_full_order_flow(self, main_page, order_page, entry_point, data_index, order_data):
        main_page.open_main()

        if entry_point == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page.fill_step_one(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro_search"],
            order_data["metro_station"],
            order_data["phone"],
        )
        order_page.fill_step_two(
            order_data["rent_period"],
            order_data["color"],
            order_data["comment"],
        )

        assert order_page.is_order_success_shown(), "Модалка об успешном заказе не появилась"

        # Проверка логотипов — продолжение того же сценария после успешного заказа
        redirected_url = main_page.click_yandex_logo_and_get_new_tab_url()
        assert "dzen" in redirected_url, "Лого Яндекса не привело на Дзен"

        main_page.click_scooter_logo()
        assert main_page.driver.current_url == MAIN_URL, "Лого самоката не вернуло на главную"