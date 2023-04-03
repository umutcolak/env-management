from dotenv import load_dotenv, dotenv_values
import os

env = "test"
env_path = None
config = {}
root_dir = os.path.abspath(__file__)

while not os.path.exists(os.path.join(root_dir, 'test.env')):
    root_dir = os.path.dirname(root_dir)

if env == 'test':
    load_dotenv(f"{root_dir}/test.env")
    config = dotenv_values(f"{root_dir}/test.env")

elif env == 'prod':
    load_dotenv(f"{root_dir}/prod.env")
    config = dotenv_values(f"{root_dir}/prod.env")

print(config['KEY3'])
