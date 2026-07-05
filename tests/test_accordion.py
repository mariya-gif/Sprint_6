import allure
import pytest

from data import ACCORDION_ANSWERS


class TestAccordion:
    @allure.title("Раскрытие ответа на вопрос №{index}")
    @pytest.mark.parametrize("index", range(8))
    def test_accordion_item_expands(self, main_page, index):
        main_page.open_main()
        main_page.open_accordion_item(index)
        assert main_page.is_accordion_panel_expanded(index), \
            f"Вопрос №{index} не раскрылся"
        assert main_page.get_accordion_panel_text(index).strip() == ACCORDION_ANSWERS[index], \
            f"Текст ответа на вопрос №{index} не совпадает с ожидаемым"