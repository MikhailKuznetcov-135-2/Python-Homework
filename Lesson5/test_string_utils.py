import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


class TestCapitalize:
    def test_capitalize_normal_string(self, utils):
        assert utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty_string(self, utils):
        # capitalize("") -> ""
        assert utils.capitalize("") == ""

    def test_capitalize_single_letter(self, utils):
        assert utils.capitalize("a") == "A"

    def test_capitalize_with_leading_space(self, utils):
        # важно: capitalize не убирает пробелы, он просто делает первую букву заглавной
        assert utils.capitalize(" skypro") == " skypro"


class TestTrim:
    def test_trim_with_leading_spaces(self, utils):
        assert utils.trim("   skypro") == "skypro"

    def test_trim_no_leading_spaces(self, utils):
        assert utils.trim("skypro") == "skypro"

    def test_trim_only_spaces(self, utils):
        # все пробелы должны удалиться, останется пустая строка
        assert utils.trim("    ") == ""

    def test_trim_empty_string(self, utils):
        assert utils.trim("") == ""


class TestContains:
    def test_contains_symbol_present(self, utils):
        assert utils.contains("SkyPro", "S") is True

    def test_contains_symbol_absent(self, utils):
        assert utils.contains("SkyPro", "U") is False

    def test_contains_empty_symbol(self, utils):
        # edge-case: пустая подстрока всегда содержится в любой строке
        assert utils.contains("SkyPro", "") is True

    def test_contains_empty_string_search_any(self, utils):
        # в пустой строке нет ни одного символа (кроме пустой подстроки)
        assert utils.contains("", "a") is False


class TestDeleteSymbol:
    def test_delete_symbol_single_char(self, utils):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self, utils):
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_found(self, utils):
        # если символа/подстроки нет, строка не должна меняться
        assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"

    def test_delete_symbol_multiple_occurrences(self, utils):
        assert utils.delete_symbol("banana", "a") == "bnn"

    def test_delete_symbol_empty_string(self, utils):
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_delete_all(self, utils):
        assert utils.delete_symbol("aaaa", "a") == ""