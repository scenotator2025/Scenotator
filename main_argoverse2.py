import json, argparse

from utils.argoverse2 import build_scenario_dict_


parser = argparse.ArgumentParser(description='Process samples in Argoverse 2.')
parser.add_argument('-sd', '--data_dir', type=str, help="the directory of sample")
parser.add_argument('-md', '--map_dir', type=str, help='the directory of map file')
parser.add_argument('-o', '--output', type=str, default='', help="output directory")
args = parser.parse_args()


if __name__ == '__main__':
    # MAP_DIR = './samples/argoverse2/'
    # DATA_DIR = './samples/argoverse2/scenario_0c6f84ef-fc15-46b6-8506-64f76a15c07c.parquet'
    # TEST_DIR = './test/test_argoverse2.json'
    MAP_DIR = args.map_dir
    DATA_DIR = args.data_dir
    SAVE_DIR = args.output

    scenario_data = build_scenario_dict_(DATA_DIR, MAP_DIR)
    with open(SAVE_DIR, 'w') as f:
        json.dump(scenario_data, f, indent=2)
    print(f"Please check the structured sample in {SAVE_DIR}")
