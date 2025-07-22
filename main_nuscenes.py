import argparse
from utils.nuscenes import build_scenario_dict_, prepare_map_data


parser = argparse.ArgumentParser(description='Process samples in nuScenes.')
parser.add_argument('-t', '--task', type=str, default='data', help='"map" for preparing map file, "data" for structuring data samples')
parser.add_argument('-sd', '--data_dir', type=str, help="the directory of record file")
parser.add_argument('-m', '--map_dir_original', type=str, default='./utils/', help='the directory of map file')
parser.add_argument('-md', '--map_dir_processed', type=str, default='./utils/', help='the directory of map file')
parser.add_argument('-o', '--output', type=str, default='', help="output directory")
args = parser.parse_args()


if __name__ == '__main__':
    # MAP_DIR = './samples/nuScenes-map-expansion-v1.3'
    # MAP_ROOT_DIR = './utils'
    # DATA_DIR = './samples/nuScenes_v1.0-mini'
    # TEST_ROOT_DIR = './test/'
    MAP_DIR = args.map_dir_original
    MAP_ROOT_DIR = args.map_dir_processed
    DATA_DIR = args.data_dir
    SAVE_DIR = args.output

    
    if args.task == "map": 
        prepare_map_data(MAP_DIR, MAP_ROOT_DIR)
    elif args.task == "data": 
        build_scenario_dict_(data_dir=DATA_DIR, save_root_dir=SAVE_DIR)
        print(f"Please check the structured sample in {SAVE_DIR}")