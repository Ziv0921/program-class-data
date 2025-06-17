import os

logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
model_dir = os.path.join(os.path.dirname(__file__), 'models')
files_dir = os.path.join(os.path.dirname(__file__), 'files')

def init():
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

def get_file_path(filename):
    return os.path.join(files_dir, filename)

def get_logs_path(filename):
    return os.path.join(logs_dir, filename)

def get_model_path(filename):
    return os.path.join(model_dir, filename)