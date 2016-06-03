# API_tutotial2016
This is an API tutorial for a workshop at "Code for DC's National Day of Civic Hacking"

## What is an API?
* **Application Programming Interface**
* **“set of routines, protocols, and tools for building software and applications” [Wikipedia]**
* **Usually used when someone makes an app that uses data**
* **Access:**
  - **Databases (comment sections on websites,  open government data)**
  - **streaming data (e.g uber, twitter)**


## Files description:

* **One `.keynote` with some basic API info and a resources slide**
* **Two `.py` files**:
  - `API_code.py` contains code to grab data from the [30-day crime API](http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8?mapSize=map-normal)
  - `scheduled_API_code.py` contains code to _schedule_ grabing of the data so you can collect multiple times at regular intervals (eg when running on a server):
        - Data is appended to a csv,
        - Duplicates are removed,
        - Scheduling is (currently, but you can change it) once every ~29 days
* **One `.ipynb` file that steps through the process more clearly (hopefully)**
  - the code is a little different from `API_code.py` but essentally does the same thing
* **One `.geojson` file as an example of API output**
* **Two `.csv.` example output files. They are _slightly_ different:**
  - `spyder_foo.csv` is an output when running the `scheduled_API_code.py` from my Spyder IDE
  - `ipython_foo.csv` is the output when running the `ipython notebook` code.
