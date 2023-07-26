# Snifmap

A web application that displays a map with a road route, taking into account speeds at given points.

## Table of Contents

- [Introduction](#introduction)
- [How to run](#how-to-run)
- [Project structure](#project-structure)
- [Example json file](#example-json-file)

## Introduction

This tool simplifies the process of visualizing JSON data in a user-friendly format. After launching the application, navigate to ```localhost:5000``` in your web browser. Here, you'll find an intuitive interface where you can upload a JSON file and click the "Submit" button to generate route map.

Once you've selected the desired **.json** file, it will be saved in the designated folder **app/jsons**. Following the file upload and click the Submit button, the application will automatically generate an **index.html** file in the **app/src** directory and open in browser.

## How to run

If you have docker you can use this commends to run app

```bash
$ sudo docker-compose up -d --build
``` 
or

```bash
$ sudo docker-compose build && sudo docker-compose up -d
```

After a while the application will open in ```localhost:5000```


## Project structure
```
.
├── app
│   ├── jsons*
│   ├── requirements.txt
│   ├── src*
│   └── website
│       ├── main.py 
│       ├── snifmap.py
│       ├── static
│       │   ├── scripts.js
│       │   ├── src
│       │   └── styles.css
│       └── templates
│           └── home.html
├── docker-compose.yml
├── Dockerfile
├── nginx
│   └── default.conf
└── README.md
```

*directory ```app/src``` and ```app/jsons``` will creating automaticly.

## Example json file
Your JSON file must have this properties
* latitude
* longitude
* gpsSpeed

```json
[
    {
        "latitude":0.00,
        "longitude":0.00,
        "gpsSpeed":0
        }
]
```

| Variable    | Type    | Unit  | Description          |
| :---------- | :------ | :---- | :------------------- |
| `latitude`  | `float` | ----- | Earth latitude       |
| `longitude` | `float` | ----- | Earth longitude      |
| `gpsSpeed`  | `float` | `m/s` | Speed in each points |
