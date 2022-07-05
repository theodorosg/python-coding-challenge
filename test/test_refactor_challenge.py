import pytest
import challenges.refactoring.to_refactor_challenge as refactor_challenge

test_read_file_input_data = [
    ["1\n", "1111\n", "1111\n", "111111\n", "222\n", "aaa\n", "a123\n"]
]


@pytest.mark.parametrize("expected", test_read_file_input_data)
def test_read_file(expected) -> None:
    actual = refactor_challenge.read_file()

    assert actual == expected


test_removed_new_lines_input_data = [
    (["1\n", "1111\n", "1111\n", "111111\n", "222\n", "aaa\n", "a123\n"],
     ["1", "1111", "1111", "111111", "222", "aaa", "a123"]),
    (["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n", "9\n"],
     ["1", "2", "3", "4", "5", "6", "7", "8\n", "9\n"])
    # Should this be like that?
    # ,(["1\n", "1"]) # This should also work
]


@pytest.mark.parametrize("input, expected", test_removed_new_lines_input_data)
def test_removed_new_lines(input, expected) -> None:
    actual = refactor_challenge.removed_new_lines(input)

    assert actual == expected


test_create_duplicate_dictionary_input_data = [
    (["1", "2", "2"], {"1": 1, "2": 2})
]


@pytest.mark.parametrize("input, expected",
                         test_create_duplicate_dictionary_input_data)
def test_create_duplicate_dictionary(input, expected) -> None:
    actual = refactor_challenge.create_duplicate_dictionary(input)

    assert actual == expected


test_find_most_duplicated_value_input_data = [
    ({"1": 1, "2": 2}, 2)
]


@pytest.mark.parametrize("input, expected",
                         test_find_most_duplicated_value_input_data)
def test_find_most_duplicated_value(input, expected) -> None:
    actual = refactor_challenge.find_most_duplicated_value(input)

    assert actual == expected


test_find_most_duplicated_key_input_data = [
    ({"1": 1, "abc": 2}, "abc")
]


@pytest.mark.parametrize("input, expected",
                         test_find_most_duplicated_key_input_data)
def test_find_most_duplicated_key(input, expected) -> None:
    actual = refactor_challenge.find_most_duplicated_key(input)

    assert actual == expected


test_find_number_of_digits_input_data = [
    (["1", "2", "3", "a", "b"], 3)
]


@pytest.mark.parametrize("input, expected",
                         test_find_number_of_digits_input_data)
def test_find_number_of_digits(input, expected) -> None:
    actual = refactor_challenge.find_number_of_digits(input)

    assert actual == expected


test_find_number_of_letters_input_data = [
    (["1", "2", "3", "a", "b"], 2)
]


@pytest.mark.parametrize("input, expected",
                         test_find_number_of_letters_input_data)
def test_find_number_of_letters(input, expected) -> None:
    actual = refactor_challenge.find_number_of_letters(input)

    assert actual == expected


test_find_number_of_alphanumerics_input_data = [
    (["1", "2", "3", "a", "b"], 5),
    (["a1a", "1"], 2)
]


@pytest.mark.parametrize("input, expected",
                         test_find_number_of_alphanumerics_input_data)
def test_find_number_of_alphanumerics(input, expected) -> None:
    actual = refactor_challenge.find_number_of_alphanumerics(input)

    assert actual == expected


test_main_input_data = [
    ("Most duplicated value(s): 1111 and appeared 2 time(s)\nNumber of digits:  5\nNumber of strings:  1\nNumber of alphanumerics:  7\n")
]


@pytest.mark.parametrize("expected", test_main_input_data)
def test_main(capsys, expected) -> None:
    refactor_challenge.main_function_to_refactor()
    captured = capsys.readouterr()
    assert captured.out == expected
