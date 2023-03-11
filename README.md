# Project 2: NYC taxi data (40 marks)

The New York City Taxi and Limousine Commission (TLC) publishes open data which contains information on all the taxi rides which have happened in the city each month. The data is available [here](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). The [user guide](https://www.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf) provided with the data describes in detail what is in the datasets.

You will get started on the project in the **Week 8 workshop**.

---

## Goal and structure

The goal of this project is for you to present a **coherent and well-coded investigation** into some aspects of the dataset. You should do this in the Jupyter notebook called **`project-2-report.ipynb`**, which will contain your code, as well as any results and visualisations. You should also use Markdown cells to structure the notebook, describe your investigations, and present/explain your results.

You should aim for approximately **2-4 main data visualisations** overall, each showing a key result of your investigation. These could potentially consist of multiple plots or smaller visualisations; you may also wish to display intermediate plots or results to demonstrate the processing of your data.

This project is an **open-ended** task, so you should come up with your **own ideas** to analyse the dataset and extract useful information or interesting facts. Some ideas of questions you might address in your analysis will be given in the section "Some ideas to get you started"; they are a guide to some things you could think about to get you started, but...

#### you don't need to answer them all, and you are strongly encouraged to answer questions that are not listed.

When you are presenting your investigation of each question, be sure to make a coherent discussion for each task (using Markdown, maths as appropriate and code cells) -- it does not need to be long, but it should be clear enough to explain the problem and interpret your results.

In particular, since you are working as a group, some work will be needed to combine all of the code and writing that you each contribute into the submitted notebook -- this is something that you should plan to do, and the quality of **presentation** will be marked.

---

## Data

Go through the [Week 8 workshop task](https://github.com/pp-22/pp-w08-workshop) to start exploring the data, and to learn to use the provided function `get_taxi_data()` to retrieve data.

As you explore the data, you should think carefully about **cleaning**. You may find some rides with an unreasonably high fare or short duration, for instance, which you might want to eliminate before further investigation. Any data cleaning you do must be part of your report.

You are also free to download and use more related data from other sources to complement your investigation if you wish. But make sure the data is licensed in a way which allows you to use it!

---

## Some ideas to get you started

Generally speaking, it's probably a good idea to **limit the scope of your report**, in space and in time. Here are a few examples of what you could consider:

- You could focus your investigation on a particular area of NYC (e.g. a borough, or even a specific neighbourhood).
- You could further focus on one type of taxi -- yellow, green, or private hire (e.g. Uber, Lyft, etc).
- You could choose a few variables in the data set and investigate how these change over time -- for instance, looking at long-term changes over the years, seasonal changes, changes depending on the day of the week, or depending on the time of day, etc.

Here are some example questions your report could address. Again, **you should not cover all of them** (aim for 2-4 main results!), and you are certainly encouraged to come up with your own questions too. The important thing is that your report is **coherent and well-presented**, that your **code** works as intended, and that you explore some of the aspects of this dataset in reasonable depth, presenting results in a way which help you answer relevant questions or queries. If you investigate 1 or 2 of these with sufficient depth, this should be plenty enough for a good report.

- Investigate geographical features in the data. For instance, where are the most common pick-up areas? Does this change depending on the time of day, weekday, or season? Can you correlate this with business/residential areas, or [popular city attractions](https://en.wikipedia.org/wiki/Tourism_in_New_York_City#Most_visited_attractions)?
- Investigate the influence of weather conditions on taxi usage: for instance, do people take more taxis when it's sunny or raining? A good place to obtain historical weather data is, for example, the [Meteostat API](https://dev.meteostat.net/guide.html), which also has a handy [Python package](https://dev.meteostat.net/python/) you can install and use to obtain data through an API (the same way you did in the Week 7 workshop).
- Over the years, the NYC subway has faced different [crises and challenges](https://en.wikipedia.org/wiki/New_York_City_Subway#Challenges), some of which have resulted in temporary closures of the subway. You could investigate whether such closures have had a visible effect on uptake of taxis.
- Using the distance and duration of the rides, can you identify rush hour (peak traffic congestion times in the day)?
- The [Oxford Covid-19 Government Response Tracker (OxCGRT) project](https://www.bsg.ox.ac.uk/research/research-projects/covid-19-government-response-tracker) has collected worldwide data of different countries' measures to limit the spread of Covid since the start of 2020. Investigate the potential impact of some of these measures on taxi usage -- for example, we might expect that lockdowns and public transportation closures could have an effect.
- The dataset contains information on trips taken specifically to the 3 main airports in NYC: JFK, Newark, and LaGuardia. Investigate the common pick-up locations for each of these airports, and whether there are significant differences.
- The [Yankee Stadium](https://en.wikipedia.org/wiki/Yankee_Stadium) is located in the Bronx. You could investigate taxi traffic to and from the stadium depending on whether there is a game or event on.
- You could investigate differences in traffic during some of NYC's [annual events](https://en.wikipedia.org/wiki/Timeline_of_New_York_City#Annual_events).
- The calculation of the standard taxi fare is explained [here](https://www.nyc.gov/site/tlc/passengers/taxi-fare.page). You could use this to make your own estimates of the fare, based on available data, and compare your results to the recorded fares in the data to identify possible errors in the dataset.
- Investigate long-term rider behaviour changes over the years, for instance in relative use of yellow/green taxis and private hire vehicles (Uber, etc), or different payment methods.


---

### Working on your project

During the Week 8 workshop, or as soon as possible after this, you should discuss with your group and come up with a **plan**.

- **Pair-program** as much as possible! You will likely be much more productive if you have another person to bounce ideas off of about what to investigate or how to present results, and help each other solve problems. You can do this in pairs, you can mix up pairs, you can even do "group programming" sessions with one driver and 2-3 navigators if that's helpful.
- Schedule quick **code reviews** for each other, to help each other stay on track and write better code.
- Use your shared GitHub repo to **collaborate**. Every time you start working on the project, start by **pulling** the latest version from GitHub. Then, as you work, **commit** your changes regularly. When you are done for the day (or even before that), **push** your work to the GitHub repo to share it with your team.
- To **submit** your project, the process will be the same as for Project 1: first, **push** your final version (ready for submission) **to your GitHub repo**, then submit your repo to Gradescope. Gradescope will be set up so that one person can submit the report on behalf of their group.

---

### Packages

You will create a new conda environment called `pp-proj2`, with the help of the `environment.yml` file, during the [Week 8 workshop](https://github.com/pp-22/pp-w08-workshop).

Beyond the packages installed in your new `pp-proj2` environment, you can also use any package or library that you find convenient. If there are any other packages you want to use:

- **Modify the `environment.yml` file** to add them to the list.
    - If the package can be installed with `conda`, then add it to the main list below `dependencies:`.
    - If the package can only be installed with `pip`, then add it to a secondary list starting with `- pip:`
- If you use Anaconda Navigator:
    - **Remove the old `pp-proj2` environment** in Anaconda Navigator, by clicking on it in the list of environments, and selecting "Remove" at the bottom.
    - **Import the (new) `environment.yml`** into Anaconda Navigator to re-create the environment `pp-proj2` with the new packages you've added.
- If you use the terminal:
    - Run the command `conda env update -f path/to/environment.yml`.
- **Activate** `pp-proj2` before launching Jupyter again.

Alternatively, you could also create a new environment with a different name, if you'd like to keep the original one! Just change the `name:` field in `environment.yml` and follow the instructions from the [Week 8 workshop](https://github.com/pp-22/pp-w08-workshop) to set it up. In any case, **make sure to include your `environment.yml` file in your repository when you submit.**

Here are a few packages you might find useful:

- If you choose to visualise anything on a map, packages like [folium](https://python-visualization.github.io/folium/) or [geopandas](https://geopandas.org/) might be useful. In particular, geopandas can deal with shapefiles such as those provided with the dataset.
- If you fancy making interactive visualisations, with things like toggle buttons or sliders, you could look into [IPython widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html). (This is how the "Solution" buttons are made in your tutorial notebooks, for example.)
- If you work with weather data, you could use the [Meteostat Python package](https://dev.meteostat.net/python/).

---

### Marking scheme

Your project will be marked on 4 criteria:

- Technical proficiency (16 marks)
- Amount of work done and depth of investigation (12 marks)
- Presentation and cohesion of the report (8 marks)
- Code comments, docstrings, code style, and readability (4 marks)

The detailed marking scheme will be available in your repositories under `project-2-markingscheme.md`.


### Providing references

Most of the content of your submission must be **authored by your group**. That being said, you may use any code from the course material (e.g. workshop tasks, tutorial sheets, videos), without citing it.

You may also use **small pieces of code** (a few lines max at a time) that you found elsewhere -- e.g. examples from the documentation, a textbook, forums, blogs, etc... You may use this code *verbatim* (i.e. almost exactly as you found it), or adapt it to write your own solution.

A programming assignment is just like any other academic assignment -- and therefore, **you must provide a citation for any such code**, whether you use it *verbatim* or adapt it. To do so, include a code comment at the start of your script or notebook cell, indicating:
- the line numbers where the code was used or adapted,
- the URL of the source (or, if it's from a book, a full reference to the book),
- the date you accessed the source,
- the author of the code (if the information is available).

You can use this template -- delete one of the URL or book reference lines as appropriate:
```python
# Lines X-Y: Author Name
# URL: http://...
# Book Title, year published, page number.
# Accessed on 10 Nov 2022.
```

You must also provide **detailed code comments** for any such code, in your own words, to demonstrate that you fully understand how it works -- you will lose marks if you use external code without explaining it, even if it's cited correctly.

Remember to exercise caution if you use any code from external sources -- there are a lot of blogs and forums out there with very bad code! I'd recommend that you review the Week 4 video on searching the documentation.

Of course, any **non-code sources** that you used for any of your work should also be cited appropriately. You can have a "**References**" section at the end of the notebook, in a Markdown cell, to give your list of references for such sources.

With all that, we trust that you'll be able to use your best judgement, and to cite your sources appropriately -- if anything is not clear, please do ask. Note that **all submissions** will be automatically checked (and manually reviewed) for plagiarism and collusion (between groups), and [the University's academic misconduct policy](https://www.ed.ac.uk/academic-services/staff/discipline/academic-misconduct) applies.
