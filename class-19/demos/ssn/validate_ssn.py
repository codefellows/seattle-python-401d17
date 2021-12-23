import re


def validate(ssn):
    pattern = "111-22-3333"
    pattern = r"\d\d\d-\d\d-\d\d\d\d"
    pattern = r"\d{3}-\d{2}-\d{4}"
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    pattern = r"^(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}$"

    match_obj = re.match(pattern, ssn)

    return match_obj.group() if match_obj else None


goodies = ["111-22-3333", "555-22-3333"]

# https://www.geeksforgeeks.org/how-to-validate-ssn-social-security-number-using-regular-expression/

baddies = [
    "666-22-3333",
    "000-22-3333",
    "900-22-3333",
    "555-00-3333",
    "111-222-3333",
    "555-22-0000",
]

questionables = [
    "1111-22-3333",
    "111-22-33333",
]  # extra leading or trailing number

for ssn in goodies:
    assert validate(ssn)

for ssn in baddies:
    assert validate(ssn) is None

for ssn in questionables:
    assert validate(ssn) is None


print("TESTS PASSED")
