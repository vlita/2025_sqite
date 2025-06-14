
# 2025 sQITE
This repository contains data-generation workflows for the 2025 sQITE study. Its dependencies are nstair/qforte, NumPy, and Matplotlib. 

This repository is organized into 3 main file types: 
- `_data.py` scripts (*which run the QITE algorithm and populate the folders corresponding to specific molecular geometries*).
- `_.dat` files (*which contain the raw data from each run*).
- `_.ipynb` notebooks (*which import the raw data and create plots*).
# 
For example, to generate a plot comparing sQITE energy error to classical resource usage for the 8-ene system, run the `ene_selected_data.py` script. This will call the function which runs the qite algorithm (using the `run_job.py` script) and generates a separate data file for each function call in the `ene/eight` folder. The data is then imported and read in order to make plots, in the corresponding `ene_plot.ipynb` jupyter notebook. 


