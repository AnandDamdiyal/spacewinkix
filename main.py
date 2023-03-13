import argparse
import pandas as pd
from src.data_collection.building_data_collection import BuildingDataCollector
from src.data_processing.building_data_processing import BuildingDataProcessor
from src.machine_learning.building_energy_prediction import BuildingEnergyPredictor
from src.visualization.energy_consumption_visualization import EnergyConsumptionVisualizer

def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', required=True, help='API key for building data collection')
    parser.add_argument('--building-id', required=True, help='ID of the building to collect data for')
    parser.add_argument('--start-date', required=True, help='Start date of data collection period in YYYY-MM-DD format')
    parser.add_argument('--end-date', required=True, help='End date of data collection period in YYYY-MM-DD format')
    args = parser.parse_args()

    # collect building data
    collector = BuildingDataCollector(args.api_key)
    data = collector.collect(args.building_id, args.start_date, args.end_date)

    # process building data
    processor = BuildingDataProcessor()
    processed_data = processor.process(data)

    # predict building energy consumption
    predictor = BuildingEnergyPredictor()
    energy_predictions = predictor.predict(processed_data)

    # visualize energy consumption
    visualizer = EnergyConsumptionVisualizer()
    visualizer.plot_energy_consumption(processed_data, energy_predictions)

if __name__ == '__main__':
    main()
