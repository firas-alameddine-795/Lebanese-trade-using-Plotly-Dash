# Lebanese trade using Plotly-Dash

[![CI](https://github.com/firas-alameddine-795/Lebanese-trade-using-Plotly-Dash/actions/workflows/ci.yml/badge.svg)](https://github.com/firas-alameddine-795/Lebanese-trade-using-Plotly-Dash/actions/workflows/ci.yml)

This repository holds the same project in two forms:

| Version | Where | What it is |
|---|---|---|
| **Notebook** | [`MSBA-FirasAlameddine.ipynb`](MSBA-FirasAlameddine.ipynb) | The original capstone: data cleaning and the Dash app in one notebook (updated to run on current Dash / pandas). |
| **Kedro project** | [`kedro_project/`](kedro_project/) | The same logic rebuilt as a tested, reproducible pipeline (ingestion, HS harmonization, enrichment) plus a `kedro dashboard` command. Produces an identical table to the notebook (1,413,972 rows). |

Both read the same raw Excel files, which are not stored in git. See [`kedro_project/README.md`](kedro_project/README.md) to run the pipeline.

## Quick start (no private data needed)

The Kedro version ships a small synthetic dataset, so you can try it right after cloning. Run these in a terminal, **one after the other**:

```bash
git clone https://github.com/firas-alameddine-795/Lebanese-trade-using-Plotly-Dash.git
cd Lebanese-trade-using-Plotly-Dash/kedro_project                  # the commands below only work from this folder
pip install -r requirements.txt && pip install -e . --no-deps

kedro run --env sample          # step 1: build the data (about a second)
kedro dashboard --port 4400     # step 2: start the dashboard, then open http://127.0.0.1:4400
```

The numbers in the sample are made up and are not real trade flows. Stop the dashboard with `Ctrl+C`.
Details, the real-data workflow and the other commands are in [`kedro_project/README.md`](kedro_project/README.md).

---

Date of submission: September 1, 2020. Date of last update: November 20, 2026.

Despite the fact that the free fall of the Lebanese currency exchange rate has had severe negative impact on the economy, illustrated by the sharp increase in prices, this free fall could create an opportunity for the Lebanese industry to evolve and gain new momentum. In fact, the sharp increase of prices of imported products makes it almost impossible for ordinary consumers to buy as they used to do prior to the crisis, hence the need for cheaper local alternative goods (many of which are virtually inexistent). Also, the decrease of production costs (in US$) of Lebanese goods provides an opportunity for manufacturers to increase their level of exports to foreign markets, an act which would help eliminate gradually trade deficit as new markets start importing cheaper Lebanese goods compared to similar goods’ prices in these markets.

The goal of this capstone project is to support knowledge acquired throughout my MSBA by getting hand-on work experience with public data. The choice of such a topic is intentional: For it helps me hone my newly acquired skills in data analytics. Accordingly, the progression of my capstone will be divided into the following milestones:

- Milestone 1 - Use and analyze data in Lebanese Industry and Commerce:<br>In the First part, the focus will be on the collection of Lebanese Customs data, as well as international trade data available via official platforms, namely World Bank, WTO and WCO. The aim is to add my contribution in terms of reporting methodology, metrics, evaluation, use of visualization, coding automation and recommendations given.

- Milestone 2 - Data Overview:<br>The second part is more informative and will go through an overview of the data tools and sources, highlighting both strong and weak points. Tools to be used: Python (main work), Tableau (investigative work).

Programming language: Python.
Packages:
- Data manipulation: Pandas.
- Data visualization: Matplotlib, Plotly
- Dashboard creation: Dash Open Source, Tableau

Tableau version of the dashboard:
https://public.tableau.com/app/profile/firas.alameddine/viz/LBNDashboard-Aug72020/Dashboard1
