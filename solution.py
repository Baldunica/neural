import os;
import shutil;

train_dir = 'train';
val_dir = 'val';
test_dir = 'test';
test_data_portion = 0.1;
val_data_portion = 0.1;

def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.makedirs(os.path.join(dir_name, "broadleaf"))
    os.makedirs(os.path.join(dir_name, "grass"))
    os.makedirs(os.path.join(dir_name, "soil"))
    os.makedirs(os.path.join(dir_name, "soybean"))

create_directory(train_dir)
create_directory(val_dir)
create_directory(test_dir)

def distribution(folder_name,count, train_folder, test_folder,val_folder):
  start_val_data_idx = int(count * (1 - val_data_portion - test_data_portion))
  start_test_data_idx = int(count * (1 - test_data_portion))
  for i in range(1, start_val_data_idx):
    shutil.copy(os.path.join(folder_name, str(i) + ".tif"), 
    os.path.join(train_folder,folder_name))

  for i in range(start_val_data_idx, start_test_data_idx):
    shutil.copy(os.path.join(folder_name, str(i) + ".tif"), 
    os.path.join(val_folder,folder_name))

  for i in range(start_test_data_idx, count):
    shutil.copy(os.path.join(folder_name, str(i) + ".tif"), 
    os.path.join(test_folder,folder_name))

broadleaf_count = len(os.listdir("broadleaf"));
grass_count = len(os.listdir("grass"));
soybean_count = len(os.listdir("soybean"));
soil_count = len(os.listdir("soil"));

distribution('broadleaf',broadleaf_count,'train','test','val');
distribution('grass',grass_count,'train','test','val');
distribution('soil',soil_count,'train','test','val');
distribution('soybean',soybean_count,'train','test','val');

os.remove('broadleaf');
os.remove('grass');
os.remove('soil');
os.remove('soybean');




