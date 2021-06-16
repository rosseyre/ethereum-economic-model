# CADLabs Ethereum Validator Economics Model

[![Python package](https://github.com/cadCAD-edu/ethereum-model/actions/workflows/python.yml/badge.svg)](https://github.com/cadCAD-edu/ethereum-model/actions/workflows/python.yml)

A modular dynamical systems model implemented using the open-source Python library radCAD (TODO: ADD LINK TO CADLABS REPO), a next-gen implementation of [cadCAD](https://cadcad.org).

**Official Eth2 specs version**: 
* Implements the [Altair](https://github.com/ethereum/eth2.0-specs#altair) updates in the [Beige Gorgon / v1.1.0-alpha.3](https://github.com/ethereum/eth2.0-specs/releases/tag/v1.1.0-alpha.3) release. (TODO: UPDATE FOR LATEST ALTAIR VERSION?)

## Table of Contents
* [Context](#context)
* [Model Features](#model-features)
* [Directory Structure](#directory-structure)
* [Model Architecture](#model-architecture)
* [Running Experiments](#running-experiments)
* [Development](#development)
* [Tests](#tests)
* [Jupyter Lab Environment](#jupyter-lab-environment)
* [Change Log](#change-log)
* [Contributors](#contributors)
* [Acknowledgements](#contributors)
* [Copyleft](#copyleft)

---

## Context

This open-source model was developed in collaboration with the Ethereum Robust Incentives Group, and funded by the Ethereum Foundation Eth2 Staking Community Grants. It accompanies the cadCAD Edu course "[cadCAD Masterclass: Ethereum Validator Economics](https://www.cadcad.education/course/masterclass-ethereum)". It intends to provide the Ethereum community with a highly versatile, customizable and extensible research tool, and includes a list of model extension ideas (TODO: link to model extension ideas here).  

(TODO: Describe in a few sentences how this model came about)

## Model Features

* Configurable to reflect protocol behavior at different points in time of the development roadmap (referred to as "development stages" in this model):<br />
  * post Beacon Chain launch, pre EIP1559, pre PoS (validators receive PoS incentives, EIP1559 disabled, and PoW still in operation)<br />
  * post Beacon Chain launch, post EIP1559, pre PoS (validators receive PoS incentives, EIP1559 enabled with miners receiving tips, and PoW still in operation)<br />
  * post Beacon Chain launch, post EIP1559, post PoS (validators receive PoS incentives, EIP1559 enabled with validators receiving tips, and PoW deprecated)<br />
* Supports [state space analysis](https://en.wikipedia.org/wiki/State-space_representation) (i.e. simulation of system behavior over time) and [phase space analysis](https://en.wikipedia.org/wiki/Phase_space) (i.e. generation of all unique system states in a given experimental setup)
* Customizable processes to set important variables such as ETH price, ETH staked, EIP1559 transaction pricing, and transaction rates
* Modular model structure for convenient extension and modification. This allows different user groups to refactor the model for different purposes, rapidly test new incentive mechanisms, or to update the model as Ethereum implements new protocol improvements.
* References to official [Eth2 specs](https://github.com/ethereum/eth2.0-specs) in Policy and State Update Function logic. This enables seamless onboarding of protocol developers or for the more advanced cadCAD user to dig into the underlying protocol design that inspired the logic.

## Directory Structure
* [data/](data/): datasets used in model
* [docs/](docs/): work-in-progress documentation of model software architecture
* [experiments/](experiments/): experiment workflow configuration and execution
* [logs/](logs/): experiment log files
* [model/](model/): model structure, parts, and configuration
* [notebooks/](notebooks/): experiment analysis notebooks (TODO: Integrate into experiments directory, TBC)
* [outputs/](outputs/): experiment outputs (images, datasets, etc.)
* [tests/](tests/): unit and integration tests for model and notebooks

## Model Architecture

The model/ directory contains the model's software architecture in the form of two categories of modules: structural modules and configuration modules.

### Structural Modules (TODO: Discuss renaming modules and/or reordering code for better accessibiltiy)

The model is composed of several structural modules in the [model/parts/](model/parts/) directory:

| Module | Description |
| --- | --- |
| [ethereum.py](model/parts/ethereum.py) | Basic Ethereum mechanisms such as EIP1559 transaction pricing, and updates to ETH price and supply |
| [incentives.py](model/parts/incentives.py) | Calculation of Proof of Stake reward, penalty and slashing incentives |
| [metrics.py](model/parts/metrics.py) | Calculation of validator operational cost, revenue, profit, and yield metrics |
| [stages.py](model/parts/stages.py) | Management of stages of the Ethereum system upgrade process |
| [spec.py](model/parts/spec.py) | Relevant extracts from the official Eth2 spec |
| [validators.py](model/parts/validators.py) | Implementation of validator processes such as activation, staking, uptime |

### Configuration Modules

The model is configured using several configuration modules in the [model/](model/) directory:

| Module | Description |
| --- | --- |
| [constants.py](model/constants.py) | Constants used in the model e.g. number of epochs in a year, Gwei in 1 Ether |
| [simulation_configuration.py](model/simulation_configuration.py) | Simulation configuration such as the number of timesteps and Monte Carlo runs |
| [state_update_blocks.py](model/state_update_blocks.py) | cadCAD model state update block structure, composed of Policy and State Update Functions |
| [state_variables.py](model/state_variables.py) | Model State Variable definition, configuration, and defaults |
| [stochastic_processes.py](model/stochastic_processes.py) | Helper functions to generate stochastic environmental processes |
| [system_parameters.py](model/system_parameters.py) | Model System Parameter definition, configuration, and defaults |
| [types.py](model/types.py) | Various types used in the model, such as the `Stage` Enum and calculation units |
| [utils.py](model/utils.py) | Misc. utility and helper functions |

## Running Experiments (TODO: Combine Notebooks into Experiment directory and make respective changes below)

The [experiments/](experiments/) directory contains modules for configuring and executing simulation experiments, as well as performing post-processing of the results.

The [experiments/templates/](experiments/templates/) directory contains different experiment templates which are used in the Jupyter experiment notebooks in the [notebooks/](notebooks/) directory to answer research questions and perform scenario analyses.

See the [notebooks/README.ipynb](notebooks/README.ipynb) notebook for a walk-through of how to configure and execute an experiment.

We created several experiment notebooks as a basis for analyzing the economics Ethereum validators are confronted with under a variety of scenarios. These notebooks and analysis don't aim to comprehensively illuminate the Ethereum protocol, but rather to answer the most salient questions and serve as inspiration for building out more customized analysis and model extensions.

### 1. Model Validation

The purpose of this notebook is to recreate selected simulations from the widely acknowledged Hoban/Borgers Ethereum 2.0 Economic Model using the CADLabs model, and to compare the results. We suggest that the CADLabs model has a high degree of validity.

### 2. Validator Revenue Yields and Profit Yields (Validator-level Analysis)

The purpose of this notebook is to explore the returns validators can expect from staking in the Ethereum protocol across different time horizons, adoption scenarios, ETH price scenarios and validator environments.

(TODO: Draft analysis, below first cut)

Analysis 1: Revenue and Profit Yields Over Time 
(Notes: can we include a slider for time horizon below the chart, and another one, maybe a dropdown, where peopel can set the average adoption level over the set time period? premium version would be three different adoption scenarios, a) extrapolated linearly from past; then one 50% less aggressive and one 50% more aggressive than past growth; something like that; then in a second slider people can set the average ETH price; premium version similar to the above) 

Analysis 2: Revenue and Profit Yields Over Adoption Curve
(Notes: Same as Analysis 1 but x-axis is ETH staked levels; while above analysis will be more interesting to validators (time value of money matters), this one will have more analytical value to the Ethereum Community; Sliders in this )

Analysis 3: Revenue and Profit Yields Over ETH Price Curve
(Notes: Same as Analysis 1 but x-axis is ETH Price levels; while above analysis will be more interesting to validators (time value of money matters), this one will have more analytical value to the Ethereum Community)

Analysis 4: Profit Yields By Validator Environment Over Time
(Notes: Same as Analysis 1 but y axis has profit yields of the different environments)


### 3. Network Issuance and Inflation Rate (Network-level Analysis)

The purpose of this notebook is to explore the ETH issuance and resulting annualized inflation rate across different time horizons and adoption scenarios. It includes a breakdown of issuance into reward types , the well-known "Ultrasound Monday" (peak ETH) analysis by Just Drake, and an analyis of the inflation impact of EIP1559. 

(TODO: Draft analysis, below first cut)

Analysis 1: TBC, let's define once the previous notebook is done
Analysis 2: TBC, let's define once the previous notebook is done
Analysis 3: TBC, let's define once the previous notebook is done

### 4. Other Analysis

The purpose of this notebook is to provide inspiration for other analysis that the model supports. Most of these analysis are in a work-in-progres  and marked as such. 

### Experiment Execution

The base experiment is an experiment that uses the default cadCAD System Parameters, Initial State, and State Update Blocks defined in the [models/](models/) directory. To run the base experiment from the terminal, execute the `experiments.run` module:
```bash
python3 -m experiments.run
```

Alternatively, open and run one of the Jupyter experiment notebooks in Jupyter Lab or Notebook.

### Experiment Workflow

1. Choose or create a new experiment template in the [experiments/templates/](experiments/templates/) directory
2. Copy the template experiment from [experiments/template.py](experiments/template.py) into the directory
3. Customize the base experiment using the template
4. Create a new Jupyter experiment notebook using the [notebooks/template.ipynb](notebooks/template.ipynb) experiment notebook template
5. Execute your experiment, post-process and analyze the results, and create Plotly charts!

## Development

A [Makefile](Makefile) is included for convenience, for example to setup your environment and start Jupyter Lab:

```bash
python3 -m venv venv
source venv/bin/activate

make setup # Setup environment
make start # Start Jupyter Lab
```

Otherwise, follow the steps below.

### Requirements

* Python versions: tested with 3.7, 3.8, 3.9
* Python dependencies: tested against versions in `requirements.txt`

### Setup

To setup a Python 3 development environment:
```bash
# Create a virtual environment using Python 3 venv module
python3 -m venv venv
# Activate virtual environment
source venv/bin/activate
# Install Python 3 dependencies inside virtual environment
pip install -r requirements.txt
```

## Tests

### Pytest Tests

To execute the Pytest tests:
```bash
source venv/bin/activate
python3 -m pytest tests
```

### Notebook Tests

```bash
source venv/bin/activate
make execute-notebooks
```

## Jupyter Environment

### Jupyter kernel

To setup your Jupyter Kernel within your virtual environment:
```bash
source venv/bin/activate
python3 -m ipykernel install --user --name python-cadlabs-eth-model --display-name "Python (CADLabs Ethereum Model)"
```

### Start environment

```bash
source venv/bin/activate
jupyter notebook
# Or Jupyter Lab, following additional steps below
jupyter lab
```

### Plotly Jupyter Lab support

To install and use Plotly with Jupyter Lab, you'll need NodeJS installed to build Node dependencies. Alternatively, use Jupyter Notebook which works out the box with Plotly.

See https://plotly.com/python/getting-started/

```bash
pip install jupyterlab "ipywidgets>=7.5"
jupyter labextension install jupyterlab-plotly@4.14.3
```

## Roadmap

The following is a non-exhaustive list of possible model extensions and future features:
* Implement the ability to simulate an inactivity leak scenario
* Implement a dynamic EIP1559 basefee with a feedback loop based on blockspace demand / network congestion
* Backtest the model against historical data such as the ETH price, ETH staked to determine expected historical yields
* Extend the model to cover future Ethereum upgrade stages after merge, such as sharding
* Apply Hoban/Borgers security (cost of attack) and required rate of return (RSAVY) analysis to simulation results
* ...

## Change Log

See [CHANGELOG.md](CHANGELOG.md) for notable changes and versions.

## Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributions to this project repo.

## Acknowledgements

* Ethereum 2.0 Economic Review. July 16, 2020. "An Analysis of Ethereum’s Proof of Stake Incentive Model". By Tanner Hoban and Thomas Borgers. For the extensive research that inspired the development of our model and the assumptions we adopted.

## Copyleft

(TODO: Which license options do we have? Can we keep attribution of base model in all distributions?)
