import data
import sender_stand_request


def get_kit_body(kit_name):
    kit_body = data.new_kit_body.copy()
    kit_body["name"] = kit_name
    return kit_body


def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.new_kit(kit_body)

    assert kit_response.status_code == 201


def negative_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.new_kit(kit_body)

    assert kit_response.status_code == 400

def negative_assert_no_characters(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_body.pop("name")
    kit_response = sender_stand_request.new_kit(kit_body)

    assert kit_response.status_code == 400

def test_1_character_in_kit_name_success_response():
    positive_assert(data.one_letter)

def test_511_character_in_kit_name_success_response():
    positive_assert(data.kit_body_511)

def test_no_characters_in_kit_name_error_response():
    negative_assert(data.no_characters)

def test_characters_in_kit_name_exceed_limit_error_response():
    negative_assert(data.kit_body_512)

def test_special_characters_in_kit_name_success_response():
    positive_assert(data.special_characters)

def test_spaces_in_kit_name_success_response():
    positive_assert(data.spaces_in_name)

def test_numbers_in_kit_name_success_response():
    positive_assert(data.str_numbers_in_name)

def test_no_parameters_in_the_request_error_response():
    negative_assert_no_characters(data.empty_kit_body)

def test_numbers_in_the_request_error_response():
    negative_assert(data.numbers_in_name)

