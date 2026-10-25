# CyberWatch — Individual CIT Capstone Project Summary

**Project:** CyberWatch — Security Log Monitoring System  
**Course:** CS 4500 CIT Seminar / Capstone  
**Institution:** William Paterson University  
**Project format:** Individual

## Motivation
Repeated failed authentication attempts can indicate suspicious activity. Small teams and students benefit from a simple demonstration tool that makes these patterns visible without requiring a full enterprise SIEM.

## Goals and MVP scope
Build a locally runnable Flask application that imports synthetic authentication CSV data, applies a time-window detection rule, presents a dashboard, and lets users investigate and resolve alerts.

## Technical solution
Python/Flask handles upload and server routes; SQLite stores event and alert records; HTML, Bootstrap, JavaScript, and Chart.js provide the dashboard. Pytest checks the detection logic, and GitHub stores source history.

## Deliverables included
Application code, tests, sample and invalid-input CSVs, dashboard screenshot, README, technical design, user guide, and test evidence.

## Project roles
Individual project: planning, development, testing, documentation, and demonstration are the student's responsibilities.

## Challenges and lessons
Detection thresholds need explicit boundary tests. CSV imports require strict validation. Displayed alert counts should be interpreted with status and database history in mind.

## Future work
Live log ingestion, stronger deployment security, more detection rules, duplicate-import controls, reporting, and authentication.

## Repository
https://github.com/DannyD1288/CyberWatch-Capstone
