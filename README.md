# Scenotator


## Prerequisites
1. Python3
2. [Anaconda](https://www.anaconda.com/)


## Step by step

**NOTE** Due to dataset license restrictions, we do not provide full training scripts or end-to-end execution. However, we provide model architecture and necessary scripts to demonstrate the core logic of our method.

### Data sample structuring. 

#### For Argoverse 2

1. Download Argoverse 2 dataset  
Follow the instructions [here](https://argoverse.github.io/user-guide/getting_started.html#downloading-the-data) to download the Argoverse 2 motion forecasting data.

2. Environment setup  
Follow the instructions [here](https://argoverse.github.io/user-guide/getting_started.html#setup) to install the necessary dependencies. 

3. Structure sample  
Run Scenotator by the following command:
```bash
python3 main_argoverse2.py -sd <sample_file_dir> -md <map_file_dir> -o <output_dir>
```

#### For nuScenes

1. Download nuScenes dataset  
Follow the instructions [here](https://www.nuscenes.org/nuscenes#download) to download the nuScenes data.

2. Environment setup  
Follow the instructions [here](https://github.com/nutonomy/nuscenes-devkit/blob/master/docs/installation.md) to install the necessary dependencies. 

3. Process map data
```bash
python3 main_nuScenes.py -t map -m <original_map_dir> -md <processed_map_file_dir>
```

4. Structure sample
```bash
python3 main_nuScenes.py -t data -sd <sample_dir> -md <processed_map_file_dir> -o <output_dir>
```

#### For Apollo Record

1. Collect Apollo records  

2. Environment setup  
Install `protobuf 3.19.4` for ACAV, by the following command: 
```shell
pip3 install protobuf==3.19.4
```
Install `cyber_record`, a cyber record file offline parse tool, by the following command: 
```shell
pip3 install cyber_record
```
To avoid introducing too many dependencies, save messages by `record_msg`.
```shell
pip3 install record_msg -U
```
Install `shapely` for ACAV, by the following command: 
```shell
pip3 install shapely
```

3. Process map data
```bash
python3 main_apollo_record.py -t map -m <map_name> -md <processed_map_file_dir>
```
To tramsform the `.bin` map file into `.json` map file, you can use the script `./utils/map_covert_to_json.py`. 

4. Structure sample
```bash
python3 main_apollo_record.py -t data -sd <record_file_dir> -f <record_file_name> -m <map_name> -o <output_directory>
```


### For the GNN Model

1. Download Waymo Open Motion dataset  
Check [here](https://waymo.com/open/download) to download the Waymo Open Motion dataset v1.2.  
⚠️ Due to its license agreement, we do not provide any original or derived data.

2. Environment setup for preprocessing samples  
Follow the instructions [here](https://github.com/waymo-research/waymo-open-dataset/blob/master/tutorial/tutorial_motion.ipynb) to install the necessary dependencies. 

3. Preprocess samples 
```bash
conda activate waymo
python3 preprocessing.py -d <data_dir>
```

4. Environment setup for training
```bash
bash setup_dependencies.sh
```

5. Train the model
```bash
python3 -m train --lr <learning_rate> --epochs <epochs>
```