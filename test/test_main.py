import pytest
import main


def test_assert_true() -> None:
    assert True


test_print_input_data = [
    ("foo", "Input is: foo\n"),
    ("bar", "Input is: bar\n")
]


@pytest.mark.parametrize("input_string, expected", test_print_input_data)
def test_print_input(capsys, input_string, expected) -> None:
    main.print_input(input_string)
    captured = capsys.readouterr()
    assert captured.out == expected

