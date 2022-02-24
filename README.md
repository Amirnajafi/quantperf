
QuantPerf: Portfolio analytics and performance calculation for financial data
==========================================

**QuantPerf** Python library that performs portfolio profiling, allowing quants and portfolio managers to understand their performance better by providing them with in-depth analytics and risk metrics.



1. ``quantperf.report.perf`` - for calculating various performance metrics, like Sharpe ratio, Win rate, Volatility, etc.

2. ``quantperf.report.total_return_chart`` - for calculating total_return of DataSeries

Here's an example of a simple tear sheet analyzing a strategy:

Quick Start
===========

.. code:: python

    from quantperf.report import perf

    # fetch the daily returns for a stock
     df = pd.read_csv("./test_data/test_data.csv",parse_dates=['Date'] , index_col='Date')
    metrics , dataframe = perf(df['Close'])
	# metrics is metrics data that calculate and return as json 
	# dataframe is whole calculations for metrics for every row and date
	

Output:

.. code:: text

    # metrics should return you json data like this :
	{'annualized_downside_volatility': 3.13,
	 'anualreturn_1y': 21.01,
	 'anualreturn_3y': 21.95,
	 'anualreturn_5y': 17.02,
	 'anualreturn_si': 0.63,
	 'anuualized_gain_volatility': 2.79,
	 'anuualized_loss_volatility': 3.41,
	 'anuualized_volatility': 3.92,
	 'average_monthly_gain': 0.69,
	 'average_monthly_loss': -0.72,
	 'best_month': 9.39,
	 'best_month_date': '2020-03-24 ',
	 'burke_ratio': -0.0,
	 'calmar_ratio': 0.02,
	 'compounded_return': 0.09,
	 'gain_loss_ratio': 1.18,
	 'kurtosis': 19.43,
	 'maximum_drawdown': -33.79,
	 'maximum_drawdown_date': '2020-03-23 ',
	 'negative_months_fraction': 44.87,
	 'omega_ratio': 0.93,
	 'plm': -0.97,
	 'positive_months_fraction': 55.02,
	 'psi': 152.16,
	 'sharp_ratio': -0.08,
	 'skewness': -0.67,
	 'sortino_ratio': -0.03,
	 'sterling_ratio': -0.33,
	 'ulcer_index': 1.78,
	 'worse_month': -11.98,
	 'worse_month_date': '2020-03-16 ',
	 'yearly_return': {'2015': 1.4,
					   '2016': 11.96,
					   '2017': 21.83,
					   '2018': -4.38,
					   '2019': 31.49,
					   '2020': 18.4,
					   '2021': 28.71,
					   '2022': -4.84
			}}


**\*\*\* Full documenttion coming soon \*\*\***

In the meantime, you can get insights as to optional parameters for each method, by using Python's ``help`` method:

.. code:: python

    help(qs.stats.conditional_value_at_risk)

.. code:: text

	Help on function conditional_value_at_risk in module quantstats.stats:

	conditional_value_at_risk(returns, sigma=1, confidence=0.99)
	    calculats the conditional daily value-at-risk (aka expected shortfall)
	    quantifies the amount of tail risk an investment


Installation
------------

Install using ``pip``:

.. code:: bash

    $ pip install quantperf --upgrade --no-cache-dir


Requirements
------------

* `Python <https://www.python.org>`_ >= 3.5+
* `pandas <https://github.com/pydata/pandas>`_ (tested to work with >=0.24.0)
* `numpy <http://www.numpy.org>`_ >= 1.15.0


P.S.
------------
Please drop me a note with any feedback you have.

**Amir najafi**
