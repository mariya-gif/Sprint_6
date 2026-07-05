# tests/test_order.py
import allure
import pytest

from data import ORDER_DATA, ENTRY_POINT_METHODS


class TestOrder:
    @allure.title("Заказ: точка входа={entry_point_method}, данные №{data_index}")
    @pytest.mark.parametrize("entry_point_method", ENTRY_POINT_METHODS)
    @pytest.mark.parametrize("data_index, order_data", list(enumerate(ORDER_DATA)))
    def test_full_order_flow(self, main_page, order_page, entry_point_method, data_index, order_data):
        main_page.open_main()
        getattr(main_page, entry_point_method)()

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


class TestLogos:
    @allure.title("Клик по лого самоката ведёт на главную")
    def test_scooter_logo_redirects_to_main(self, main_page):
        main_page.open_main()
        main_page.click_scooter_logo()
        assert main_page.is_on_main_page(), "После клика лого не вернуло на главную"

    @allure.title("Клик по лого Яндекса открывает Дзен в новой вкладке через редирект")
    def test_yandex_logo_redirects_to_dzen(self, main_page):
        main_page.open_main()
        redirected_url = main_page.click_yandex_logo_and_get_new_tab_url()
        assert "dzen" in redirected_url, "Лого Яндекса не привело на Дзен"