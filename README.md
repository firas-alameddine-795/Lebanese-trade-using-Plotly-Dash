# Lebanese trade using Plotly-Dash

This repository holds the same project in two forms:

| Version | Where | What it is |
|---|---|---|
| **Notebook** | [`MSBA-FirasAlameddine.ipynb`](MSBA-FirasAlameddine.ipynb) | The original capstone: data cleaning and the Dash app in one notebook (updated to run on current Dash / pandas). |
| **Kedro project** | [`kedro_project/`](kedro_project/) | The same logic rebuilt as a tested, reproducible pipeline (ingestion, HS harmonization, enrichment) plus a `kedro dashboard` command. Produces an identical table to the notebook (1,413,972 rows). |

Both read the same raw Excel files, which are not stored in git. See [`kedro_project/README.md`](kedro_project/README.md) to run the pipeline.

---

Date of submission: September 1, 2020. Date of last update: November 20, 2026.

Despite the fact that the free fall of the Lebanese currency exchange rate has had severe negative impact on the economy, illustrated by the sharp increase in prices, this free fall could create an opportunity for the Lebanese industry to evolve and gain new momentum. In fact, the sharp increase of prices of imported products makes it almost impossible for ordinary consumers to buy as they used to do prior to the crisis, hence the need for cheaper local alternative goods (many of which are virtually inexistent). Also, the decrease of production costs (in US$) of Lebanese goods provides an opportunity for manufacturers to increase their level of exports to foreign markets, an act which would help eliminate gradually trade deficit as new markets start importing cheaper Lebanese goods compared to similar goods’ prices in these markets.

The goal of this capstone project is to support knowledge acquired throughout my MSBA by getting hand-on work experience with public data. The choice of such a topic is intentional: For it helps me hone my newly acquired skills in data analytics. Accordingly, the progression of my capstone will be divided into the following milestones:

- Milestone 1 - Use and analyze data in Lebanese Industry and Commerce:<br>In the First part, the focus will be on the collection of Lebanese Customs data, as well as international trade data available via official platforms, namely World Bank, WTO and WCO. The aim is to add my contribution in terms of reporting methodology, metrics, evaluation, use of visualization, coding automation and recommendations given.

- Milestone 2 - Data Overview:<br>The second part is more informative and will go through an overview of the data tools and sources, highlighting both strong and weak points. Tools to be used: Python (main work), Tableau (investigative work).

- Milestone 3 - Data Driven Answers:<br>Finally, the third part is meant to provide answers for the following questions:<br>
1- What are the main countries Lebanon is dealing with for each import/export category? How did it evolve with time from 2011 to 2019?<br>
2- What are the export verticals that are growing in Lebanon and what are the ones shrinking?<br>
3- How does our pricing per ton for exports compare with the one from other countries?<br>
4- Is the pricing per ton for our imports competitive? Are neighboring countries (such as Jordan) getting better deals?<br>
5- What are the export verticals that exist in Lebanon and that have a potential for growth as other comparable countries were able to grow in the past three years?<br>

Programming language: Python.
Packages:
- Data manipulation: Pandas.
- Data visualization: Matplotlib, Plotly
- Dashboard creation: Dash Open Source, Tableau

Tableau version of the dashboard:
https://public.tableau.com/app/profile/firas.alameddine/viz/LBNDashboard-Aug72020/Dashboard1
