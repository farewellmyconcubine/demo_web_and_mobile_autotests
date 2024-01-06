import os.path


def get_personal_env_path():
    main_path = os.path.abspath(os.path.dirname(__file__))
    private_path = os.path.join(main_path, '.env.personal_data.private')
    example_path = os.path.join(main_path, '.env.personal_data.example')

    if os.path.exists(private_path):
        return private_path
    else:
        return example_path

def get_test_data_path():
    main_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(main_path, '.env.test_data')