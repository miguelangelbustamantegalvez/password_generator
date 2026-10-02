from generator.password_generator import generate_password


def test_password_length():
    password = generate_password(12)
    assert len(password) == 12


def test_password_different_lengths():
    assert len(generate_password(8)) == 8
    assert len(generate_password(16)) == 16
    assert len(generate_password(20)) == 20
