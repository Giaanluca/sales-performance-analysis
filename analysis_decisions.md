# Analysis Decisions and Reasoning

## Purpose

This document explains the reasoning behind the analytical and technical decisions made throughout the project.

The goal is to justify not only the choice of variables and visualizations, but also the structure of the data pipeline and the overall analytical approach.

---

## 1. Data Structure and Pipeline Design

A basic ETL pipeline was implemented to organize the data into:

* **Raw layer** → original dataset without modifications
* **Processed layer** → cleaned and transformed data ready for analysis

This separation ensures:

* Data integrity (raw data remains unchanged)
* Reproducibility of the analysis
* A structured workflow aligned with real-world data practices

---

## 2. Variable Selection

The analysis focused on variables directly related to the business question:

* Product
* Category
* Revenue / Sales Value
* Customer
* Transaction details

These were prioritized to identify top performers, revenue patterns, and lower-performing segments.

Variables less relevant to the business objective were intentionally excluded to maintain focus and clarity.

---

## 3. Visualization Choices

### Bar Charts

* Used for comparing categories and products side by side
* Effective for ranking and identifying top and low performers
* Preferred over pie charts for clarity and readability

### Line Charts

* Used to analyze revenue trends over time
* Helps identify patterns, fluctuations, and potential seasonality

### Donut Charts

* Used in the dashboard to show category contribution to total revenue
* Provides a quick overview of distribution while maintaining a clean visual design

---

## 4. Dashboard Design Decisions (Power BI)

The dashboard was designed to prioritize clarity and business usability:

* KPIs placed at the top for quick performance overview
* Trend analysis (revenue over time) positioned as the primary visual
* Category and customer breakdowns included to support deeper analysis
* Clean layout and consistent color scheme to improve readability

The goal was to create a tool that allows users to quickly understand performance and explore key insights.

---

## 5. Analytical Approach

Decisions were guided by the principle: *analyze what matters for the business question.*

The focus was on:

* Identifying revenue drivers
* Understanding distribution across products, categories, and customers
* Highlighting actionable insights rather than just descriptive statistics

The value of the project lies not only in executing analysis, but in making intentional decisions that lead to meaningful conclusions.

---

## 6. Reflection

Each decision — from data structuring to visualization and dashboard design — aimed to keep the analysis:

* Relevant
* Clear
* Aligned with the business objective

The project evolved from a simple analysis into a more complete data workflow, incorporating data engineering, analysis, and visualization.

The goal was to demonstrate not only technical skills, but also structured thinking and a business-oriented mindset.
