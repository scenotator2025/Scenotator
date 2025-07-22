import json, argparse

from utils.apollo_record import build_scenario_dict_, prepare_map_data


parser = argparse.ArgumentParser(description='Process samples of Apollo record.')
parser.add_argument('-t', '--task', type=str, default='data', help='"map" for preparing map file, "data" for structuring data samples')
parser.add_argument('-sd', '--data_dir', type=str, help="the directory of record file")
parser.add_argument('-f', '--data_file', type=str, help="record file name")
parser.add_argument('-md', '--map_dir', type=str, default='./utils/', help='the directory of map file')
parser.add_argument('-m', '--map_name', type=str, help='map name, e.g., "borregas_ave"')
parser.add_argument('-o', '--output', type=str, default='', help="output directory")
args = parser.parse_args()


if __name__ == '__main__': 
    # MAP_NAME = "borregas_ave"
    # MAP_ROOT_DIR = "./utils/"
    # RECORD_ROOT_DIR = "./samples/ApolloRecord/"
    # RECORD_NAME = "apollo_dev_ROUTE_1.Scenario_00000.00000"
    # TEST_DIR = f'./test/test_{RECORD_NAME}.json'
    MAP_NAME = args.map_name
    MAP_ROOT_DIR = args.map_dir
    RECORD_ROOT_DIR = args.data_dir
    RECORD_NAME = args.data_file
    SAVE_DIR = f'{args.output}/{RECORD_NAME}.json'

    if args.task == "map": 
        prepare_map_data(MAP_NAME, MAP_ROOT_DIR, MAP_ROOT_DIR)
    elif args.task == "data":  
        scenario_data = build_scenario_dict_(RECORD_ROOT_DIR, RECORD_NAME, MAP_NAME)
        with open(SAVE_DIR, "w") as f:
            json.dump(scenario_data, f, indent=2)
        print(f"Please check the structured sample in {SAVE_DIR}")
